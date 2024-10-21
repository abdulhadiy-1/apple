from PyQt5.QtWidgets import *

class AppleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("font-size: 15px")

        self.v_main_lay = QVBoxLayout()
        self.h_mainlbl_lay = QHBoxLayout()
        self.v_help_visit_lay = QVBoxLayout()
        self.h_store_lay = QHBoxLayout()
        self.h_btns_lay = QHBoxLayout()
        self.h_ads_lay = QHBoxLayout()

        # mainlbl
        self.m1  = QLabel("Store    ")
        self.m2  = QLabel("Mac    ")
        self.m3  = QLabel("iPad    ")
        self.m4  = QLabel("iPhone    ")
        self.m5  = QLabel("Watch    ")
        self.m6  = QLabel("Vision    ")
        self.m7  = QLabel("AirPods    ")
        self.m8  = QLabel("TV & Home    ")
        self.m9  = QLabel("Entertainment    ")
        self.m10 = QLabel("Accessories    ")
        self.m11 = QLabel("Support")

        lst = [self.m1, self.m2, self.m3, self.m4, self.m5, self.m6, self.m7, self.m8, self.m9, self.m10, self.m11]
        self.h_mainlbl_lay.addStretch()
        for i in lst:
            i.setStyleSheet("font-size: 15px")
            self.h_mainlbl_lay.addWidget(i)
        self.h_mainlbl_lay.addStretch()

        # store
        self.h1  = QLabel("Need shopping help?")
        self.h2  = QLabel("Ask a Specialist")
        self.h2.setStyleSheet("color: blue")
        self.h3  = QLabel("Visit an Apple store")
        self.h4  = QLabel("Find one near you")
        self.h4.setStyleSheet("color: blue")


        lst = [self.h1, self.h2, self.h3, self.h4]
        for i in lst:
            self.v_help_visit_lay.addWidget(i)
        
        self.store_lbl = QLabel("<b>Store. The best way to buy the\nproducts you love.</b>")
        self.store_lbl.setStyleSheet("font-size: 30px")

        self.h_store_lay.addWidget(self.store_lbl)
        self.h_store_lay.addStretch()
        self.h_store_lay.addLayout(self.v_help_visit_lay)

        # btn
        self.btn1 = QPushButton("Mac")
        self.btn2 = QPushButton("iPhone")
        self.btn3 = QPushButton("iPad")
        self.btn4 = QPushButton("Apple Watch")
        self.btn5 = QPushButton("Apple Vision Pro")
        self.btn6 = QPushButton("AirPods")
        self.btn7 = QPushButton("AirTag")
        self.btn8 = QPushButton("Apple TV 4K")
        self.btn9 = QPushButton("HomePod")

        lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        for i in lst:
            i.setStyleSheet("padding-top: 150px")
            self.h_btns_lay.addWidget(i)
        
        # Ads
        self.ad1 = QLabel("<b>iPhone 16 Pro</b><br>Apple inteligence<br>from $999 or $41.62/mo. for 24 mo.")
        self.ad2 = QLabel("<b>iPad Mini</b><br>Apple inteligence<br>from $999 or $41.62/mo. for 24 mo.")
        self.ad3 = QLabel("<b>Apple watch Series 10</b><br>Apple inteligence<br>from $999 or $41.62/mo. for 24 mo.")

        self.h_ads_lay.addWidget(self.ad1)
        self.h_ads_lay.addStretch()
        self.h_ads_lay.addWidget(self.ad2)
        self.h_ads_lay.addStretch()
        self.h_ads_lay.addWidget(self.ad3)


        # main
        self.main_lbl = QLabel("<b>The latest. Take a look at what's new, right now.</b>")
        self.main_lbl.setStyleSheet("font-size: 30px")

        self.v_main_lay.addLayout(self.h_mainlbl_lay)
        self.v_main_lay.addStretch()
        self.v_main_lay.addLayout(self.h_store_lay)
        self.v_main_lay.addLayout(self.h_btns_lay)
        self.v_main_lay.addWidget(self.main_lbl)
        self.v_main_lay.addStretch()
        self.v_main_lay.addLayout(self.h_ads_lay)

        self.setLayout(self.v_main_lay)





app = QApplication([])
win = AppleWindow()
win.showMaximized()
app.exec_()

        
