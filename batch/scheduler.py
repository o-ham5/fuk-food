import schedule
import time

from utils.nearest_neighbors import *
from utils.scoring import *

# 毎時間ごとにjobを実行
schedule.every(5).minutes.do(job_knn)
schedule.every(5).minutes.do(job_scoring)

while True:
    schedule.run_pending()
    time.sleep(1)
