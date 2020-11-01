#pip3 install tika reportlab PyQt5
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from tika import parser

# 출처: https: // swgurus.tistory.com/79 [In Quest for Gurus]
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QDialog, QHeaderView
from PyQt5.QtGui import QPdfWriter, QPagedPaintDevice, QPainter, QScreen, QPixmap
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import sys

from tika.parser import from_file

# c = canvas.Canvas("/Users/pechezi/Downloads/sample.pdf")

rowNum = 10
colNum = 1
path = "/Users/pechezi/Desktop/data.pdf"

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        # 테이블 생성
        self.table = QTableWidget(self)
        self.table.setRowCount(rowNum)
        self.table.setColumnCount(colNum)
        col = ["Message"]
        self.table.setHorizontalHeaderLabels(col)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.table.setItem(0, 0, QTableWidgetItem(str("Hello, World")))
        self.table.setItem(1, 0, QTableWidgetItem(str("안녕하세요. 김대환님")))
        # 버튼 생성
        self.btn = QPushButton('Print PDF File', self)
        self.btn.clicked.connect(self.btnClick)

        self.btn2 = QPushButton('Make PDF file', self)
        self.btn2.clicked.connect(self.btnClick2)

        self.btn3 = QPushButton('Load PDF file', self)
        self.btn3.clicked.connect(self.btnClick3)

        # 컨트롤들 박스 레이아웃 배치
        vbox.addWidget(self.table)
        vbox.addWidget(self.btn)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        self.setLayout(vbox)
        self.resize(600, 400)


    def btnClick(self):
        # 프린터 생성, 실행
        printer = QPrinter()
        dlg = QPrintDialog(printer, self)
        if dlg.exec() == QDialog.Accepted:
            # Painter 생성
            qp = QPainter()
            qp.begin(printer)

            # 여백 비율
            wgap = printer.pageRect().width()*0.1
            hgap = printer.pageRect().height()*0.1

            # 화면 중앙에 위젯 배치
            xscale = (printer.pageRect().width()-wgap)/self.table.width()
            yscale = (printer.pageRect().height()-hgap)/self.table.height()
            scale = xscale if xscale < yscale else yscale
            qp.translate(printer.paperRect().x() + printer.pageRect().width()/2,
                            printer.paperRect().y() + printer.pageRect().height()/2)
            qp.scale(scale, scale)
            qp.translate(-self.table.width()/2, -self.table.height()/2)

            # 인쇄
            self.table.render(qp)

            qp.end()

    def btnClick2(self):
        # pdf 생성
        pdfmetrics.registerFont(TTFont("HCR Batang", "HANBatang-LVT.ttf"))
        c = canvas.Canvas(path)
        c.setFont("HCR Batang", 16)
        c.setTitle("소재환 데이터")
        # c.drawString(100, 750, "Hellow,world!")
        for i in range(rowNum):
            try:
                text = self.table.item(i, 0).text()
                c.drawString(100, 780-30*i, text)
                pass
            except :
                pass

        c.save()

    def btnClick3(self):
        """
        PDF Loading Button
        """
        # try:
        print(path)
        with open(path, 'rb') as f:
            
            
            parsed = parser.from_file(path)
            text = parsed["content"]
            text = text.strip()
            text = text.split("\n")
            text = list(filter(None,text))
            print(len(text))
            for i in range(len(text)):
                self.table.setItem(i,0,QTableWidgetItem(str(text[i])))
            print(text)
            # print(parsed["content"])
            # get the first page
            # page = pdf.getPage(1)
            # print(page)
            # print('Page type: {}'.format(str(type(page))))
            # text = page.extractText()
            # print(text)
        # except:
            # print("There is no data.")
            

    
    # pdf = QPdfWriter('hello.pdf')
    # pdf.setPageSize(QPagedPaintDevice.A4)

    # # 화면 캡쳐
    # screen = QApplication.primaryScreen()
    # img = screen.grabWindow(self.winId(), 0, 0, self.rect().width(), self.rect().height())

    # # 3항 연산자 (a if test else b, 만약 test가 참이면 a, 아니면 b)
    # # 이미지 크기는 큰 값 기준, PDF 크기는 작은값 기준(화면 초과 방지)
    # img_size = img.width() if img.width()-img.height() > 0 else img.height()
    # pdf_size = pdf.width() if pdf.width()-pdf.height() < 0 else pdf.height()

    # # 최적 비율 얻기
    # ratio = pdf_size / img_size

    # # pdf에 쓰기
    # qp = QPainter()
    # qp.begin(pdf)
    # qp.drawPixmap(0, 0, img.width()*ratio, img.height()*ratio, img)
    # qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    print(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())
