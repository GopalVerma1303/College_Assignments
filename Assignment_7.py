# 1.
import calendar
from tkinter import *


def findGst():
    org_cost = int(org_priceField.get())
    N_price = int(net_priceField.get())
    gst_rate = ((N_price - org_cost) * 100) / org_cost
    gst_rateField.insert(10, str(gst_rate) + " % ")


def clearAll():
    org_priceField.delete(0, END)
    net_priceField.delete(0, END)
    gst_rateField.delete(0, END)


if __name__ == "__main__":
    gui = Tk()
    gui.title("GST Rate Finder")
    gui.geometry("300x300")
    org_price = Label(gui, text="Original Price")
    net_price = Label(gui, text="Net Price")
    find = Button(gui, text="Find", command=findGst)
    gst_rate = Label(gui, text="GST Rate")
    clear = Button(gui, text="Clear", command=clearAll)
    org_price.grid(row=1, column=1, padx=10, pady=10)
    net_price.grid(row=2, column=1, padx=10, pady=10)
    find.grid(row=3, column=2, padx=10, pady=10)
    gst_rate.grid(row=4, column=1, padx=10, pady=10)
    clear.grid(row=5, column=2, padx=10, pady=10)
    org_priceField = Entry(gui)
    net_priceField = Entry(gui)
    gst_rateField = Entry(gui)
    org_priceField.grid(row=1, column=2, padx=10, pady=10)
    net_priceField.grid(row=2, column=2, padx=10, pady=10)
    gst_rateField.grid(row=4, column=2, padx=10, pady=10)
    gui.mainloop()


# 2.


def showCal():
    new_gui = Tk()
    new_gui.config(background="white")
    new_gui.title("CALENDAR")
    new_gui.geometry("550x600")
    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(new_gui, text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    new_gui.mainloop()


if __name__ == "__main__":
    gui = Tk()
    gui.title("CALENDAR")
    gui.geometry("220x150")
    cal = Label(gui, text="CALENDAR",
                font=("times", 28, 'bold'))
    year = Label(gui, text="Enter Year")
    year_field = Entry(gui)
    Show = Button(gui, text="Show Calendar",
                  command=showCal)
    Exit = Button(gui, text="Exit", command=exit)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    Show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
    gui.mainloop()


# 3.


win = Tk()
win.geometry("312x324")
win.resizable(0, 0)
win.title("Calculator")


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def bt_clear():
    global expression
    expression = ""
    input_text.set("")


def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""
input_text = StringVar()
input_frame = Frame(win, width=312, height=50, bd=0,
                    highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)
input_field = Entry(input_frame, font=('arial', 18, 'bold'),
                    textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)

input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()
clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee",
               cursor="hand2", command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                cursor="hand2", command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
               cursor="hand2", command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
               cursor="hand2", command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
              cursor="hand2", command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                  cursor="hand2", command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
              cursor="hand2", command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
              cursor="hand2", command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
             cursor="hand2", command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
               cursor="hand2", command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
             cursor="hand2", command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
             cursor="hand2", command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
               cursor="hand2", command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
              cursor="hand2", command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)
zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
              command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
               cursor="hand2", command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
                cursor="hand2", command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)
win.mainloop()


# 4.


def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums)
    return nums


example = list(input())
print(quicksort(0, len(example)-1, example))


# 5.


def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums)
    return nums


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


example = []
size = int(input())
for i in range(size):
    tmp = int(input())
    example.append(tmp)
print(quicksort(0, len(example)-1, example))
target = int(input())
print(binary_search(example, 0, len(example), target))
no_of_times = 0
for i in example:
    if(i == target):
        no_of_times += 1
print(no_of_times)


# 6.


def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def bubble(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            return


example = []
size = int(input())
for i in range(size):
    tmp = int(input())
    example.append(tmp)
print(remove(example))
bubble(remove(example))
