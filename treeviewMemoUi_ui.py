# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'treeviewMemoUi.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSplitter, QStatusBar,
    QTextEdit, QToolBar, QTreeWidget, QTreeWidgetItem,
    QWidget)
import iconResources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(901, 645)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionOpenFolder = QAction(MainWindow)
        self.actionOpenFolder.setObjectName(u"actionOpenFolder")
        icon = QIcon()
        icon.addFile(u":/icon/icons/folderclosed1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpenFolder.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/floppy-disk-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionReadMode = QAction(MainWindow)
        self.actionReadMode.setObjectName(u"actionReadMode")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/address-book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionReadMode.setIcon(icon2)
        self.actionEditMode = QAction(MainWindow)
        self.actionEditMode.setObjectName(u"actionEditMode")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/note-edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEditMode.setIcon(icon3)
        self.actionAddImage = QAction(MainWindow)
        self.actionAddImage.setObjectName(u"actionAddImage")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/img-landscape-add2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddImage.setIcon(icon4)
        self.actionTooBarOnOff = QAction(MainWindow)
        self.actionTooBarOnOff.setObjectName(u"actionTooBarOnOff")
        self.actionTooBarOnOff.setCheckable(True)
        self.actionTooBarOnOff.setChecked(True)
        self.actionAddRootFolder = QAction(MainWindow)
        self.actionAddRootFolder.setObjectName(u"actionAddRootFolder")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icons/folder-new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddRootFolder.setIcon(icon5)
        self.actionAddNewDoc = QAction(MainWindow)
        self.actionAddNewDoc.setObjectName(u"actionAddNewDoc")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icons/document-new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddNewDoc.setIcon(icon6)
        self.actionRefreshTree = QAction(MainWindow)
        self.actionRefreshTree.setObjectName(u"actionRefreshTree")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icons/clockwise-arrow1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRefreshTree.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(11, 11, 881, 541))
        self.splitter.setOrientation(Qt.Horizontal)
        self.treeWidget = QTreeWidget(self.splitter)
        self.treeWidget.headerItem().setText(0, "")
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy1)
        self.treeWidget.setMinimumSize(QSize(20, 0))
        self.splitter.addWidget(self.treeWidget)
        self.textEdit = QTextEdit(self.splitter)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit.setMinimumSize(QSize(20, 0))
        self.splitter.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 901, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDocument = QMenu(self.menubar)
        self.menuDocument.setObjectName(u"menuDocument")
        self.menuTool = QMenu(self.menubar)
        self.menuTool.setObjectName(u"menuTool")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuDocument.menuAction())
        self.menuFile.addAction(self.actionAddRootFolder)
        self.menuFile.addAction(self.actionOpenFolder)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionRefreshTree)
        self.menuDocument.addAction(self.actionTooBarOnOff)
        self.menuTool.addAction(self.actionReadMode)
        self.menuTool.addAction(self.actionEditMode)
        self.menuTool.addAction(self.actionAddImage)
        self.toolBar.addAction(self.actionAddRootFolder)
        self.toolBar.addAction(self.actionOpenFolder)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionAddNewDoc)
        self.toolBar.addAction(self.actionRefreshTree)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionReadMode)
        self.toolBar.addAction(self.actionEditMode)
        self.toolBar.addAction(self.actionAddImage)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpenFolder.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc5f4\uae30", None))
#if QT_CONFIG(tooltip)
        self.actionOpenFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\ucee8\ud150\uce20\ub4e4\uc774 \ud3ec\ud568\ub41c \ud3f4\ub354\ub97c \uc5fd\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionOpenFolder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc804\uccb4 \uc800\uc7a5", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \ub0b4 \ubaa8\ub4e0 \ub0b4\uc6a9\uc744 \uc800\uc7a5.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionReadMode.setText(QCoreApplication.translate("MainWindow", u"\uc77d\uae30 \ubaa8\ub4dc", None))
#if QT_CONFIG(tooltip)
        self.actionReadMode.setToolTip(QCoreApplication.translate("MainWindow", u"\uc77d\uae30 \ubaa8\ub4dc\ub85c \uc804\ud658 (\ud3b8\uc9d1 \ubd88\uac00)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionReadMode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionEditMode.setText(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9d1 \ubaa8\ub4dc", None))
#if QT_CONFIG(tooltip)
        self.actionEditMode.setToolTip(QCoreApplication.translate("MainWindow", u"\ud3b8\uc9d1 \ubaa8\ub4dc\ub85c \uc804\ud658\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionEditMode.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.actionAddImage.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ucca8\ubd80", None))
#if QT_CONFIG(tooltip)
        self.actionAddImage.setToolTip(QCoreApplication.translate("MainWindow", u"\ubb38\uc11c \ub0b4\uc5d0 \uc774\ubbf8\uc9c0\ub97c \ucca8\ubd80\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionAddImage.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionTooBarOnOff.setText(QCoreApplication.translate("MainWindow", u"\ub3c4\uad6c \ubaa8\uc74c \ucf1c\uae30/\ub044\uae30", None))
#if QT_CONFIG(tooltip)
        self.actionTooBarOnOff.setToolTip(QCoreApplication.translate("MainWindow", u"\ub3c4\uad6c \ubaa8\uc74c(toolbar)\uc744 \ud0a4\uac70\ub098 \ub055\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.actionAddRootFolder.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ub8e8\ud2b8 \ud3f4\ub354 \ucd94\uac00", None))
#if QT_CONFIG(tooltip)
        self.actionAddRootFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\uc0c8 \ub8e8\ud2b8 \ud3f4\ub354 \ucd94\uac00", None))
#endif // QT_CONFIG(tooltip)
        self.actionAddNewDoc.setText(QCoreApplication.translate("MainWindow", u"\uc0c8 \ubb38\uc11c", None))
#if QT_CONFIG(tooltip)
        self.actionAddNewDoc.setToolTip(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \ub0b4 \uc0c8 \ubb38\uc11c\ub97c \ucd94\uac00\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
        self.actionRefreshTree.setText(QCoreApplication.translate("MainWindow", u"\ud2b8\ub9ac \uc0c8\ub85c\uace0\uce68", None))
#if QT_CONFIG(tooltip)
        self.actionRefreshTree.setToolTip(QCoreApplication.translate("MainWindow", u"\ud2b8\ub9ac\ub97c \uc0c8\ub85c\uace0\uce68\ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionRefreshTree.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
        self.menuDocument.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uad6c", None))
        self.menuTool.setTitle(QCoreApplication.translate("MainWindow", u"\ubb38\uc11c", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

