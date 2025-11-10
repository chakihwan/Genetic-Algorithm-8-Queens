import matplotlib.pyplot as plt
import numpy as np

# PDF에서 찾은 최종 해답
solution = [7, 3, 8, 2, 5, 1, 6, 4] # 1-based index
board_size = 8

# 1. 체스판 배경 생성
board = np.zeros((board_size, board_size))
board[1::2, 0::2] = 1 # 흑백 격자 무늬
board[0::2, 1::2] = 1
plt.imshow(board, cmap='binary') # 흑백으로 표시

# 2. 퀸 배치
for col, row in enumerate(solution):
    # plt.text()로 퀸(♛)을 그립니다. (row-1은 0-based index로 변환)
    plt.text(col, row - 1, '♛', fontsize=20, ha='center', va='center', color='red')

plt.title(f"Final Solution (Fitness: 28)")

# --- [수정된 부분] ---
# 축의 '위치'는 0-7 (np.arange(8))을 그대로 사용하고,
# 축에 '표시될 이름'만 1-8 (range(1, 9))로 설정합니다.
ticks_range = np.arange(board_size)
labels_range = [str(i) for i in range(1, board_size + 1)]

plt.xticks(ticks_range, labels_range) # X축 레이블을 1~8로 변경
plt.yticks(ticks_range, labels_range) # Y축 레이블을 1~8로 변경
# --- [여기까지] ---

plt.show()