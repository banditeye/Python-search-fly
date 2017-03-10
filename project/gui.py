# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from aaa import Postesky
import sys
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QFrame):
    reload(sys)    # to re-enable sys.setdefaultencoding()
 
    
    def __init__(self):
        QtGui.QFrame.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(365, 235)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(9, 35, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 9, 36, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(9, 61, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(127, 61, 16, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.dateEdit_2 = QtGui.QDateEdit(Form)
        self.dateEdit_2.setGeometry(QtCore.QRect(244, 146, 83, 20))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        actualdate=datetime.datetime.now()
        self.dateEdit_2.setDate(actualdate)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(244, 9, 69, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem('Berlin, Schonefeld, Niemcy (SXF)')
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(244, 35, 69, 20))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem('Warszawa - dowolne lotnisko (WAWA)')
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(127, 145, 16, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.dateEdit = QtGui.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(244, 90, 83, 20))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.dateEdit.setDate(actualdate)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(244, 203, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.szukaj)
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "Przylot z", None))
        self.label.setText(_translate("Form", "Wylot z", None))
        self.label_3.setText(_translate("Form", "Termin", None))
        self.label_4.setText(_translate("Form", "Od", None))
        self.label_5.setText(_translate("Form", "Do", None))
        self.pushButton.setText(_translate("Form", "Szukaj", None))
    
    """ilosc dni po odjeciu dwoch dat"""
    def iloscdni(self):
        day1=self.dateEdit.date().day()
        month1=self.dateEdit.date().month()
        year1=self.dateEdit.date().year()

        day2=self.dateEdit_2.date().day()
        month2=self.dateEdit_2.date().month()
        year2=self.dateEdit_2.date().year()
        
        
    
    
  
      
    def szukaj(self):
        

        from aaa import Connectdb
        b=Connectdb.Connectdb()
        a=Postesky.Postesky()

       
        """uruchomienie selenium"""
        a.driver()
        """ilosc polaczen pomiedzy lotniskami dostepnymi w bazie danych"""
        b.create_connection()
        licznik=b.countairport()+1
        print licznik
        b.closeconnection()

        k=0
        i=36

        """ustawienie polaczenia w jedna strone"""
        a.onewayticket()

        """petla od 1 lotniska do ostatniego jako licznik"""
        for i in range(1,licznik):
            
          while(True):  
            try:
                 """polaczenie z baza danych"""
                 b.create_connection() 
                 """pobranie z bazy danych lotnisk"""            
                 pierwsze_lotnisko=b.selectairportone(i)
                 drugie_lotnisko=b.selectairporttwo(i)
                 
                 b.closeconnection()

                 a.oczekujnalotniskodeparture()
                 a.selectcountryone(pierwsze_lotnisko)
                 a.selectcountrytwo(drugie_lotnisko)
                


                 day=self.dateEdit.date().day()
                 month=self.dateEdit.date().month()
                 year=self.dateEdit.date().year()


                 yearccc=year
                 monthccc=month
                 break
            except Exception:
                continue
                     
                     
          for i in range(25):
                 
                    count_day_of_month=datetime.date (year, month, 1) - datetime.timedelta (days = 1)
                    ccc=int(count_day_of_month.day)   
                    print 'dana cccc',ccc   
                    a.oczekujnakalendarz()
                    """jesli ilosc dni miesiaca jest rowna ilosc dni aktualnego miesiaca i jest to pierwsze wejsce"""
                    if ccc>=day and i<1:
                            """jesli pierwszy raz wchodzimy to zmieniamy miesiac"""
                            if k<1:
                                try:
                                    a.calendarone(day,month,year,0) 
                                    day=day+1
                                    """jesli nie to zmieniamy tylko dzien"""
                                except Exception:
                                    a.calendarone(day,month,year,0) 
                                    day=day+1
                            else:
                                try:
                                    a.calendarone(day,month,year,2) 
                                    day=day+1
                                except Exception:
                                    a.calendarone(day,month,year,2) 
                                    day=day+1
                    elif ccc>=day:
                            try:
                                a.calendarone(day,month,year,2) 
                                day=day+1
                            except Exception:
                                a.calendarone(day,month,year,2) 
                                day=day+1
                    else:
                            try:
                                month=month+1
                                day=1
                                a.calendarone(day,month,year,1) 
                                day=day+1
                            except Exception:
                                month=month+1
                                day=1
                                a.calendarone(day,month,year,1) 
                                day=day+1


                    try:
                        a.zatwierdz()
                    except Exception:
                        a.zatwierdz()
                        
                    try:
                        a.delay()
                    except Exception:
                        a.back()

                    a.back()
          """ drugie wejscie do daty"""
          k=k+1
               
        
               
        
        
        
        
       



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Ui_Form()
    myapp.show()
    sys.exit(app.exec_())