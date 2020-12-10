import shelve
from tkinter import *

class application(Frame):
    
    def __init__(self, master):
        
        super(application, self).__init__(master)
        self.grid()
        self.widgets()
        self.dup()
        self.tngDisplay()
        self.aut()
        self.gen()
        self.dup()
    def widgets(self):
        

        self.fileData = 'data'  

        # label title
        Label(self,
              text = "title:"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # field title
        self.title_ent = Entry(self)
        self.title_ent.grid(row = 0, column = 1, sticky = W)


        # label author
        Label(self,
              text = "author:"
              ).grid(row = 1, column = 0, sticky = W)

        # field author
        self.author_ent = Entry(self)
        self.author_ent.grid(row = 1, column = 1, sticky = W)


        # label year
        Label(self,
              text = "year:"
              ).grid(row = 2, column = 0, sticky = W)

        # field year
        self.year_ent = Entry(self)
        self.year_ent.grid(row = 2, column = 1, sticky = W)


        # label genre
        Label(self,
              text = "genre:"
              ).grid(row = 3, column = 0,  sticky = W)

        # field genre
        self.genre_ent = Entry(self)
        self.genre_ent.grid(row = 3, column = 1, sticky = W)

#=========BUTTONS
        # insert button
        Button(self,
               text = "insert",
               command = self.insert
               ).grid(row = 5, column = 0, sticky = W)

# clear button
        Button(self,
               text = "clear",
               command = self.clear
               ).grid(row = 5, column = 1, sticky = W)
        # delete button
        Button(self,
               text = "delete",
               command = self.delete
               ).grid(row = 5, column = 2, sticky = W)
        
        # update button
        Button(self,
               text = "update",
               command = self.update
               ).grid(row = 5, column = 3, sticky = W)


        # show all button
        Button(self,
               text = "show all",
               command = self.tngDisplay
               ).grid(row = 5, column = 4, sticky = W)



#==========FIELD FOR LISTING
        self.tngField = Listbox(self, width = 50, height = 10)
        self.tngField.grid(row = 6, column = 0, columnspan = 4)
        
        
#=========FIELD FOR GENRES
        self.geField = Listbox(self, width = 20, height = 10)
        self.geField.grid(row = 7, column = 0, columnspan = 4)
        
#=========FIELD FOR AUTORS
        self.auField = Listbox(self, width = 20, height = 10)
        self.auField.grid(row = 7, column = 2, columnspan = 4)

#==========functions



 #"official" list of book KEYS
    lb=list()

#===function to remove duplicates from author and genre list

    def dup(self):
        #datFile = shelve.open(self.fileData)
        self.au = list(dict.fromkeys(self.au))
    
        self.ge = list(dict.fromkeys(self.ge))
        
        

    def listinsert( self):
        title = self.title_ent.get()
        author = self.author_ent.get()
        year = self.year_ent.get()
        genre = self.genre_ent.get()
        tng = [title, author,year ,genre]
        return tng

    def insert (self):
        #unselect
        self.tngField.bind('<FocusOut>', lambda e: self.tngField.selection_clear(0, END))
        self.gen()
        self.aut()
        self.tngDisplay()
        tngList = self.listinsert()
        tngNumber = self.title_ent.get()

        datFile = shelve.open(self.fileData)
        #insert to the end:
        datFile[tngNumber] = tngList
       
        datFile.sync()
        datFile.close()
        

  #updating a book info 
    def update(self):
        modifiedBook=self.title_ent.get()
        print(modifiedBook)
    
        datFile = shelve.open(self.fileData)          
        for key, item in datFile.items():
            if(modifiedBook == str(key)):
               nested_dict = datFile[str(key)]
               nested_dict[0] = self.title_ent.get()
               nested_dict[1] = self.author_ent.get()
               nested_dict[2] = self.year_ent.get()
               nested_dict[3] = self.genre_ent.get()
               datFile[str(key)] = nested_dict
        self.gen()
        self.aut()
        
               
    
    
    #=====filling author field====================================================
    
    au=list() 
    def aut(self):
      
        tnn = list()
        self.auField.delete(0, END)
        datFile = shelve.open(self.fileData)
        for key, item in datFile.items():
            
          
             self.au.insert( len(self.au),str(item[1]))
             
            # self.auField.insert( END, tnn )
        self.dup()
        #from list to field
        [self.auField.insert(END, item) for item in self.au]
            
  
      #if author is selected= show only books by that author in main field  
    def on_click_aubox(self,event):
     self.dup()
     #print(self.auField.curselection()) 
     selected = self.auField.curselection()
     #if something is in an entry fields-clear it:
     self.clear()
     if len(selected) == 0:
         return
     # stores selected author:
     tit = self.au[selected[0]]
     #print(tit)

     datFile = shelve.open(self.fileData)
     #clear main field
     self.tngField.delete(0,END)
     tng = list()
  
     #go thru all shelve, if needed author= insert it into main field
     for key, item in datFile.items(): 
        
         if (tit==str(item[1])):
             tng = str(key)
             self.tngField.insert( END, tng ) 
 
    
     
     
      #=====filling genre field====================================================
      
    ge=list() 
    def gen(self):
        #tnn = list()
        self.geField.delete(0, END)
        datFile = shelve.open(self.fileData)
        for key, item in datFile.items():
            #tnn = (str(item[3]))
            self.ge.insert( len(self.ge),str(item[3]))
            
            #self.geField.insert( END, tnn )
        self.dup()
        #from list to field
        [self.geField.insert(END, item) for item in self.ge]
        
          
            
          
    
    def on_click_gebox(self,event):
       
     #selected index:
     selected = self.geField.curselection()
     self.clear()
     if len(selected) == 0:
         return
     #to store selected genre:
     tit = self.ge[selected[0]]
     
  
     datFile = shelve.open(self.fileData)
     #clear main field
     self.tngField.delete(0,END)
     
     tng = list()
     for key, item in datFile.items(): 
        
         if (tit==str(item[3])):
             tng = str(key)
             
             self.tngField.insert( END, tng ) 
             
     #==========================================================================        
     
    
    
   
    def tngDisplay (self):
    
        self.lb.clear()
        tng = list()
        tngNumber = self.title_ent.get()
        self.tngField.delete(0, END)
        self.aut()
        self.gen()
        datFile = shelve.open(self.fileData)
        for key, item in datFile.items():
            tng = str(key)
            self.lb.append(str(key))
            self.tngField.insert( END, tng )
        self.gen()
        self.aut()
        
        
        
    def on_click_listbox(self,event):
       

     #if something is in an entry fields-clear it:
     self.clear()
     #if len(selected) == 0:
         #return
         
     # stores the title of selected:
     tit = self.tngField.get(self.tngField.curselection())
     print(tit)
     datFile = shelve.open(self.fileData)
     for key, item in datFile.items():
         if (tit==str(key)):
             #insert to the entry fields with selected:
             self.title_ent.insert(0, str(item[0]))
             self.author_ent.insert(0, str(item[1]) )
             self.year_ent.insert(0, str(item[2]) )
             self.genre_ent.insert(0, str(item[3]) )
             #print(str(key) + ': ' + str(item))
     
      
    def clear(self):
     self.title_ent.delete(0, END) 
     self.author_ent.delete(0, END)
     self.year_ent.delete(0, END) 
     self.genre_ent.delete(0, END) 
     
    def delete(self):
    #title of a book to delete:
     d=self.title_ent.get()
     #print(d)
     datFile = shelve.open(self.fileData)
     for key, item in datFile.items():
         if (d==str(key)):
             del datFile[d]
     self.gen()
     self.aut()
             
     
     
     
                
        
    

    
    
root = Tk()
root.title('Book management')
app = application(root)
app.tngField.bind('<ButtonRelease-1>', app.on_click_listbox)
app.auField.bind('<ButtonRelease-1>', app.on_click_aubox)
app.geField.bind('<ButtonRelease-1>', app.on_click_gebox)
root.mainloop()