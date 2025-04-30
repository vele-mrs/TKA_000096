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
import pandas as pd

# User Library
sys.path.append("C:/workspace/projects/development/_library/python")
from user_print import advanceprint, progress_print, save_log # type: ignore
from user_timestamp import TimeStamp # type: ignore
from user_data import set_filepath # type: ignore

# User Module
sys.path.append(os.path.join(os.path.dirname(__file__), "module"))
# from workspace import WorkSpace # type: ignore

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
class WorkSpace:
    def __init__(self):
        pass


    ############################################################
    # 描画エリアをクリアするメソッド
    def clear_view_area(self):
        if hasattr(self, 'ax'):
            self.ax.cla()  # 軸内をクリア（グリッドや描画された線など）
            self.set_view_area()  # 軸設定を再適用

    ############################################################
    # 描画エリア設定メソッド
    def set_view_area(self):
        # フィギュアサイズはアスペクトに合わせて適当に調整
        fig, self.ax = plt.subplots(figsize=(16, 9))

        # 軸設定
        self.ax.set_xlim(-3840, 3840)
        self.ax.set_ylim(0, 2160)
        self.ax.set_aspect('equal')

        # 上下反転（画面っぽいY軸）
        self.ax.invert_yaxis()

        # グリッド設定（240ピクセル刻み）
        x_ticks = list(range(-3840, 3840+1, 240))
        y_ticks = list(range(0, 2160+1, 240))

        self.ax.set_xticks(x_ticks)
        self.ax.set_yticks(y_ticks)
        self.ax.grid(True, which='both', linestyle='--', color='gray', linewidth=0.5)

        # 横軸のラベルを30度傾ける
        self.ax.set_xticklabels(x_ticks, rotation=30)

        # 横軸を上側に移動
        self.ax.xaxis.set_ticks_position('top')  # 横軸の位置を上側に設定

        # 軸のラベルを追加（オプション）
        self.ax.set_xlabel("X (pixels)")
        self.ax.set_ylabel("Y (pixels)")
        plt.title("Custom Workspace Grid (3840x2160, 240px step)")


    ############################################################
    # モニタ領域設定メソッド
    def set_monitor_area(self):

        # モニタ枠線を引く
        rect = patches.Rectangle((0, 0), 3840, 2160, linewidth=2, edgecolor='black', facecolor='none')
        self.ax.add_patch(rect)

        rect = patches.Rectangle((-3840, 0), 3840, 2160, linewidth=2, edgecolor='black', facecolor='none')
        self.ax.add_patch(rect)




    ############################################################
    # CSV Readメソッド
    def read_csv(self):
        filepath = set_filepath(["data", "WorkSpace"], self.filename, self.num, "csv")
        self.df = pd.read_csv(filepath)

    ############################################################
    # CSV Writeメソッド
    def write_csv(self):
        filepath = set_filepath(["data", "WorkSpace"], self.filename, self.num, "csv")
        self.df.to_csv(filepath, index=False)








    ############################################################
    # 禁止エリア設定メソッド
    def set_restricted_area(self):

        self.filename = "restricted_area"
        self.num = 0
        self.read_csv()
        print(self.df)

        self.df['x'] = 1
        self.df['y'] = 1
        self.df['width'] = 1
        self.df['high'] = 1
        self.write_csv()


        

        # エリアを設定
        self.x1 = 100
        self.y1 = 100
        self.x2 = 500
        self.y2 = 500
        self.xpadding = 0
        self.ypadding = 0

        # x,y,width,hightを生成
        self.make_rectangle()

        print(self.x     )
        print(self.y     )
        print(self.width )
        print(self.height)


        self.set_restricted_area_single()

    ############################################################
    # 禁止エリア設定メソッド
    def set_restricted_area_single(self):
        # トラテープ部の設定
        linewidth   = 2
        facecolor   = 'yellow'
        alpha       = 0.5
        hatch       = '/////'

        # rectangle
        rect = patches.Rectangle(
            (self.x, self.y), 
            self.width, 
            self.height, 
            linewidth=linewidth, 
            facecolor=facecolor, 
            alpha=alpha, 
            hatch=hatch
            )
        self.ax.add_patch(rect)


    def set_restricted_area_single_old(self):
        # (0, 0) ~ (3840, 240) の位置に枠を描き、トラテープパターンで塗りつぶし（太いスラッシュ模様）
        rect = patches.Rectangle((0, 0), 3840, 180, linewidth=2, facecolor='yellow', alpha=0.5, hatch='/////')
        self.ax.add_patch(rect)

        rect = patches.Rectangle((-3840, 0), 3840, 180, linewidth=2, facecolor='yellow', alpha=0.5, hatch='/////')
        self.ax.add_patch(rect)

        rect = patches.Rectangle((0, 0), 70, 2160-50, linewidth=2, facecolor='yellow', alpha=0.5, hatch='/////')
        self.ax.add_patch(rect)

        rect = patches.Rectangle((0, 2160-50), 3840, 50, linewidth=2, facecolor='yellow', alpha=0.5, hatch='/////')
        self.ax.add_patch(rect)


    ############################################################
    # (x1,y1),(x2,y2)から(x,y), width, highを生成するメソッド
    def make_rectangle(self):
        self.x      = min(self.x1 , self.x2) + self.xpadding
        self.y      = min(self.y1 , self.y2) + self.ypadding
        self.width  = abs(self.x2 - self.x1) - self.xpadding
        self.height = abs(self.y2 - self.y1) - self.ypadding

    ############################################################
    # ワークスペースメソッド



    ############################################################
    # ワークスペース設定メソッド
    def set_workspace_area(self):
        # (300, 300) ~ (600, 600) の位置に枠を描く
        rect_window1 = patches.Rectangle((300, 300), 300, 300, linewidth=2, edgecolor='black', facecolor='none')
        self.ax.add_patch(rect_window1)

        # (300, 300) ~ (600, 600) の中心に "Window1" ラベルを追加
        self.ax.text(450, 450, 'Window2', color='black', ha='center', va='center', fontsize=12)


    ############################################################
    # ワークスペース保存メソッド
    def save_workspace_png(self, num):

        # グラフを保存
        filepath = set_filepath(["data", "WorkSpace"], "workspace", num, "png")
        plt.savefig(filepath, bbox_inches='tight', dpi=300)



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
    # [INFO]
    progress_print("start", os.path.abspath(__file__))

    # --------------------------------------------------------------------------------
    # [INFO] Phase : X - NotionClient : Get Database and convert csv and df
    # 
    PHASE += 1
    progress_print("phase", f"{PHASE} - NotionClient : Get Database and convert csv and df")
    save_log(level="INFO", comment=f"{os.path.abspath(__file__)} -> PHASE{PHASE}")

    # Notion Client
    ws = WorkSpace()

    # グラフエリアを初期化
    ws.clear_view_area()
    advanceprint('INFO', None, f"Successfully clear_view_area")

    # グラフエリアを生成
    ws.set_view_area()
    advanceprint('INFO', None, f"Successfully set_view_area")

    # モニタエリアを指定
    ws.set_monitor_area()
    advanceprint('INFO', None, f"Successfully set_monitor_area")

    # 禁止エリアを指定
    ws.set_restricted_area()
    advanceprint('INFO', None, f"Successfully set_restricted_area")


    # ワークスペースを指定
    ws.set_workspace_area()
    advanceprint('INFO', None, f"Successfully set_workspace_area")

    # ワークスペースを保存
    ws.save_workspace_png(1)
    advanceprint('INFO', None, f"Successfully save_workspace_png")

    # [INFO] - * - * - * - * - * - * - * - * - * - 
    progress_print("end", os.path.basename(__file__))


