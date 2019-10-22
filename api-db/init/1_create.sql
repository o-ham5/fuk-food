use api-db;

SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE accounts;
TRUNCATE TABLE areas;
TRUNCATE TABLE genres;
TRUNCATE TABLE situations;
TRUNCATE TABLE spots;
TRUNCATE TABLE rest_kuchikomi;

SET FOREIGN_KEY_CHECKS = 1;

ALTER TABLE accounts CHANGE date_joined  date_joined TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE accounts CHANGE bias bias FLOAT NOT NULL DEFAULT 0;
ALTER TABLE accounts CHANGE variance variance FLOAT NOT NULL DEFAULT 0;
ALTER TABLE areas CHANGE created_at  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE areas CHANGE updated_at  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE genres CHANGE created_at  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE genres CHANGE updated_at  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE situations CHANGE created_at  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE situations CHANGE updated_at  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;
ALTER TABLE areas CHANGE created_at  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE areas CHANGE updated_at  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;


-- 管理者の作成
INSERT INTO accounts (account_id, password, username, email, is_active, is_staff, is_admin) VALUES ('6dadb2ef2464765b7cad8ca3c3e2051', '1234567', 'superuser01', 'superuser01@e.com', 1, 1, 1);
INSERT INTO accounts (account_id, password, username, email, is_active, is_staff, is_admin) VALUES ('6dadb2ef2464765b7cad8ca3c3e2052', '1234567', 'superuser02', 'superuser02@e.com', 1, 1, 1);
INSERT INTO accounts (account_id, password, username, email, is_active, is_staff, is_admin) VALUES ('6dadb2ef2464765b7cad8ca3c3e2053', '1234567', 'superuser03', 'superuser03@e.com', 1, 1, 1);

-- 一般ユーザーの作成
INSERT INTO accounts (account_id, password, username, email, is_active, is_staff, is_admin) VALUES ('6dadb2ef2464765b7cad8ca3c3e2054', '1234567', 'user01', 'user01@e.com', 1, 0, 0);
INSERT INTO accounts (account_id, password, username, email, is_active, is_staff, is_admin) VALUES ('6dadb2ef2464765b7cad8ca3c3e2055', '1234567', 'user02', 'user02@e.com', 1, 0, 0);
INSERT INTO accounts (account_id, password, username, email, is_active, is_staff, is_admin) VALUES ('6dadb2ef2464765b7cad8ca3c3e2056', '1234567', 'user03', 'user03@e.com', 1, 0, 0);
INSERT INTO accounts (account_id, password, username, email, is_active, is_staff, is_admin) VALUES ('6dadb2ef2464765b7cad8ca3c3e2057', '1234567', 'user04', 'user04@e.com', 1, 0, 0);
INSERT INTO accounts (account_id, password, username, email, is_active, is_staff, is_admin) VALUES ('6dadb2ef2464765b7cad8ca3c3e2058', '1234567', 'user05', 'user05@e.com', 1, 0, 0);

-- エリアの作成
INSERT INTO areas (area_name) VALUES ('天神');
INSERT INTO areas (area_name) VALUES ('博多');
INSERT INTO areas (area_name) VALUES ('薬院');
INSERT INTO areas (area_name) VALUES ('大橋');
INSERT INTO areas (area_name) VALUES ('九大学研都市');
INSERT INTO areas (area_name) VALUES ('周船寺');
INSERT INTO areas (area_name) VALUES ('今宿');
INSERT INTO areas (area_name) VALUES ('姪浜');
INSERT INTO areas (area_name) VALUES ('唐人町');
INSERT INTO areas (area_name) VALUES ('赤坂');
INSERT INTO areas (area_name) VALUES ('西新');
INSERT INTO areas (area_name) VALUES ('祇園');
INSERT INTO areas (area_name) VALUES ('中洲');
INSERT INTO areas (area_name) VALUES ('大名');

-- ジャンルの作成
INSERT INTO genres (genre_name) VALUES ('寿司');
INSERT INTO genres (genre_name) VALUES ('魚介料理');
INSERT INTO genres (genre_name) VALUES ('天ぷら');
INSERT INTO genres (genre_name) VALUES ('とんかつ');
INSERT INTO genres (genre_name) VALUES ('串揚げ');
INSERT INTO genres (genre_name) VALUES ('そば');
INSERT INTO genres (genre_name) VALUES ('うどん');
INSERT INTO genres (genre_name) VALUES ('うなぎ');
INSERT INTO genres (genre_name) VALUES ('焼き鳥');
INSERT INTO genres (genre_name) VALUES ('串焼き');
INSERT INTO genres (genre_name) VALUES ('すき焼き');
INSERT INTO genres (genre_name) VALUES ('しゃぶしゃぶ');
INSERT INTO genres (genre_name) VALUES ('お好み焼き');
INSERT INTO genres (genre_name) VALUES ('丼もの');
INSERT INTO genres (genre_name) VALUES ('ステーキ');
INSERT INTO genres (genre_name) VALUES ('ハンバーグ');
INSERT INTO genres (genre_name) VALUES ('洋食');
INSERT INTO genres (genre_name) VALUES ('パスタ');
INSERT INTO genres (genre_name) VALUES ('ピザ');
INSERT INTO genres (genre_name) VALUES ('フレンチ');
INSERT INTO genres (genre_name) VALUES ('スペイン料理');
INSERT INTO genres (genre_name) VALUES ('中華');
INSERT INTO genres (genre_name) VALUES ('韓国料理');
INSERT INTO genres (genre_name) VALUES ('カレー');
INSERT INTO genres (genre_name) VALUES ('焼肉');
INSERT INTO genres (genre_name) VALUES ('もつ鍋');
INSERT INTO genres (genre_name) VALUES ('水炊き');
INSERT INTO genres (genre_name) VALUES ('居酒屋');
INSERT INTO genres (genre_name) VALUES ('創作料理');
INSERT INTO genres (genre_name) VALUES ('ダイニングバー');
INSERT INTO genres (genre_name) VALUES ('カフェ');

-- シチュエーション
INSERT INTO situations (situation_name) VALUES ('宴会');
INSERT INTO situations (situation_name) VALUES ('友人');
INSERT INTO situations (situation_name) VALUES ('デート');
INSERT INTO situations (situation_name) VALUES ('接待');
INSERT INTO situations (situation_name) VALUES ('家族');
INSERT INTO situations (situation_name) VALUES ('合コン');

