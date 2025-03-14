import numpy as np
import pandas as pd
from deap import base, creator, tools
from functools import reduce
from dotenv import load_dotenv
import finlab
import random
import os
import pickle
from tqdm import tqdm
from finlab import data
from finlab.backtest import sim
from finlab.dataframe import FinlabDataFrame
from finlab.portfolio import Portfolio


# 載入.env檔案中的環境變數
def login_finlab():
    load_dotenv()
    # 這裡要替換成自己的FinLab VIP token
    token = os.environ.get("FINLAB_TOKEN")
    finlab.login(token)
