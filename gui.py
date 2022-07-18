from PyQt5 import QtWidgets
import sys, converter

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.is_darkmode = False

        self.available_currencies = ['USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL']
        self.dark_theme = "/** QSS Qt Stylesheets Collection.* Created in 2013 by Khromathyon Software.* QSS Theme: Visual Studio(R) 2012 Dark Theme.* License: WTFPL*/QMainWindow {  background-color:#2d2d30;  color:#f1f1f1;}QMenuBar {  background-color:#2d2d30;  text-transform: uppercase;  color:#f1f1f1;}QMenuBar::item:selected{  background-color:#3e3e40;}QMenu {  border:0.5px solid #333337;  color:#f1f1f1;}QMenu::item:selected {  background-color:#2d2d30;  border-color:#333337;}QMenu::item {  background-color:#1b1b1c;  border-color:#333337;       padding: 2px 25px 2px 20px;}QMenu::separator{  background-color:#333337;  spacing:2px;}QTabBar::tab {  background-color:#2d2d30;  border: 1px solid transparent;  color:#f1f1f1;  padding:5px;}QTabBar::tab:hover{  background-color:#1c97ea;}QTabBar::tab:selected{  background-color:#007acc;}QTabWidget::pane {  border-top: 2px solid #007acc;  background-color:#2d2d30;}QDockWidget {    background: #2d2d30;    color:#f1f1f1;}QDockWidget::active {  border: 1px solid #007acc;}QDockWidget::title {  color:#f1f1f1;  background:#007acc;}QComboBox {  border-style:none;  background-color:#333337;  color:#b2b2b2;  border-style:none;}QComboBox:on {  background-color:#3f3f46;}QComboBox:down-arrow {  border-style:none;  border-left: 1px solid #007acc;}QComboBox:drop-down {  border-style:none;}/*Needs fix*/QScrollBar{  background:#3e3e42;  border-style:none;}QScrollbar::horizontal{     height: 15px;     margin: 0px 20px 0 20px;}QScrollBar:handle {  border-style:none;  background:#9d9d9d;  margin: inherited;}QPushButton {  border-style:none;  border-bottom:1px solid #007acc;  color:#f1f1f1;  background:#3e3e42;  padding:5px;}QPushButton::pressed {  border: 1px solid #007acc;  background:#3e3e42;}QToolButton {  border-style:none;  background:#2d2d30;  color:#f1f1f1;}QToolButton:pressed {  border: 1px solid #007acc;  background:#3e3e42;}QLabel {  color:#f1f1f1;}QLineEdit {  border: 1px solid #3e3e42;  background-color:#3f3f46;  color:#b2b2b2;  selection-background-color:#1c97ea;}QLineEdit:selected {  border-color:#007acc;}QToolBar {  background:#2d2d30;  border-style:none;}QToolBox{  background:#2d2d30;}QToolBox::tab{  background:#2d2d30;  color:#f1f1f1;  border-style:none;  border-bottom-style: solid;  border-bottom: 2px solid #007acc;}QToolBox::tab:selected {  border:1px solid #007acc;}QWidget{  background:#2d2d30;  color:#f1f1f1;}QTreeView {  background-color:#2d2d30;  border-style:none;}QTreeView::item:selected{  background:#007acc;}QTreeView::item:selected!active {  background: #3f3f46;}QTreeView::item:selected {  background: #3f3f46;}QListView {  background-color:#252526;  border-style:none;}"

        self.setGeometry(200,200,330,280)
        self.setWindowTitle("Duties And Taxes Calculator")
        self.setStyleSheet("")
        self.initUI()

    def switch_color_mode(self):
        if self.is_darkmode:
            self.setStyleSheet("")
            self.darkmode_checkmark.setText("Dark Mode")
            self.is_darkmode = False
        else:
            self.setStyleSheet(self.dark_theme)
            self.darkmode_checkmark.setText("Light Mode")
            self.is_darkmode = True

    def initUI(self):
        
        # Dark Mode Toggle

        self.darkmode_checkmark = QtWidgets.QPushButton(self)
        self.darkmode_checkmark.setGeometry(240,10,80,30)
        self.darkmode_checkmark.setText("Dark Mode")
        self.darkmode_checkmark.clicked.connect(self.switch_color_mode)

        # Amount Input

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Amount")
        self.label.setGeometry(10,10,90,30)

        self.coords_input = QtWidgets.QTextEdit(self)
        self.coords_input.setGeometry(10,50,310,30)

        # Currency Input

        self.convert_checkmark = QtWidgets.QCheckBox(self)
        self.convert_checkmark.setGeometry(10,90,120,30)
        self.convert_checkmark.setText("Convert Currencies")

        # Currency Selection

        self.from_currency_combo_box = QtWidgets.QComboBox(self)
        self.from_currency_combo_box.setGeometry(10,130,150,20)

        self.to_currency_combo_box = QtWidgets.QComboBox(self)
        self.to_currency_combo_box.setGeometry(180,130,140,20)

        for currency in self.available_currencies:
            self.from_currency_combo_box.addItem(currency)
            self.to_currency_combo_box.addItem(currency)

        self.from_currency_combo_box.setCurrentText("From")
        self.to_currency_combo_box.setCurrentText("To")

        # Result Output

        self.result_text = QtWidgets.QTextBrowser(self)
        self.result_text.setGeometry(10,170,200,100)
        
        self.calc_button = QtWidgets.QPushButton(self)
        self.calc_button.setText("Calculate")
        self.calc_button.setGeometry(230,170,90,100)
        self.calc_button.clicked.connect(self.calculate_perspective)

    def parse_inputs(self):
        coords = "<" + self.coords_input.toPlainText() + ">"
        origin = ""
        ratio = ""
        scale = 1

        if self.origin_checkmark.isChecked():
            try:
                origin = int(self.origin_input.toPlainText())
            except ValueError:
                origin = ""

        if self.ratio_checkmark.isChecked():
            try:
                ratio = int(self.ratio_input.toPlainText())
            except ValueError:
                ratio = ""

        if self.scale_checkmark.isChecked():
            try:
                scale = int(self.scale_input.toPlainText())
            except ValueError:
                scale = 1
        
        return {
            "coord" : coords,
            "origin" : origin,
            "ratio" : ratio,
            "scale" : scale
        }


    def calculate_perspective(self):
        self.result_text.setText(perspective.get_perspective(self.parse_inputs()))
        self.update()

    def update(self):
        self.label.adjustSize()

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()
