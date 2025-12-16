import pandas as pd

#pathlibというモジュールから、Pathだけを読み込む
from pathlib import Path

#__file__というのは変数名(Python標準で用意してくれている変数)
#Path()は括弧内の引数をパスオブジェクトに変換する関数（OSの差異を吸収してくれる）

BASE_PATH = Path(__file__).resolve().parent
csv_path = BASE_PATH / '../../100knock-data_analytics/1/customer_master.csv'

customer_master = pd.read_csv(csv_path)
print(customer_master.head())