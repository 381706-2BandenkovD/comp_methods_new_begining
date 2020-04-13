import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

#This is FitzHugh Nagumo model
#function for X
def fx(u, v, Ie):
    return float(u - u * u * u / 3. - v + Ie)
#function for Y
def fy(u, v, a, b, T):
    return float((u + a - b * v) / T)

#runge kutta 4th order
def Runge_Kutt(x0,y0,n,h):
    x.append(x0)
    y.append(y0)
    t0 = 0.
    i = 0
    yt = 0
    xt = 0
    while(t0 < n):
        k1_y = h * fy(x[i], y[i], a, b, T)
        kx = x[i] + h / 2
        y1 = y[i] + k1_y / 2
        k2_y = h * fy(kx, y1, a, b, T)
        y1 = y[i] + k2_y / 2
        k3_y = h * fy(kx, y1, a, b, T)
        kx = kx + h / 2
        y1 = y[i] + k3_y
        k4_y = h * fy(kx, y1, a, b, T)
        yt = y[i] + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
        y.append(yt)

        k1_x = h * fx(x[i], y[i], Ie)
        kx = x[i] + h / 2
        y1 = y[i] + k1_x / 2
        k2_x = h * fx(kx, y1, Ie)
        y1 = y[i] + k2_x / 2
        k3_x = h * fx(kx, y1, Ie)
        kx = kx + h / 2
        y1 = y[i] + k3_x
        k4_x = h * fx(kx, y1, Ie)
        xt = x[i] + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) / 6
        x.append(xt)
        t0+=h
        i+=1

#draw graph_axes
def addGraphPhase(graph_axes, x, y):
     graph_axes.plot(x, y)
     plt.draw()

if __name__ == '__main__':
    x = list()
    y = list()

    #Event handler for the Add button
    def onButtonAddClicked(event):
        global graph_axes, x, y
        global x0, y0, n, h, a, b, Ie, T
        Runge_Kutt(x0,y0,n,h)
        addGraphPhase(graph_axes, x, y)
        x = []
        y = []

    #Event handler for the Clear button
    def onButtonClearClicked(event):
        global graph_axes
        graph_axes.clear()
        graph_axes.grid()
        plt.draw()

    #Event handler for entering text (may be finish it)
    def submitA(text):
        global a
        try:
            a = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            print("Для параметра 'a' были использованы значения по умолчанию = ", a)
            

    def submitH(text):
        global h
        try:
            h = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            print("Для шага 'h' были использованы значения по умолчанию = ", h)

    def submitX0(text):
        global x0
        try:
            x0 = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            print("Для начального 'x0' были использованы значения по умолчанию = ", x0)

    def submitY0(text):
        global y0
        try:
            y0 = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            print("Для начального 'y0' были использованы значения по умолчанию = ", y0)

    def submitN(text):
        global n
        try:
            n = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            print("Для колличества точек 'n' были использованы значения по умолчанию = ", n)

    def submitB(text):
        global b
        try:
            b = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            print("Для параметра 'b' были использованы значения по умолчанию = ", b)

    def submitIe(text):
        global Ie
        try:
            Ie = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            print("Для параметра 'a' были использованы значения по умолчанию = ", Ie)

    def submitT(text):
        global T
        try:
            T = float(text)
        except ValueError:
            print("Вы пытаетесь ввести не число")
            print("Для параметра 'T' были использованы значения по умолчанию = ", T)

    #Create graph
    fig, graph_axes = plt.subplots()
    graph_axes.grid()
    fig.subplots_adjust(left=0.07, right=0.95, top=0.95, bottom=0.4)

    #Create add button
    axes_button_add = plt.axes([0.55, 0.05, 0.4, 0.075])
    button_add = Button(axes_button_add, 'Добавить')
    button_add.on_clicked(onButtonAddClicked)

    #Create clear buttin
    axes_button_clear = plt.axes([0.05, 0.05, 0.4, 0.075])
    button_clear = Button(axes_button_clear, 'Очистить')
    button_clear.on_clicked(onButtonClearClicked)

    #Create textbox for h, n, x0, y0, a, b, T,
    axbox = plt.axes([0.12, 0.25, 0.12, 0.075])
    h_box = TextBox(axbox, 'Шаг h =', initial="0.01")
    h = 0.01
    h_box.on_submit(submitH)

    axbox = plt.axes([0.37, 0.25, 0.12, 0.075])
    x0_box = TextBox(axbox, 'Задача   \nКоши x0 =', initial="1")
    x0 = 1.0
    x0_box.on_submit(submitX0)

    axbox = plt.axes([0.56, 0.25, 0.12, 0.075])
    y0_box = TextBox(axbox, 'y0 =', initial= "0.1")
    y0 = 0.1
    y0_box.on_submit(submitY0)

    axbox = plt.axes([0.83, 0.25, 0.12, 0.075])
    n_box = TextBox(axbox, 'Количество\n точек n =', initial="100")
    n = 100.0
    n_box.on_submit(submitN)

    axbox = plt.axes([0.16, 0.15, 0.12, 0.075])
    a_box = TextBox(axbox, 'Параметры \n a =', initial= "0.7")
    a = 0.7
    a_box.on_submit(submitA)

    axbox = plt.axes([0.37, 0.15, 0.12, 0.075])
    b_box = TextBox(axbox, 'b =', initial= "0.8")
    b = 0.8
    b_box.on_submit(submitB)

    axbox = plt.axes([0.56, 0.15, 0.12, 0.075])
    Ie_box = TextBox(axbox, 'Ie =', initial= "0.5")
    Ie = 0.5
    Ie_box.on_submit(submitIe)

    axbox = plt.axes([0.83, 0.15, 0.12, 0.075])
    T_box = TextBox(axbox, 'T =', initial= "12.5")
    T = 12.5
    T_box.on_submit(submitT)

    plt.show()


