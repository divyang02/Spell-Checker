from tkinter import *
class MyWindow:
    def __init__(self):
        self.win = Tk()
        self.win.geometry('1200x500')
        self.win.title('English Dictionary')
        
        self.d = {}
        self.load_data()
        self.lbl1=Label(self.win, text='ENTER WORD')
        self.lbl3=Label(self.win, text='Result')
        self.t1=Entry(bd=3)
        self.t3=Entry(width=100)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1=Button(self.win, text='SEARCH', command=self.add)
        self.b1.place(x=100, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        
        self.win.mainloop()
    
    def add(self):
        self.t3.delete(0, 'end')
        word= self.t1.get()
        result = self.find(word)
        if type(result) == list :
            result = "Did you mean : " + str(result)
        self.t3.insert(END, str(result))
    
    def load_data(self) :

        with open("dictionary.txt") as f:
            for line in f:
                if line == '\n' or line == '' or line == ' ':
                    continue
                if len(line) <= 3 :
                    continue
                words = line.split()
                key, val = words[0], words[1:]
                self.d[key.lower()] = " ".join(val)
    
    def calculate_distance(self, s1: str, s2: str):
        n1 = len(s1)
        n2 = len(s2)

        row = n1 + 1
        col = n2 + 1

        dp_array = [[0] * col for i in range(row)]

        for i in range(row):
            for j in range(col):

                if i == 0:
                    dp_array[i][j] = j
                    continue

                if j == 0:
                    dp_array[i][j] = i
                    continue

                if s1[i - 1] != s2[j - 1]:
                    dp_array[i][j] = min(dp_array[i - 1][j], dp_array[i][j - 1], dp_array[i - 1][j - 1]) + 1

                else:
                    dp_array[i][j] = dp_array[i - 1][j - 1]

        return dp_array[row - 1][col - 1]
    
    def find(self, s) :
        s = s.lower()
        if s in self.d :
            return self.d[s]
        else :
            ret = []
            m1 = 9999
            m2 = 9999
            m3 = 9999
            s1 = ""; s1 = ""; s3 = ""
            for key in self.d.keys() :
                dist = self.calculate_distance(key, s)
                if dist < m1 :
                    m1 = dist
                    s1 = key
                elif m1 <= dist < m2 :
                    m2 = dist
                    s2 = key
                elif m2 <= dist < m3 :
                    m3 = dist
                    s3 = key
            ret = [s1, s2, s3]
            return ret

app = MyWindow()