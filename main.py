from tkinter import *
import time 
import heapq as hq
import re
from Trie import TrieNode
from search_utils import *

class MyWindow:
    def __init__(self):
        self.win = Tk()
        self.win.geometry('1500x500')
        
        self.result = None
        self.trie = TrieNode()
        self.d = {}
        self.popped = []
        self.curr_text = ""
        
        self.load_data()
        self.lbl1=Label(self.win, text='ENTER WORD')
        self.lbl3=Label(self.win, text='Result')
        self.t1=Entry(bd=3)
        self.t3=Entry(width=100)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1=Button(self.win, text='SEARCH', command=self.search)
        self.b1.place(x=100, y=150)
        self.b2 = Button(self.win, text='Next suggestion', command=self.next_sugg)
        self.b2.place(x=100, y=350)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
        
        self.win.mainloop()
    
    def search(self):
        self.t3.delete(0, 'end')
        word= self.t1.get()
        self.curr_text = word
        self.result = self.find(word)
        tmp = ""
        if type(self.result) == list :
            for i in range(3) :
                pop = hq.heappop(self.result)
                self.popped.append(pop)
                tmp = tmp + pop[1] + " "
            tmp = "Did you mean : " + tmp
        else :
            tmp = self.result
        self.t3.insert(END, tmp)
    
    def next_sugg(self) :
        tmp = ""
        
        self.t3.delete(0, 'end')
        if self.t1.get() != self.curr_text :
            self.t3.insert(END, "press search first....!!!!")
        else :
            if len(self.result) < 3 :
                self.result = hq.heapify(self.popped)
                self.popped = []
            for i in range(3) :
                pop = hq.heappop(self.result)
                self.popped.append(pop)
                tmp = tmp + pop[1] + " "
            tmp = "Did you mean : " + tmp
            self.t3.insert(END, tmp)    
        
    
    def load_data(self) :

        with open("dictionary.txt") as f:
            for line in f:
                if line == '\n' or line == '' or line == ' ':
                    continue
                if len(line) <= 3 :
                    continue
                words = line.split()
                key, val = words[0], words[1:]
                key = re.sub(r'[^a-zA-Z]', '', key)
                self.d[key] = " ".join(val)
#         trie = TrieNode()
        for word in self.d.keys():
            self.trie.insert( word )
    
    
    def find(self, s) :
        s = s.capitalize()
        if s in self.d :
            return self.d[s]
        else :
            return search( s ,5, self.trie)

app = MyWindow()