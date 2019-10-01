## Dockerfile
### dockerfileに何を書くか
dockerfileの目的はイメージを作成すること。開発時にほとんど変更することがないベースの環境を整えることが目的になる。  
例えばdjnagoを使って開発する場合、コンテナの起動時にいちいちpip installするのはナンセンスなので、必要なモジュールをあらかじめ全てインストールしたイメージを用意しておき、実装内容はコンテナ起動時にマウントして反映させる、という使い方がベスト。
### docker-compseによる開発
```
# docker-compose.ymlで定義したdockerfileをビルドする。
$ docker-compose build

# ビルドしたイメージをdocker-composeのルールにしたがって起動する。
# この時、ローカルからのvolumeのマウントや、コンテナ間ネットワークが形成される。
$ docker-compose up -d

# ローカルで変更した実装内容を反映させる。
$ docker-compose restart

# コンテナとネットワークを削除する。
$ docker-compse down
```
### ADDのエラー
```
ADD failed: stat /var/lib/docker/tmp/docker-builder799963864/nginx/config/fuk_api_web.conf: no such file or directory
```
パスの間違い
```
(before)
ADD ./nginx/config/fuk_api_web.conf /etc/nginx/conf.d
(after)
ADD ./config/fuk_api_web.conf /etc/nginx/conf.d
```
dockerfileがある場所がADDのルートになるので、no such fileになってしまっていた。
### mysqlコンテナでDBが初期化できない
* 事象
```yml
# docker-compose.ymlにて
  api_db:
    container_name: api_db
    restart: always
    image: mysql:8.0.17
    ports:
      - "3306:3306"
    volumes:
      - ./mysql/init:/docker-entrypoint-initdb.d
      - ./mysql/data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: app_db
      MYSQL_USER: fuk
      MYSQL_PASSWORD: fuk
```
本来は、ローカルホストの./mysql/init配下においてある.sqlファイルが実行され、DBに初期データが投入される設計になっていた。  
しかし、コンテナ起動後もtableが存在しないという事象が発生した。
* 原因
```sh
# コンテナ起動時に実行される entrypoint.sh
if [ ! -d "$DATADIR/mysql" ]; then
    //Some other logic here

    for f in /docker-entrypoint-initdb.d/*; do
        case "$f" in
            *.sh)     echo "$0: running $f"; . "$f" ;;
            *.sql)    echo "$0: running $f"; "${mysql[@]}" < "$f"; echo ;;
            *.sql.gz) echo "$0: running $f"; gunzip -c "$f" | "${mysql[@]}"; echo ;;
            *)        echo "$0: ignoring $f" ;;
        esac
        echo
    done 
```
entrypoint.shにおいて、"mysql/"ディレクトリの存在チェックをしており、なかった場合にのみsqlスクリプトが実行されるようになっている。  
したがって、docker-compose runを実行する前にローカルにmysql/とバインドされたdata/ディレクトリが存在する場合、sqlスクリプトは実行されない。  
* 解決策
ローカルディレクトリのdata/を削除したうえでコンテナを起動する。
* 補足
```
# mysqlコンテナに入る
$ docker exec -it <container_id> /bin/bash

# mysql対話環境に入る
# mysql -u fuk -p
mysql> show tables;
```
### djangoでmysqlコンテナに接続できない
* 原因1: port 3306が3360になっていた -> 結構あるので注意！
* 原因2: 認証方式が対応していない
```
OperationalError: (2059, "Authentication plugin 'caching_sha2_password' cannot be loaded: The specified module could not be found.\r\n")
```
* 解決策  
以下のバインドをdocker-composeに追加する
```
./mysql/conf/:/etc/mysql/conf.d
```
ローカルのconf/ディレクトリには、default_authentication.cnfを追加
```
[mysqld]
default_authentication_plugin= mysql_native_password
```
認証方式をmysql_native_passwordに変更する。なお、変更前の認証方式はmysql8.0.xから追加されたもので、native_passwordより安全性が高いとのこと。djangoが対応していないのでしゃーない。
### DjangoのDisabled Hostエラー
* 原因1 : settings.pyのALLOWED HOSTに接続元ホストのIPが記載されていない。
* 原因2 : 接続元ホスト名に使ってはいけない文字が含まれている。特にアンダースコアが使えないことには注意！
### トラブルシューティング
下記のコマンドでコンテナ内のログをみる。
```
$ docker logs <container_id>
```
例えば、nginx用のコンテナが落ちてしまう時にはこんなログが出ている。
```
2019/09/18 15:30:28 [emerg] 1#1: no port in upstream "api_app" in /etc/nginx/conf.d/fuk_api_web.conf:31
nginx: [emerg] no port in upstream "api_app" in /etc/nginx/conf.d/fuk_api_web.conf:31
```
upstreamにhost "api_app"はいるが、portが開放されていないというエラーメッセージ。  
（確かこの時点ではapi_appコンテナに対してなんのサービスも定義していなかったことが原因。）