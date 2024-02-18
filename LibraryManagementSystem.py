# Library Management System

class Library:
     
    def __init__(self):
      self.file = open("books.txt","a+",encoding="utf-8")      
    def __del__(self): 
      self.file.close()
      print("file close")
      
          
    def addBook(self):
        
        bookName=input("Write the book name: ") 
        if bookName=="":
           raise Exception("Incomplete data entry")                
        author=input("Write the author name: ")
        if author=="":
            raise Exception("Incomplete data entry") 
        releaseDate=input("Write the release date: ")
        if releaseDate=="":
            raise Exception("Incomplete data entry")                  
        numberOfPages=input("Write the number of pages: ")
        if numberOfPages=="":
            raise Exception("Incomplete data entry") 
            
        book= bookName+","+author+","+releaseDate+","+numberOfPages
        self.file.write(book+"\n")
                
            
            
    def listBooks(self):
       
       self.file.seek(0)
       content=self.file.read()
       list1=content.splitlines()
       for book in list1:   
          list2=book.split(",")
          print("Book name: "+list2[0]+","+" Author: "+list2[1])
         
        
     
    def removeBook(self):  
        
        bookName =input("Please write the name of the book you want to delete: ")
        self.file.seek(0)
        content=self.file.read()
        list1=content.splitlines()
        self.file.truncate(0)  
        case=False
        for book in list1:
            list2=book.split(",")
            if list2[0]==bookName:
               case=True 
            else:
               self.file.write(book+"\n") 
                
        if case==True:
           print(bookName+" deleted")
        else:
           print("The book you wanted to delete was not found!")
        


lib=Library()

menu="""
***MENU***
1) List Books
2) Add Book
3) Remove Book
q) Quit 
""" 

while True:
    print(menu)
    choice=input("Enter your choice(1-4):")
    if choice =="q":
        del lib    # We close the file when we log out
        print("You are logged out")
        break
    elif choice =="1":
       lib.listBooks() 
    elif choice =="2":
       lib.addBook()
    elif choice =="3":
        lib.removeBook()
    else:
        raise Exception("Invalid transaction entry!")

