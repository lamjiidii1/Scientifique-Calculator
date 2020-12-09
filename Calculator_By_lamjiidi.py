import sys
try:
    from PyQt5.QtWidgets import QApplication,QMainWindow
except:
    print("PyQt5 lib not installed !")
try:
    from UI import Ui_layoutMAIN
except:
    print("UI class not found !")
try:
    from tkinter import*
except:
    print("tkinter lib not installed !")
try:
    import math
except:
    print('Math lib not installed')
if __name__ == '__main__':
    calc_operator = ""
    text_input2 = []
    app= QApplication(sys.argv)
    w = QMainWindow()
    ui = Ui_layoutMAIN()
    ui.setupUi(w)
    def Scientific_OP():
            ui.second_power.setText('x\u00B2')
            ui.third_power.setText('x\u00B3')
            ui.nth_power.setText('x^n')
            ui.inv_power.setText('x\u207b\xb9')
            ui.tens_powers.setText('10^x')
            ui.square_root.setText('\u00B2\u221A')
            ui.third_root.setText('\u00B3\u221A')
            ui.nth_root.setText('\u221A')
            ui.log_base10.setText('log\u2081\u2080')
            ui.signs.setText('\u00B1')
            ui.abs_value.clicked.connect(lambda: button_click("abs("))
            ui.modulo.clicked.connect(lambda: button_click('%'))
            ui.int_div.clicked.connect(lambda: button_click('//'))
            ui.factorial_button.clicked.connect(lambda: fact_func())
            ui.eulers_num.clicked.connect(lambda: button_click(str(math.exp(1))))
            ui.sine.clicked.connect(lambda: button_click("math.sin("))
            ui.cosine.clicked.connect(lambda: button_click("math.cos("))
            ui.tangent.clicked.connect(lambda: button_click("math.tan("))
            ui.cotangent.clicked.connect(lambda: button_click("1/math.tan("))
            ui.pi_num.clicked.connect(lambda: button_click(str(math.pi)))
            ui.third_power.clicked.connect(lambda: button_click("**3"))
            ui.nth_power.clicked.connect(lambda: button_click("**"))
            ui.inv_power.clicked.connect(lambda: button_click("**(-1)"))
            ui.tens_powers.clicked.connect(lambda: button_click("10**"))
            ui.left_par.clicked.connect(lambda: button_click("("))
            ui.right_par.clicked.connect(lambda: button_click(")"))
            ui.signs.clicked.connect(lambda: sign_change())
            ui.percentage.clicked.connect(lambda: percent())
            ui.ex.clicked.connect(lambda: button_click("e("))
            ui.square_root.clicked.connect(lambda: square_root())
            ui.third_root.clicked.connect(lambda: third_root())
            ui.nth_root.clicked.connect(lambda: button_click("**(1/"))
            ui.log_base10.clicked.connect(lambda: button_click("log("))
            ui.log_basee.clicked.connect(lambda: button_click("ln("))
    Scientific_OP()
    ui.button_1.clicked.connect(lambda : button_click("1"))
    ui.button_2.clicked.connect(lambda: button_click("2"))
    ui.button_3.clicked.connect(lambda: button_click("3"))
    ui.button_4.clicked.connect(lambda: button_click("4"))
    ui.button_5.clicked.connect(lambda: button_click("5"))
    ui.button_6.clicked.connect(lambda: button_click("6"))
    ui.button_7.clicked.connect(lambda: button_click("7"))
    ui.button_8.clicked.connect(lambda: button_click("8"))
    ui.button_9.clicked.connect(lambda: button_click("9"))
    ui.button_0.clicked.connect(lambda: button_click("0"))
    ui.add.clicked.connect(lambda: button_click("+"))
    ui.sub.clicked.connect(lambda: button_click("-"))
    ui.div.clicked.connect(lambda: button_click("/"))
    ui.mul.clicked.connect(lambda: button_click("*"))
    ui.point.clicked.connect(lambda: button_click("."))
    ui.exp.clicked.connect(lambda: button_click(E))
    ui.equal.clicked.connect(lambda: button_equal())
    ui.delete_all.clicked.connect(lambda :button_clear_all())
    ui.delete_one.clicked.connect(lambda : button_delete())
    w.show()
    def text_input():
        h=text_input2
        for ele in text_input2:
            h +=ele
        return h
    def labelRe(value):
            t=""
            for ele in value:
                t += ele
            t = t.replace('math.sin(','sin(').replace('math.tan(','tan(').replace('math.cos(','cos(').replace('1/tan(','cot(')
            t = t.replace('/', '÷')
            t = t.replace('3.141592653589793','π')
            t = t.replace("**2",'\u00B2').replace('**3','\u00B3')
            t = t.replace("**",'^')
            ui.text_display.setText(t.replace("*10**", "E").replace('*', '×'))
    def button_click(char):
        global calc_operator
        calc_operator += str(char)
        text_input2.clear()
        text_input2.append(calc_operator)
        labelRe(text_input2)
    def button_clear_all():
        global calc_operator
        calc_operator = ""
        text_input2.clear()
        labelRe(text_input2)
    def button_delete():
        global calc_operator
        text = calc_operator[:-1]
        calc_operator = text
        text_input2.clear()
        text_input2.append(calc_operator)
        labelRe(calc_operator)
    def factorial(n):
        try:
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        except:
            labelRe("Oops!")
    def fact_func():
        try:
            global calc_operator
            result = str(factorial(int(calc_operator)))
            calc_operator = result
            text_input2.clear()
            text_input2.append(result)
            labelRe(result)
        except:
            labelRe("Bad expression")
    def trig_sin():
        try:
            global calc_operator
            result = str(math.sin(math.radians(int(calc_operator))))
            calc_operator = result
            text_input2.clear()
            text_input2.append(result)
            labelRe(text_input2)
        except:
            labelRe("Bad expression")
    def trig_cos():
        try:
            global calc_operator
            result = str(math.cos(math.radians(int(calc_operator))))
            calc_operator = result
            text_input2.clear()
            text_input2.append(result)
            labelRe(text_input2)
        except:
            labelRe("Bad expression")
    def trig_tan():
        try:
            global calc_operator
            result = str(math.tan(math.radians(int(calc_operator))))
            calc_operator = result
            text_input2.clear()
            text_input2.append(result)
            labelRe(text_input2)
        except:
            labelRe("Bad expression")
    def trig_cot():
        try:
            global calc_operator
            result = str(1 / math.tan(math.radians(int(calc_operator))))
            calc_operator = result
            text_input2.clear()
            text_input2.append(result)
            labelRe(text_input2)
        except:
            labelRe("Bad expression")
    def square_root():
        try:
            global calc_operator
            temp = str(eval(calc_operator + '**(1/2)'))
            calc_operator = temp
            text_input2.clear()
            text_input2.append(temp)
            labelRe(text_input2)
        except:
            labelRe("Bad expression")
    def third_root():
        try:
            global calc_operator
            temp = str(eval(calc_operator + '**(1/3)'))
            calc_operator = temp
            text_input2.clear()
            text_input2.append(temp)
            labelRe(text_input2)
        except:
            labelRe("Bad expression")
    def sign_change():
        try:
            global calc_operator
            if calc_operator[0] == '-':
                temp = calc_operator[1:]
            else:
                temp = '-' + calc_operator
            calc_operator = temp
            text_input2.clear()
            text_input2.append(temp)
            labelRe(text_input2)
        except:
            labelRe("Bad expression")
    def percent():
        try:
            global calc_operator
            temp = str(eval(calc_operator + '/100'))
            calc_operator = temp
            text_input2.clear()
            text_input2.append(temp)
            labelRe(text_input2)
        except:
            labelRe("Bad expression")
    def button_equal():
        if text_input2==[]:
            text_input2.clear()
            labelRe(text_input2)
        else:
            global calc_operator
            try:
                temp_op = str(eval(calc_operator))
                text_input2.clear()
                text_input2.append(temp_op)
                labelRe(text_input2)
                calc_operator = temp_op
            except:
                labelRe("Bad expression")
    sys.exit(app.exec_())
