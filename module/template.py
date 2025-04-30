###############################################################################
## ------------------------------------------------------------
## | Python Version             | 3.13.1
## | Development Environment    | .\.venv\Scripts\activate
## | Author                     | Vele
## | Initial Version            | 2025.1.19
## ------------------------------------------------------------
## Description
##      This code analyzes the asset status from graph.csv.
## 

###############################################################################
## PARAMETER
TIME_SLEEP = 1

###############################################################################
## Library
import sys
import os

# User Library
sys.path.append("C:/workspace/projects/development/_library/python")
from user_print import advanceprint, progress_print # type: ignore

# System


# Scraping


# Data
import pandas as pd

###############################################################################
## Option
# Pandasの浮動小数点は3桁に丸めて表示する
pd.options.display.float_format = '{:.3f}'.format
url_alignment = 50
integre_alignment       = 10
fractional_alignment    = 3


## ------------------------------------------------------------------------- ##
##                                                                           ##
##        .g8"""bgd `7MMF'            db       .M"""bgd  .M"""bgd            ## 
##      .dP'     `M   MM             ;MM:     ,MI    "Y ,MI    "Y            ## 
##      dM'       `   MM            ,V^MM.    `MMb.     `MMb.                ## 
##      MM            MM           ,M  `MM      `YMMNq.   `YMMNq.            ## 
##      MM.           MM      ,    AbmmmqMA   .     `MM .     `MM            ## 
##      `Mb.     ,'   MM     ,M   A'     VML  Mb     dM Mb     dM            ## 
##        `"bmmmd'  .JMMmmmmMMM .AMA.   .AMMA.P"Ybmmd"  P"Ybmmd"             ## 
##                                                                           ##
## ------------------------------------------------------------------------- ##
## 価格・評価額情報を取得・計算するクラス
class Template:
    def __init__(self, data):
        self.data = data

    def show(self):
        print(self.data)



if __name__ == "__main__":

    # [INFO]
    progress_print("start", os.path.abspath(__file__))

    temp = Template("Hello, world!")
    temp.show()  # → Hello, world!

    # [INFO]
    progress_print("end", os.path.basename(__file__))


