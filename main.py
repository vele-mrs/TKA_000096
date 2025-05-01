###############################################################################
## Python Version             | 3.13.1
## Author                     | Vele
###############################################################################

## Library
import sys
import os
import configparser
import shutil
from datetime import datetime, timedelta

# Data
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# User Library
sys.path.append("C:/workspace/projects/development/_library/python")
from user_print import advanceprint, progress_print, save_log # type: ignore
from user_timestamp import TimeStamp # type: ignore
from user_data import set_filepath # type: ignore

# User Module
sys.path.append(os.path.join(os.path.dirname(__file__), "module"))
from workspace import WorkSpace # type: ignore

###############################################################################
## PARAMETER

# Initialize
PHASE = 0

# config.iniファイルの読み込み
config = configparser.ConfigParser()
config.read('config.ini')

# TimeStampの読み込み
ts = TimeStamp()
yyyymmdd_today = ts.yyyymmdd_today()
yyyymmdd_yesterday = ts.yyyymmdd_yesterday()

## ------------------------------------------------------------------------- ##
##                                                                           ##
##      `7MMM.     ,MMF'      db      `7MMF'`7MN.   `7MF'                    ## 
##        MMMb    dPMM       ;MM:       MM    MMN.    M                      ## 
##        M YM   ,M MM      ,V^MM.      MM    M YMb   M                      ## 
##        M  Mb  M' MM     ,M  `MM      MM    M  `MN. M                      ## 
##        M  YM.P'  MM     AbmmmqMA     MM    M   `MM.M                      ## 
##        M  `YM'   MM    A'     VML    MM    M     YMM                      ## 
##      .JML. `'  .JMML..AMA.   .AMMA..JMML..JML.    YM                      ## 
##                                                                           ##
## ------------------------------------------------------------------------- ##
## Main
if __name__ == "__main__":

    # [INFO]  - * - * - * - * - * - * - * - * - * - 
    progress_print("start", os.path.abspath(__file__))
    



    # --------------------------------------------------------------------------------
    # [INFO] Phase : X - NotionClient : Get Database and convert csv and df
    # 
    PHASE += 1
    progress_print("phase", f"{PHASE} - NotionClient : Get Database and convert csv and df")
    save_log(level="INFO", comment=f"{os.path.abspath(__file__)} -> PHASE{PHASE}")



    # [INFO] - * - * - * - * - * - * - * - * - * - 
    progress_print("end", os.path.basename(__file__))


    # WorkSpace
    ws = WorkSpace(
        mon_w = 3840,
        mon_h = 2160,
        grid  = 240
    )

    # エリアを描画
    ws.draw_area()
    advanceprint('INFO', None, f"Successfully draw_area")



    # [INFO] - * - * - * - * - * - * - * - * - * - 
    progress_print("end", os.path.basename(__file__))
