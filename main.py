import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtGui import QPixmap, QGuiApplication
from PySide6.QtCore import Qt, QThread, Signal, Slot, QMutex
from PySide6 import QtGui
from ui_mainwindow import Ui_MainWindow
from ui_demowindow import Ui_DemoWindow
import numpy as np
import cv2
import torch


def list_ports():
    dev_port = 0
    working_ports = []
    while dev_port < 6:
        camera = cv2.VideoCapture(dev_port)
        if camera.isOpened():
            is_reading, img = camera.read()
            if is_reading:
                working_ports.append(dev_port)
        dev_port += 1
    return working_ports


WEBCAM_ID_1, WEBCAM_ID_2 = list_ports()[-2:]
# WEBCAM_ID_1 = 0
# WEBCAM_ID_2 = 2
MODEL = torch.hub.load('ultralytics/yolov5', "custom", path="model/best.pt")
MODEL.eval()
MODEL.max_det = 2
MODEL.conf = 0.4
THRESHOLD_TWO = 0.6
THRESHOLD_ONE = 0.7
SIDE_WEIGHT = 0.7
FRONT_WEIGHT = 0.3
MODEL_TO_CATEGORY = [
    "INJECTE PVC SUR TIGE",
    "INJECTE TPR SUR TIGE",
    "FULL INJECTE PVC",
    "FULL INJECTE PVC",
    "AUTRE",
    "AUTRE",
    "AUTRE",
    "AUTRE",
    "AUTRE",
    "AUTRE",
    "AUTRE",
    "AUTRE",
    "BOTTE TPE",
    "AUTRE",
    "AUTRE",
    "INJECTE PVC SUR TIGE"
]


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.pushButtonDemo = self.findChild(QPushButton, 'pushButtonDemo')
        self.pushButtonDemo.clicked.connect(self.change_to_demo)

        # Set Window to center
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

    def change_to_demo(self):
        self.demo_window = DemoWindow()
        self.demo_window.show()
        self.close()


class DemoWindow(QMainWindow):
    def __init__(self):
        super(DemoWindow, self).__init__()
        self.ui = Ui_DemoWindow()
        self.ui.setupUi(self)
        self.pushButtonBack = self.findChild(QPushButton, 'pushButtonBack')
        self.pushButtonBack.clicked.connect(self.change_to_main)
        self.displayWidth = 627
        self.displayHeight = 170

        # Set Window to center
        self.qtRectangle = self.frameGeometry()
        self.centerPoint = QGuiApplication.primaryScreen().availableGeometry().center()
        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

        # Stream videos
        self.labelVideo1 = self.findChild(QLabel, 'labelVideo1')
        self.labelVideo2 = self.findChild(QLabel, 'labelVideo2')

        self.thread1 = VideoThreadSide()
        self.thread1.change_pixmap_signal.connect(self.update_image_webcam_1)
        self.thread1.change_pixmap_signal.connect(self.get_frame_side)

        self.thread1.start()

        self.thread2 = VideoThreadFront()
        self.thread2.change_pixmap_signal.connect(self.update_image_webcam_2)
        self.thread2.change_pixmap_signal.connect(self.get_frame_front)

        self.thread2.start()

        self.mutex = QMutex()
        self.results = [None, None]

        # START images saves on click
        self.pushButtonStart = self.findChild(QPushButton, 'pushButtonStart')
        self.pushButtonStart.clicked.connect(self.detect)

        # Get predictions results
        self.labelBac = self.findChild(QLabel, 'bacPredictionLabel')

    def closeEvent(self, event):
        self.thread1.stop()
        self.thread2.stop()
        event.accept()

    @Slot(np.ndarray)
    def update_image_webcam_1(self, frame):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(frame)
        self.labelVideo1.setPixmap(qt_img)

    @Slot(np.ndarray)
    def update_image_webcam_2(self, frame):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(frame)
        self.labelVideo2.setPixmap(qt_img)

    def detect(self):
        # Directory name with model name
        self.labelBac.setText("En attente...")
        global SIDE_WEIGHT, FRONT_WEIGHT, THRESHOLD_TWO, THRESHOLD_ONE, MODEL_TO_CATEGORY
        if (self.results[0] is not None) and (self.results[1] is not None):
            predictions = MODEL(self.results)
            predictions_df = predictions.pandas().xyxy
            predictions_df = [prediction_df.sort_values(by='confidence', ascending=False).loc[:, "confidence":"name"]
                              for prediction_df in predictions_df if not prediction_df.empty]
            if len(predictions_df) > 1:
                predictions_df[0].confidence = predictions_df[0].confidence * SIDE_WEIGHT
                predictions_df[1].confidence = predictions_df[1].confidence * FRONT_WEIGHT
                prediction_df = predictions_df[0].append(predictions_df[1], ignore_index=True)\
                    .groupby(by="class").sum().reset_index().sort_values(by=['confidence'], ascending=False)
                if prediction_df.confidence[0] >= THRESHOLD_TWO:
                    self.labelBac.setText(MODEL_TO_CATEGORY[prediction_df['class'][0]])
                else:
                    self.labelBac.setText("Non reconnue, veuillez réessayez...")
                # print("Predictions Two: ", prediction_df)
            elif len(predictions_df) == 1:
                prediction_df = predictions_df[0].groupby(by="class").sum().reset_index()\
                    .sort_values(by=['confidence'], ascending=False)
                if prediction_df.confidence[0] >= THRESHOLD_ONE:
                    self.labelBac.setText(MODEL_TO_CATEGORY[prediction_df['class'][0]])
                else:
                    self.labelBac.setText("Non reconnue, veuillez réessayez...")
                # print("Prediction One : ", prediction_df)
            else:
                self.labelBac.setText("Non reconnue, veuillez réessayez...")

    def convert_cv_qt(self, frame):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_qt_format.scaled(self.displayWidth, self.displayHeight, Qt.KeepAspectRatioByExpanding)
        return QPixmap.fromImage(p)

    @Slot(np.ndarray)
    def get_frame_side(self, frame):
        self.mutex.lock()
        img = frame[..., ::-1]
        self.results[0] = img
        self.mutex.unlock()

    @Slot(np.ndarray)
    def get_frame_front(self, frame):
        self.mutex.lock()
        img = frame[..., ::-1]
        self.results[1] = img
        self.mutex.unlock()

    def change_to_main(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.thread1.stop()
        self.thread2.stop()
        self.close()


class VideoThreadSide(QThread):
    def __init__(self):
        super(VideoThreadSide, self).__init__()
        self.run_flag = True
        self.vid = cv2.VideoCapture(WEBCAM_ID_1)

    change_pixmap_signal = Signal(np.ndarray)

    def run(self):
        while self.run_flag:
            ret, frame = self.vid.read()
            if not ret:
                continue

            # Convert images to numpy arrays
            self.change_pixmap_signal.emit(frame)
        self.vid.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self.run_flag = False
        self.wait()


class VideoThreadFront(QThread):
    def __init__(self):
        super(VideoThreadFront, self).__init__()
        self.run_flag = True
        self.vid = cv2.VideoCapture(WEBCAM_ID_2)

    change_pixmap_signal = Signal(np.ndarray)

    def run(self):
        while self.run_flag:
            ret, frame = self.vid.read()
            if not ret:
                continue

            # Convert images to numpy arrays
            self.change_pixmap_signal.emit(frame)
        self.vid.release()

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self.run_flag = False
        self.wait()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
