import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, solve, Eq

class QuadraticGraph(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # PyQt 위젯 초기화
        self.setWindowTitle('sniper_game')  # 윈도우 제목 변경
        self.setGeometry(100, 100, 800, 600)

        # 입력 위젯 초기화
        input_width = 200
        self.target_distance_label = QLabel('target_distance:', self)
        self.target_distance_edit = QLineEdit(self)
        self.target_distance_edit.setFixedWidth(input_width)

        self.a_label = QLabel('a:', self)
        self.a_edit = QLineEdit(self)
        self.a_edit.setFixedWidth(input_width)

        self.vertex_y_label = QLabel('Maximum_altitude:', self)
        self.vertex_y_edit = QLineEdit(self)
        self.vertex_y_edit.setFixedWidth(input_width)

        self.point_a_label = QLabel('target_size:', self)
        self.point_a_edit = QLineEdit(self)
        self.point_a_edit.setFixedWidth(input_width)

        # 게임 설명 라벨 추가
        self.game_description_label = QLabel('탄도학공식: a * (x_values-target_distance)**2 + Maximum_altitude\n t_distance에 타겟과의 거리를 입력하세요.\n target_size에는 타겟의 크기를 넣어주세요.\n a는 탄도학 공식에서 타겟을 맞출수있는 적절한 기울기를 넣어 주세요.\n Maximum_altitude에는 탄환의 궤적이 타겟과 닿을수있는 적절한 값을 넣어주세요. 타겟의 최상단을 맞춰야 헤드샷(사살)판정으로 명중입니다.\n 헤드샷이 아니면 히트판정이 나오고 사살하지 않은것으로 처리됩니다\n 직접 계산하여 헤드샷을 노리세요!', self)
        self.game_description_label.setStyleSheet('font-weight: bold; font-size: 12px;')
        self.game_description_label.setAlignment(Qt.AlignRight)

    
        self.plot_button = QPushButton('FIRE', self)
        self.plot_button.clicked.connect(self.trajectory_function)

        # Matplotlib 그래프 초기화
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.game_description_label)
        layout.addWidget(self.target_distance_label)
        layout.addWidget(self.target_distance_edit)
        layout.addWidget(self.a_label)
        layout.addWidget(self.a_edit)
        layout.addWidget(self.vertex_y_label)
        layout.addWidget(self.vertex_y_edit)
        layout.addWidget(self.point_a_label)
        layout.addWidget(self.point_a_edit)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.canvas)

        self.setLayout(layout)

    def trajectory_function(self):
        # 기존 그래프를 지우고, 새로운 그래프를 그립니다.
        self.ax.clear()

        

        try:
            # 입력값 가져오기
            target_distance = float(self.target_distance_edit.text())
            a = float(self.a_edit.text())
            vertex_y = float(self.vertex_y_edit.text())

            # 주어진 점들 가져오기
            point_a_y = float(self.point_a_edit.text())

            if a * (0 - float(self.target_distance_edit.text()))**2 + vertex_y != 0:
                raise ValueError("입력값 오류. 발사지점은 원점입니다")
            
            

            
             # x 값 생성
            x_values = np.linspace(0, target_distance, 100)

            # 이차함수 값 계산
            y_values = a * (x_values-float(self.target_distance_edit.text()))**2 + vertex_y

            # 이차함수 그래프 추가
            self.ax.plot(x_values, y_values, label=f'trajestory_of_bullet (a={a}, Vertex Y: {vertex_y})')

            # 주어진 점들을 그래프에 추가
            self.ax.scatter([target_distance,target_distance], [point_a_y, 0], color='red', label='target_edge')

            # 선분 AB를 그래프에 추가
            self.ax.plot([target_distance,target_distance], [point_a_y, 0], linestyle='--', color='green', label='target_size')

            # 그래프 설정
            self.ax.set_title('trajestory_of_bullet')
            self.ax.set_xlabel('x')
            self.ax.set_ylabel('f(x)')
            self.ax.legend()
            self.ax.grid(True)

            # 그래프 업데이트
            self.canvas.draw()

            # 입력값 확인
            input_x = float(self.target_distance_edit.text())
            input_y = float(self.point_a_edit.text())

            # 교차 여부 확인
            for i in range(len(x_values) - 1):
                x1, x2 = x_values[i], x_values[i+1]
                y1, y2 = y_values[i], y_values[i+1]

                # 입력값과 그래프의 교차 여부 확인
                if (y1 - input_y) * (y2 - input_y) <= 0 and (x1 <= input_x <= x2 or x2 <= input_x <= x1):
                    print("헤드샷! 목표를 사살하였습니다.")
                    return

            print("히트! 사살못함.")

        except ValueError as e:
            print(f"잘못된 입력 값입니다: {e}")


        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuadraticGraph()
    window.show()
    sys.exit(app.exec_())
