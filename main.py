import matplotlib.pyplot as plt
import matplotlib.patches as patches

# フィギュアサイズはアスペクトに合わせて適当に調整
fig, ax = plt.subplots(figsize=(16, 9))

# 軸設定
ax.set_xlim(-3840, 3840)
ax.set_ylim(0, 2160)
ax.set_aspect('equal')

# 上下反転（画面っぽいY軸）
ax.invert_yaxis()

# グリッド設定（240ピクセル刻み）
x_ticks = list(range(-3840, 3841, 240))
y_ticks = list(range(0, 2161, 240))

ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.grid(True, which='both', linestyle='--', color='gray', linewidth=0.5)

# 横軸のラベルを30度傾ける
ax.set_xticklabels(x_ticks, rotation=30)

# 横軸を上側に移動
ax.xaxis.set_ticks_position('top')  # 横軸の位置を上側に設定

# 軸のラベルを追加（オプション）
ax.set_xlabel("X (pixels)")
ax.set_ylabel("Y (pixels)")
plt.title("Custom Workspace Grid (3840x2160, 240px step)")





# (0, 0) ~ (3840, 240) の位置に枠を描き、トラテープパターンで塗りつぶし（太いスラッシュ模様）
rect = patches.Rectangle((0, 0), 3840, 180, linewidth=2, facecolor='yellow', alpha=0.5, hatch='/////')
ax.add_patch(rect)

rect = patches.Rectangle((-3840, 0), 3840, 180, linewidth=2, facecolor='yellow', alpha=0.5, hatch='/////')
ax.add_patch(rect)

rect = patches.Rectangle((0, 0), 70, 2160-50, linewidth=2, facecolor='yellow', alpha=0.5, hatch='/////')
ax.add_patch(rect)

rect = patches.Rectangle((0, 2160-50), 3840, 50, linewidth=2, facecolor='yellow', alpha=0.5, hatch='/////')
ax.add_patch(rect)
















# モニタ枠線を引く
rect = patches.Rectangle((0, 0), 3840, 2160, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(rect)

rect = patches.Rectangle((-3840, 0), 3840, 2160, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(rect)













# (300, 300) ~ (600, 600) の位置に枠を描く
rect_window1 = patches.Rectangle((300, 300), 300, 300, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(rect_window1)

# (300, 300) ~ (600, 600) の中心に "Window1" ラベルを追加
ax.text(450, 450, 'Window1', color='black', ha='center', va='center', fontsize=12)














plt.show()
