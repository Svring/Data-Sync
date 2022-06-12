from tkinter import *
from tkinter import filedialog
import jieba
import re

#设定窗口
root = Tk()
root.title('词频统计')
root.geometry('900x600')

#设定四个框架
f1 = Frame(root, width=450, height=360)
f1.place(relx=0.0, rely=0.0)
f2 = Frame(root, width=450, height=360)
f2.place(relx=0.5, rely=0.0)
f3 = Frame(root, width=450, height=240)
f3.place(relx=0.0, rely=0.6)
f4 = Frame(root, width=450, height=240)
f4.place(relx=0.5, rely=0.6)

#---------------------------------------

#第一框架的组件

#按钮功能：选择文件
def f1_btn1():
    global sfname
    global content
    f1_text.delete('1.0', END)
    sfname = filedialog.askopenfilename(title='选择txt文件', filetypes=[('All Files', '*')])
    select_path.set(sfname)
    #文本内容写入文本框
    if sfname is not None:
        with open(file=sfname, mode='r+', encoding='utf-8') as file:
            content = file.read()
        f1_text.insert('insert', content)

#按钮功能：词频统计
def f1_btn2():
    f2_text1.delete('1.0', END)
    words = jieba.lcut(content)
    counts = {}
    for word in words:
        if len(word) == 1:     # 排除单个字符分词的影响
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    # 按词频从高到低排序
    counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    for i in range(10):
        word, count = counts[i]
        f2_text1.insert('insert', word + ' ' + str(count) + '\n')

#按钮功能：生成词云
def f1_btn3():
    pass

#初始化文件路径变量
select_path = StringVar()

#设定文件选择按钮
f1_btn1 = Button(f1, text='选择文件', relief=RIDGE, width=15, command=f1_btn1)
f1_btn1.grid(row=0, padx=10, pady=5, sticky=W)

#设定文件路径视窗
f1_entry = Entry(f1, textvariable = select_path, relief=RIDGE, width=40, border=3)
f1_entry.grid(row=0, padx=10, sticky=E)

#设定文本视窗
f1_text = Text(f1, relief=SOLID, width=60, height=21)
f1_text.grid(row=1, padx=10, pady=3, sticky=NSEW)

#设定词频统计按钮
f1_btn2 = Button(f1, text='词频统计', relief=RIDGE, width=10, command=f1_btn2)
f1_btn2.grid(row=3, padx=10, pady=5, sticky=W)

#设定生成词云按钮
f1_btn3 = Button(f1, text='生成词云', relief=RIDGE, width=10, command=f1_btn3)
f1_btn3.grid(row=3, padx=10, pady=5, sticky=E)

#---------------------------------------

#第二框架的组件

#按钮功能：保存结果
def f2_btn1():
    sfname = filedialog.asksaveasfilename(title=u'保存文件')
    content = f1_text.get('1.0', END)
    with open(file=sfname, mode='a+', encoding='utf-8') as file:
        file.truncate(0)
        file.write(content)
    f1_text.delete('1.0', END)

#按钮功能：删除词组
def f2_btn2():
    words = f2_text2.get('1.0', END).split(';')
    text = f1_text.get('1.0', END)
    for word in words:
        text = re.sub(word, '', text)
    f1_text.delete('1.0', END)
    f1_text.insert('insert', text)

#按钮功能：替换词组
def f2_btn3():
    words = f2_text3.get('1.0', END).split()
    print(words)
    text = f1_text.get('1.0', END)
    for word in words:
        pre, cur = word.split('-->')
        print(pre, cur)
        text = re.sub(pre, cur, text)
    f1_text.delete('1.0', END)
    f1_text.insert('insert', text)

#按钮功能：删去词组后重新统计
def f2_btn4():
    f2_text1.delete('1.0', END)
    words = jieba.lcut(f1_text.get('1.0', END))
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    # 按词频从高到低排序
    counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    for i in range(10):
        word, count = counts[i]
        f2_text1.insert('insert', word + ' ' + str(count) + '\n')

#按钮功能：生成统计图
def f2_btn5():
    pass

#按钮功能：替换词组后重新统计
def f2_btn6():
    f2_text1.delete('1.0', END)
    words = jieba.lcut(f1_text.get('1.0', END))
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    # 按词频从高到低排序
    counts = sorted(counts.items(), key = lambda x: x[1], reverse = True)
    for i in range(10):
        word, count = counts[i]
        f2_text1.insert('insert', word + ' ' + str(count) + '\n')

#标签:词频统计
f2_label1 = Label(f2, text='词频统计结果', width=15)
f2_label1.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

#按钮：保存结果
f2_btn1 = Button(f2, text='保存结果', command=f2_btn1, relief=RIDGE)
f2_btn1.grid(row=0, column=1, padx=10, pady=5)

#文本框：词频统计结果
f2_text1 = Text(f2, width=20, height=21, relief=SOLID)
f2_text1.grid(row=1, column=0, padx=10, pady=5, columnspan=2, rowspan=3, sticky=NSEW)

#标签：需要删除的词组
f2_label2 = Label(f2, text='需要删除的词组', width=30)
f2_label2.grid(row=0, column=2, padx=10, pady=5, sticky=NSEW)

#文本框：需要删除的词组
f2_text2 = Text(f2, relief=SOLID, width=30, height=10)
f2_text2.grid(row=1, column=2, padx=10, pady=5, sticky=N)

#按钮：删除词组
f2_btn2 = Button(f2, text='删除词组', command=f2_btn2, relief=RIDGE)
f2_btn2.grid(row=4, column=0)

#按钮：替换词组
f2_btn3 = Button(f2, text='替换词组', command=f2_btn3, relief=RIDGE)
f2_btn3.grid(row=4, column=1)

#按钮：重新统计
f2_btn4 = Button(f2, text='重新统计', command=f2_btn4, relief=RIDGE)
f2_btn4.grid(row=2, column=2, padx=10, sticky=(N, E))

#标签：需要替换的词组
f2_label3 = Label(f2, text='需要替换的词组', width=15)
f2_label3.grid(row=2, column=2, padx=10, sticky=(W, S))

#文本框：需要替换的词组
f2_text3 = Text(f2, width=30, height=5, relief=SOLID)
f2_text3.grid(row=3, column=2)

#按钮：生成统计图
f2_btn5 = Button(f2, text='生成统计图', command=f2_btn5, relief=RIDGE)
f2_btn5.grid(row=4, column=2, padx=10, sticky=W)

#按钮：重新统计
f2_btn6 = Button(f2, text='重新统计', command=f2_btn6, relief=RIDGE)
f2_btn6.grid(row=4, column=2, padx=10, sticky=E)

#---------------------------------------

root.mainloop()
