#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel, QPushButton
from PyQt5.QtCore import *
import rospy
from std_msgs.msg import Float64

class YFRobotController(QWidget):
    def __init__(self, parent = None) -> None:
        super(YFRobotController, self).__init__(parent)
        self.initROS()
        self.initUI()

    def initROS(self):
        try:
            self.pub6 = rospy.Publisher('/yfrobot/servo1_to_2_servo_position_controller/command', Float64, queue_size=10)
            self.pub2 = rospy.Publisher('/yfrobot/servo2_to_1_ib_servo_position_controller/command', Float64, queue_size=10)
            self.pub3 = rospy.Publisher('/yfrobot/ib_to_3_servo_servo_position_controller/command', Float64, queue_size=10)
            self.pub = rospy.Publisher('/yfrobot/servo4_to_3_ib_servo_position_controller/command', Float64, queue_size=10)
            self.pub4 = rospy.Publisher('/yfrobot/servo5_to_grab_base_servo_position_controller/command', Float64, queue_size=10)
            self.pub5 = rospy.Publisher('/yfrobot/servo6_to_right_grab_servo_position_controller/command', Float64, queue_size=10)
            rospy.init_node('yf_publisher', anonymous=True)
        except rospy.ROSInterruptException:
            pass

    def initUI(self):
        layout = QVBoxLayout()

        label1 = QLabel("Servo 1")
        self.slServo1 = QSlider(Qt.Horizontal)
        self.slServo1.setMinimum(-314)
        self.slServo1.setMaximum(314)
        self.slServo1.setTickPosition(QSlider.TicksBelow)
        self.slServo1.setTickInterval(1)
        self.slServo1.valueChanged.connect(self.sl1Valuechange)

        label2 = QLabel("Servo 2")
        self.slServo2 = QSlider(Qt.Horizontal)
        self.slServo2.setMinimum(-200)
        self.slServo2.setMaximum(200)
        self.slServo2.setTickPosition(QSlider.TicksBelow)
        self.slServo2.setTickInterval(1)
        self.slServo2.valueChanged.connect(self.sl2Valuechange)

        label3 = QLabel("Servo 3")
        self.slServo3 = QSlider(Qt.Horizontal)
        self.slServo3.setMinimum(-125)
        self.slServo3.setMaximum(314)
        self.slServo3.setTickPosition(QSlider.TicksBelow)
        self.slServo3.setTickInterval(1)
        self.slServo3.valueChanged.connect(self.sl3Valuechange)

        label4 = QLabel("Servo 4")
        self.slServo4 = QSlider(Qt.Horizontal)
        self.slServo4.setMinimum(-250)
        self.slServo4.setMaximum(250)
        self.slServo4.setValue(0)
        self.slServo4.setTickPosition(QSlider.TicksBelow)
        self.slServo4.setTickInterval(1)
        self.slServo4.valueChanged.connect(self.sl4Valuechange)

        label5 = QLabel("Servo 5")
        self.slServo5 = QSlider(Qt.Horizontal)
        self.slServo5.setMinimum(-314)
        self.slServo5.setMaximum(314)
        self.slServo5.setValue(0)
        self.slServo5.setTickPosition(QSlider.TicksBelow)
        self.slServo5.setTickInterval(1)
        self.slServo5.valueChanged.connect(self.sl5Valuechange)

        label6 = QLabel("Servo 6")
        self.slServo6 = QSlider(Qt.Horizontal)
        self.slServo6.setMinimum(10)
        self.slServo6.setMaximum(78)
        self.slServo6.setValue(10)
        self.slServo6.setTickPosition(QSlider.TicksBelow)
        self.slServo6.setTickInterval(1)
        self.slServo6.valueChanged.connect(self.sl6Valuechange)

        btn = QPushButton('Reset')
        btn.clicked.connect(self.button1_clicked)


        layout.addWidget(label1)
        layout.addWidget(self.slServo1)
        layout.addWidget(label2)
        layout.addWidget(self.slServo2)
        layout.addWidget(label3)
        layout.addWidget(self.slServo3)
        layout.addWidget(label4)
        layout.addWidget(self.slServo4)
        layout.addWidget(label5)
        layout.addWidget(self.slServo5)
        layout.addWidget(label6)
        layout.addWidget(self.slServo6)
        layout.addWidget(btn)

        self.setLayout(layout)

    def sl1Valuechange(self):
        angle = self.slServo1.value() / 100
        rospy.loginfo(angle)
        self.pub6.publish(angle)

    def sl2Valuechange(self):
        angle = self.slServo2.value() / 100
        rospy.loginfo(angle)
        self.pub2.publish(angle)

    def sl3Valuechange(self):
        angle = self.slServo3.value() / 100
        rospy.loginfo(angle)
        self.pub3.publish(angle)

    def sl4Valuechange(self):
        angle = self.slServo4.value() / 100
        rospy.loginfo(angle)
        self.pub.publish(angle)

    def sl5Valuechange(self):
        angle = self.slServo5.value() / 100
        rospy.loginfo(angle)
        self.pub4.publish(angle)

    def sl6Valuechange(self):
        angle = self.slServo6.value() / 100
        rospy.loginfo(angle)
        self.pub5.publish(angle)

    def button1_clicked(self):
        self.slServo1.setValue(0)
        self.slServo2.setValue(0)
        self.slServo3.setValue(0)
        self.slServo4.setValue(0)
        self.slServo5.setValue(0)
        self.slServo6.setValue(0)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = YFRobotController()
    c.resize(300, 700)
    c.move(0, 0)
    c.setWindowTitle('YFRobot Controller')
    c.show()
    sys.exit(app.exec_())
    
