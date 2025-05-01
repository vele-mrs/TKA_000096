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
    def __init__(self, mon_w, mon_h, grid):
        self.mon_w = mon_w
        self.mon_h = mon_h
        self.grid  = grid
        pass


    ############################################################
    # 描画エリアをクリアするメソッド
    def clear_view_area(self):
        if hasattr(self, 'ax'):
            self.ax.cla()  # 軸内をクリア（グリッドや描画された線など）
            self.set_view_area()  # 軸設定を再適用



    ############################################################
    # エリア描画メソッド
    def draw_area(self):


        # .csvファイルの読み出し
        for filename in os.listdir(r"data/Workspace"):
            if filename.endswith('.csv'):
                self.filename, self.filenum = os.path.splitext(filename)[0].split('.')
                # 描画エリアの呼び出し
                self.set_view_area()

                # self.filename = "restricted_area"
                # self.filenum = 0
                self.load_csv()
                advanceprint('INFO', None, f"Successfully Load {self.filename}.{self.filenum}.csv")
  
                for index, row in self.df.iterrows():
                    # advanceprint('INFO', ('row', row))

                    self.type = row['type']
                    self.name = row['name']
                    self.x1 = row['x1']
                    self.x2 = row['x2']
                    self.y1 = row['y1']
                    self.y2 = row['y2']
                    self.xp = row['xp']
                    self.yp = row['yp']

                    # x,y,width,hightを生成
                    self.make_rectangle()

                    self.df.loc[index, 'x'] = int(self.x)
                    self.df.loc[index, 'y'] = int(self.y)
                    self.df.loc[index, 'w'] = int(self.w)
                    self.df.loc[index, 'h'] = int(self.h)

                    # モニタ枠線を描画する
                    if self.type=="frame":
                        self.set_frame()

                    # 禁止エリアを描画する
                    elif self.type=="redzone":
                        self.set_redzone()

                    # ウィンドウエリアを描画する
                    elif self.type=="window":
                        self.set_window()

                # print(self.df)

                # データを保存する
                self.save_csv()
                self.save_png()
                advanceprint('INFO', None, f"Successfully Save {self.filename}.{self.filenum}.csv")


    ############################################################
    # 描画エリア設定メソッド
    def set_view_area(self):
        # フィギュアサイズはアスペクトに合わせて適当に調整
        fig, self.ax = plt.subplots(figsize=(16, 9))

        # 軸設定
        self.ax.set_xlim(-self.mon_w, self.mon_w)
        self.ax.set_ylim(0, self.mon_h)
        self.ax.set_aspect('equal')

        # 上下反転（画面っぽいY軸）
        self.ax.invert_yaxis()

        # グリッド設定（240ピクセル刻み）
        x_ticks = list(range(-self.mon_w, self.mon_w+1, self.grid))
        y_ticks = list(range(0, self.mon_h+1, self.grid))

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

    ############################################################
    # モニタ枠線設定メソッド
    def set_frame(self):

        linewidth   = 4
        edgecolor   = 'black'
        facecolor   = 'none'

        # rectangle
        rect = patches.Rectangle(
            (self.x, self.y), 
            self.w, 
            self.h, 
            linewidth=linewidth, 
            edgecolor=edgecolor, 
            facecolor=facecolor, 
            )
        self.ax.add_patch(rect)

    ############################################################
    # 禁止エリア設定
    def set_redzone(self):

        linewidth   = 2
        facecolor   = 'yellow'
        alpha       = 0.5
        hatch       = '/////'

        # rectangle
        rect = patches.Rectangle(
            (self.x, self.y), 
            self.w, 
            self.h, 
            linewidth=linewidth, 
            facecolor=facecolor, 
            alpha=alpha, 
            hatch=hatch
            )
        self.ax.add_patch(rect)



    ############################################################
    # ワークスペース設定

    def set_window(self):

        # エリアを透明度ありで塗りつぶし
        linewidth   = 1
        edgecolor   = 'black'
        facecolor   = '#f2f6ff' 
        alpha       = 0.2

        rect = patches.Rectangle(
            (self.x, self.y), 
            self.w, 
            self.h, 
            linewidth=linewidth, 
            edgecolor=edgecolor, 
            facecolor=facecolor, 
            alpha=alpha, 
            )
        self.ax.add_patch(rect)

        # 枠線を透明度なしで表示
        linewidth   = 1
        edgecolor   = 'black'
        facecolor   = 'none' 
        alpha       = 1

        rect = patches.Rectangle(
            (self.x, self.y), 
            self.w, 
            self.h, 
            linewidth=linewidth, 
            edgecolor=edgecolor, 
            facecolor=facecolor, 
            alpha=alpha, 
            )
        self.ax.add_patch(rect)

        # アプリケーション名を中央に表示
        self.center_x = self.x + self.w / 2
        self.center_y = self.y + self.h / 2
        text = f"{self.name}\n\nx={self.x}\ny={self.y}\nwidth={self.w}\nhigh={self.h}"

        self.ax.text(
            self.center_x, 
            self.center_y, 
            text, 
            color='black', 
            ha='center', 
            va='center', 
            fontsize=12
            )



    ############################################################
    # ワークスペース設定メソッド
    # def set_workspace_area(self):
    #     # (300, 300) ~ (600, 600) の位置に枠を描く
    #     rect_window1 = patches.Rectangle((300, 300), 300, 300, linewidth=2, edgecolor='black', facecolor='none')
    #     self.ax.add_patch(rect_window1)

    #     # (300, 300) ~ (600, 600) の中心に "Window1" ラベルを追加
    #     self.ax.text(450, 450, 'Window2', color='black', ha='center', va='center', fontsize=12)



    ############################################################
    # (x1,y1),(x2,y2)から(x,y), width, highを生成するメソッド
    def make_rectangle(self):
        self.x = min(self.x1 , self.x2) + self.xp
        self.y = min(self.y1 , self.y2) + self.yp
        self.w = abs(self.x2 - self.x1) - self.xp
        self.h = abs(self.y2 - self.y1) - self.yp

    ############################################################
    # CSV Loadメソッド
    def load_csv(self):
        filepath = set_filepath(["data", "WorkSpace"], self.filename, self.filenum, "csv")
        self.df = pd.read_csv(filepath)

    ############################################################
    # CSV Saveメソッド
    def save_csv(self):
        filepath = set_filepath(["data", "WorkSpace"], self.filename, self.filenum, "csv")
        self.df.to_csv(filepath, index=False)


    ############################################################
    # ワークスペース保存メソッド
    def save_png(self):

        # タイトルを表示
        plt.title(self.filename)

        # グラフを保存
        filepath = set_filepath(["data", "WorkSpace"], self.filename, self.filenum, "png")
        plt.savefig(filepath, bbox_inches='tight', dpi=300)
        plt.clf()   # 現在の図をクリア（figure全体を消去）






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
    ws = WorkSpace(
        mon_w = 3840,
        mon_h = 2160,
        grid  = 240
    )

    # グラフエリアを初期化
    ws.clear_view_area()
    advanceprint('INFO', None, f"Successfully clear_view_area")

    # グラフエリアを生成
    # ws.set_view_area()
    # advanceprint('INFO', None, f"Successfully set_view_area")

    # モニタエリアを指定
    # ws.set_monitor_area()
    # advanceprint('INFO', None, f"Successfully set_monitor_area")

    # エリアを描画
    ws.draw_area()
    advanceprint('INFO', None, f"Successfully draw_area")


    # ワークスペースを保存
    # ws.save_workspace_png(1)
    # advanceprint('INFO', None, f"Successfully save_workspace_png")

    # [INFO] - * - * - * - * - * - * - * - * - * - 
    progress_print("end", os.path.basename(__file__))


