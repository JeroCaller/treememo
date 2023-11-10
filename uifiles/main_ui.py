# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFontComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QSplitter, QStatusBar, QTextEdit, QToolBar,
    QTreeWidget, QTreeWidgetItem, QWidget)
from .resources import iconset_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(997, 638)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon = QIcon()
        icon.addFile(u":/icons/icons/save.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionOpenFolder = QAction(MainWindow)
        self.actionOpenFolder.setObjectName(u"actionOpenFolder")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/open_folder.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpenFolder.setIcon(icon1)
        self.actionCreateNewRootFolder = QAction(MainWindow)
        self.actionCreateNewRootFolder.setObjectName(u"actionCreateNewRootFolder")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add_folder.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCreateNewRootFolder.setIcon(icon2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fontComboBox = QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setMinimumSize(QSize(0, 0))
        self.fontComboBox.setMaximumSize(QSize(1677215, 16777215))
        self.fontComboBox.setEditable(True)

        self.horizontalLayout_4.addWidget(self.fontComboBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setEnabled(True)
        self.spinBox.setMinimumSize(QSize(55, 0))
        self.spinBox.setMaximumSize(QSize(1677215, 16777215))
        self.spinBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.spinBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonLeftAlign = QPushButton(self.centralwidget)
        self.pushButtonLeftAlign.setObjectName(u"pushButtonLeftAlign")
        self.pushButtonLeftAlign.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLeftAlign.sizePolicy().hasHeightForWidth())
        self.pushButtonLeftAlign.setSizePolicy(sizePolicy)
        self.pushButtonLeftAlign.setMinimumSize(QSize(32, 32))
        self.pushButtonLeftAlign.setMaximumSize(QSize(32, 32))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/text_left_align.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonLeftAlign.setIcon(icon3)
        self.pushButtonLeftAlign.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.pushButtonLeftAlign)

        self.pushButtonCenterAlign = QPushButton(self.centralwidget)
        self.pushButtonCenterAlign.setObjectName(u"pushButtonCenterAlign")
        sizePolicy.setHeightForWidth(self.pushButtonCenterAlign.sizePolicy().hasHeightForWidth())
        self.pushButtonCenterAlign.setSizePolicy(sizePolicy)
        self.pushButtonCenterAlign.setMinimumSize(QSize(32, 32))
        self.pushButtonCenterAlign.setMaximumSize(QSize(32, 32))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/text_center_align.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonCenterAlign.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.pushButtonCenterAlign)

        self.pushButtonRightAlign = QPushButton(self.centralwidget)
        self.pushButtonRightAlign.setObjectName(u"pushButtonRightAlign")
        sizePolicy.setHeightForWidth(self.pushButtonRightAlign.sizePolicy().hasHeightForWidth())
        self.pushButtonRightAlign.setSizePolicy(sizePolicy)
        self.pushButtonRightAlign.setMinimumSize(QSize(32, 32))
        self.pushButtonRightAlign.setMaximumSize(QSize(32, 32))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/text_right_align.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRightAlign.setIcon(icon5)

        self.horizontalLayout_2.addWidget(self.pushButtonRightAlign)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonChangeTextStyle = QPushButton(self.centralwidget)
        self.pushButtonChangeTextStyle.setObjectName(u"pushButtonChangeTextStyle")
        sizePolicy.setHeightForWidth(self.pushButtonChangeTextStyle.sizePolicy().hasHeightForWidth())
        self.pushButtonChangeTextStyle.setSizePolicy(sizePolicy)
        self.pushButtonChangeTextStyle.setMinimumSize(QSize(32, 32))
        self.pushButtonChangeTextStyle.setMaximumSize(QSize(32, 32))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/bold_letter.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonChangeTextStyle.setIcon(icon6)
        self.pushButtonChangeTextStyle.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.pushButtonChangeTextStyle)

        self.pushButtonAddImage = QPushButton(self.centralwidget)
        self.pushButtonAddImage.setObjectName(u"pushButtonAddImage")
        sizePolicy.setHeightForWidth(self.pushButtonAddImage.sizePolicy().hasHeightForWidth())
        self.pushButtonAddImage.setSizePolicy(sizePolicy)
        self.pushButtonAddImage.setMinimumSize(QSize(32, 32))
        self.pushButtonAddImage.setMaximumSize(QSize(32, 32))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/image.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddImage.setIcon(icon7)
        self.pushButtonAddImage.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.pushButtonAddImage)

        self.pushButtonWriteReadMode = QPushButton(self.centralwidget)
        self.pushButtonWriteReadMode.setObjectName(u"pushButtonWriteReadMode")
        sizePolicy.setHeightForWidth(self.pushButtonWriteReadMode.sizePolicy().hasHeightForWidth())
        self.pushButtonWriteReadMode.setSizePolicy(sizePolicy)
        self.pushButtonWriteReadMode.setMinimumSize(QSize(32, 32))
        self.pushButtonWriteReadMode.setMaximumSize(QSize(32, 32))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/pencil.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonWriteReadMode.setIcon(icon8)
        self.pushButtonWriteReadMode.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.pushButtonWriteReadMode)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.gridLayout = QGridLayout(self.layoutWidget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonAddFile = QPushButton(self.layoutWidget_2)
        self.pushButtonAddFile.setObjectName(u"pushButtonAddFile")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/add_new_file.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonAddFile.setIcon(icon9)

        self.gridLayout.addWidget(self.pushButtonAddFile, 0, 0, 1, 1)

        self.pushButtonAddFolder = QPushButton(self.layoutWidget_2)
        self.pushButtonAddFolder.setObjectName(u"pushButtonAddFolder")

        self.gridLayout.addWidget(self.pushButtonAddFolder, 0, 1, 1, 1)

        self.treeWidget = QTreeWidget(self.layoutWidget_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.header().setVisible(True)

        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 2)

        self.splitter.addWidget(self.layoutWidget_2)
        self.textEdit = QTextEdit(self.splitter)
        self.textEdit.setObjectName(u"textEdit")
        self.splitter.addWidget(self.textEdit)

        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 997, 22))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBarMain = QToolBar(MainWindow)
        self.toolBarMain.setObjectName(u"toolBarMain")
        self.toolBarMain.setEnabled(True)
        self.toolBarMain.setMovable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBarMain)

        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionOpenFolder)
        self.menu.addAction(self.actionCreateNewRootFolder)
        self.menu_2.addAction(self.actionAbout)
        self.toolBarMain.addAction(self.actionSave)
        self.toolBarMain.addAction(self.actionOpenFolder)
        self.toolBarMain.addAction(self.actionCreateNewRootFolder)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"\ubaa8\ub4e0 \ud30c\uc77c \uc800\uc7a5", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpenFolder.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc5f4\uae30", None))
#if QT_CONFIG(tooltip)
        self.actionOpenFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc5f4\uae30", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionOpenFolder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionCreateNewRootFolder.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ub8e8\ud2b8 \ud3f4\ub354 \uc0dd\uc131", None))
#if QT_CONFIG(tooltip)
        self.actionCreateNewRootFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\uc0c8 \ub8e8\ud2b8 \ud3f4\ub354 \uc0dd\uc131", None))
#endif // QT_CONFIG(tooltip)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uae00\uc790 \ud06c\uae30", None))
#if QT_CONFIG(tooltip)
        self.pushButtonLeftAlign.setToolTip(QCoreApplication.translate("MainWindow", u"\uc67c\ucabd \uc815\ub82c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonLeftAlign.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonCenterAlign.setToolTip(QCoreApplication.translate("MainWindow", u"\uac00\uc6b4\ub370 \uc815\ub82c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCenterAlign.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonRightAlign.setToolTip(QCoreApplication.translate("MainWindow", u"\uc624\ub978\ucabd \uc815\ub82c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRightAlign.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonChangeTextStyle.setToolTip(QCoreApplication.translate("MainWindow", u"\uae00\uc790 \uc2a4\ud0c0\uc77c", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonChangeTextStyle.setText("")
        self.pushButtonAddImage.setText("")
        self.pushButtonWriteReadMode.setText("")
        self.pushButtonAddFile.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \ucd94\uac00", None))
        self.pushButtonAddFolder.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \ucd94\uac00", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uba54\ub274", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\uc815\ubcf4", None))
        self.toolBarMain.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

