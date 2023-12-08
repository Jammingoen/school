import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class QuadraticGraph(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # PyQt 위젯 초기화
        self.setWindowTitle('sniper_game')  # 윈도우 제목 변경
        self.setGeometry(100, 100, 800, 600)

        # 입력 위젯 초기화
        self.target_distance_label = QLabel('target_distance:', self)
        self.target_distance_edit = QLineEdit(self)

        self.a_label = QLabel('a:', self)
        self.a_edit = QLineEdit(self)

        self.vertex_y_label = QLabel('Maximum_altitude:', self)
        self.vertex_y_edit = QLineEdit(self)

        self.point_a_label = QLabel('target_size:', self)
        self.point_a_edit = QLineEdit(self)


        self.plot_button = QPushButton('FIRE', self)
        self.plot_button.clicked.connect(self.plot_quadratic)

        # Matplotlib 그래프 초기화
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # 레이아웃 설정
        layout = QVBoxLayout()
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

    def plot_quadratic(self):
        # 기존 그래프를 지우고, 새로운 그래프를 그립니다.
        self.ax.clear()

        try:
            # 입력값 가져오기
            target_distance = float(self.target_distance_edit.text())
            a = float(self.a_edit.text())
            vertex_y = float(self.vertex_y_edit.text())

            # 주어진 점들 가져오기
            point_a_y = float(self.point_a_edit.text())

            
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

        except ValueError:
            print("잘못된 입력 값입니다.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QuadraticGraph()
    window.show()
    sys.exit(app.exec_())
