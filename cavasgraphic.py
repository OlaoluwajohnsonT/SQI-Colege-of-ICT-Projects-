from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from PIL import ImageTk, Image, ImageGrab
import tkinter.colorchooser
import os

class  GraphicsEditor():
    def __init__(self):
        self.root = Tk()
        self.root.title('Graphic Editor')
        self.frame =Frame(self.root, height = 600, width = 1000, bd = 20)
        
        self.frame.pack()  
        self.frame3 =Frame(self.frame, height = 600, width = 50, bg= '#a7b8cf')
        self.frame3.pack(side = 'left')
        self.bgcolor = 'white'
        self.canva = Canvas(self.frame3, bg = self.bgcolor, height = 600, width = 1000, relief = 'raised', borderwidth =1)
        self.canva.pack(side= 'right')
        self.canva.bind("<B1-Motion>", self.mouseMove)
        self.canva.bind("<Button-1>", self.ButtonPress)
        self.canva.bind( "<Double-1>", self.doubleClick)
        self.choosen_color ='#000000'
        self.eventState = ""
        self.file =""
        self.count = 1
        self.loadImage()
        self.creatGUI()
        
   
    def ButtonPress(self, event):
        self.eventState = "B1-pressed"
        self.item_id = self.canva.find_withtag(CURRENT)
        self.lastx = event.x
        self.lasty = event.y

    def doubleClick(self, event):
        self.eventState = "D1-pressed"
        # Translate mouse screen x0,y0 coordinates to canvas coordinates
        self.item_id = self.canva.find_withtag(CURRENT)
        if self.item_id:
            self.item_coords = self.canva.coords(self.item_id)
            self.lastx = self.item_coords[0]
            self.lasty= self.item_coords[1]       
        else:
            pass
    
    def mouseMove(self, event):
        if self.eventState == "B1-pressed":
            self.canva.move(CURRENT, event.x - self.lastx, event.y - self.lasty)
            self.lastx = event.x
            self.lasty = event.y

        elif self.eventState == "D1-pressed":
            #Translate mouse screen x1,y1 coordinates to canvas coordinates
            self.lastx1 = event.x
            self.lasty1 = event.y
            #Modify rectangle x1, y1 coordinates
            self.canva.coords(self.item_id, self.lastx, self.lasty, self.lastx1, self.lasty1)

    def drawObject(self, draw):
        self.canva.configure(cursor = "plus")
        self.coords = {"x":0,"y":0,"x2":0,"y2":0}
        # keep a reference to all lines by keeping them in a list 
        self.lines = []
        if draw == "line":
            def click(event):
                # define start point for line
                self.coords["x"] = event.x
                self.coords["y"] = event.y 
                # create a line on this point and store it in the list
                self.line_id = self.lines.append(self.canva.create_line(self.coords["x"],self.coords["y"],self.coords["x2"],self.coords["y2"], tag="linetag", activefill=self.choosen_color))
               
            def drag(event):
                # update the coordinates from the event
                self.coords["x2"] = event.x
                self.coords["y2"] = event.y
                # Change the coordinates of the last created line to the new coordinates
                self.canva.coords(self.lines[-1], self.coords["x"],self.coords["y"],self.coords["x2"],self.coords["y2"])
        elif draw == "circle":
            def click(event):
                self.lastx = event.x
                self.lasty = event.y
                self.circle_id =self.canva.create_oval(self.lastx, self.lasty, self.lastx, self.lasty, tag="circletag", activefill=self.choosen_color)
               
            def drag(event):
                self.lastx2 = event.x
                self.lasty2 = event.y
                self.canva.coords(self.circle_id, self.lastx, self.lasty, self.lastx2, self.lasty2)
        elif draw == "rectangle":
            def click(event):
                self.lastx = event.x
                self.lasty = event.y
                self.rec_id =self.canva.create_rectangle(self.lastx, self.lasty, self.lastx, self.lasty, tag="circletag", activefill=self.choosen_color)
               
            def drag(event):
                self.lastx2 = event.x
                self.lasty2 = event.y
                self.canva.coords(self.rec_id, self.lastx, self.lasty, self.lastx2, self.lasty2)
                       

        self.canva.bind("<ButtonPress-1>", click)
        self.canva.bind("<B1-Motion>", drag)
    
    def paint(self):
        self.canva.configure(cursor = "plus")
        self.coords = {"x":0,"y":0,"x2":0,"y2":0}
        # keep a reference to all lines by keeping them in a list 
        self.lines = []
        def click(event):
            # define start point for line
            self.coords["x"] = (event.x -4)
            self.coords["y"] = (event.y -4) 
            # create a line on this point and store it in the list
            self.line_id = self.lines.append(self.canva.create_oval(self.coords["x"],self.coords["y"],self.coords["x2"],self.coords["y2"], tag="linetag", activefill=self.choosen_color))
           
        def drag(event):
            # update the coordinates from the event
            self.coords["x2"] = (event.x -4)
            self.coords["y2"] = (event.y -4) 
            # Change the coordinates of the last created line to the new coordinates
            self.line_id = self.lines.append(self.canva.create_oval(self.coords["x"],self.coords["y"],self.coords["x2"],self.coords["y2"], tag="linetag", activefill=self.choosen_color))
        self.canva.bind("<ButtonPress-1>", click)
        self.canva.bind("<B1-Motion>", drag)

    def triangle(self):
        arcs = self.canva.create_line(30,50,30,200,90,200,30,48, fill='red', ) 

    def colorchooser(self):
        self.colorfill = tkinter.colorchooser.askcolor()
        self.choosen_color =self.colorfill[1]
        self.canva.itemconfig(self.item_id, fill=self.colorfill[1])

    def bg_change(self):
        self.bgcolor = tkinter.colorchooser.askcolor()
        self.canva.config(bg =self.bgcolor[1])

    def changeCursor(self):
        self.canva.configure(cursor = "arrow")
        self.canva.unbind("<ButtonPress-1>")
        self.canva.unbind("<B1-Motion>")
        self.canva.bind( "<Double-1>")
        self.canva.bind("<Button-1>", self.ButtonPress)
        self.canva.bind("<B1-Motion>", self.mouseMove)

    #**********************************************************INSERT IMAGE************************************************************************************
    def loadImage(self):
        loadcursor = Image.open('iconimage/Cursor.png')
        self.image_cursor = ImageTk.PhotoImage(loadcursor, master = self.root)

        loadcircle = Image.open('iconimage/circle.png')
        self.image_circle = ImageTk.PhotoImage(loadcircle, master = self.root)

        loadrectangle = Image.open('iconimage/rectangular.png')
        self.image_rectangle= ImageTk.PhotoImage(loadrectangle, master = self.root)

        loadpolygon = Image.open('iconimage/polygon.png')
        self.image_polygon = ImageTk.PhotoImage(loadpolygon, master = self.root)

        loadline = Image.open('iconimage/horizontalline.png')
        self.image_line = ImageTk.PhotoImage(loadline, master = self.root)

        loadoval = Image.open('iconimage/oval.png')
        self.image_oval = ImageTk.PhotoImage(loadoval, master = self.root)

        loadsquare = Image.open('iconimage/square.png')
        self.image_square = ImageTk.PhotoImage(loadsquare, master = self.root)

        loadtriangle = Image.open('iconimage/triangle.png')
        self.image_triangle = ImageTk.PhotoImage(loadtriangle, master = self.root)

        loadpaint = Image.open('iconimage/paint.png')
        self.image_paint = ImageTk.PhotoImage(loadpaint, master = self.root)

        loadungroup = Image.open('iconimage/ungroup.png')
        self.image_ungroup = ImageTk.PhotoImage(loadungroup, master = self.root)

        loadopen = Image.open('iconimage/open.png')
        self.image_open = ImageTk.PhotoImage(loadopen, master = self.root)

        loadsave = Image.open('iconimage/save.png')
        self.image_save = ImageTk.PhotoImage(loadsave, master = self.root)

        loadsaveas = Image.open('iconimage/saveas.png')
        self.image_saveas = ImageTk.PhotoImage(loadsaveas, master = self.root)

        loaddelete = Image.open('iconimage/delete.png')
        self.image_delete = ImageTk.PhotoImage(loaddelete, master = self.root)

        loadcolorwheel = Image.open('iconimage/colorwheel.png')
        self.image_colorwheel = ImageTk.PhotoImage(loadcolorwheel, master = self.root)

        loadnew = Image.open('iconimage/addnew.png')
        self.image_new = ImageTk.PhotoImage(loadnew, master = self.root)

        loadexit = Image.open('iconimage/exit.png')
        self.image_exit = ImageTk.PhotoImage(loadexit, master = self.root)

        loadview = Image.open('iconimage/view.png')
        self.image_view = ImageTk.PhotoImage(loadview, master = self.root)

        loadabout = Image.open('iconimage/about.png')
        self.image_about = ImageTk.PhotoImage(loadabout, master = self.root)

        loadcut = Image.open('iconimage/cut.png')
        self.image_cut = ImageTk.PhotoImage(loadcut, master = self.root)

        loadcopy = Image.open('iconimage/copy.png')
        self.image_copy = ImageTk.PhotoImage(loadcopy, master = self.root)

        loadpaste = Image.open('iconimage/paste.png')
        self.image_paste = ImageTk.PhotoImage(loadpaste, master = self.root)

        loadselectall = Image.open('iconimage/selectall.png')
        self.image_selectall = ImageTk.PhotoImage(loadselectall, master = self.root)

        #**********************************************************BUTTON IMAGE********************************************
        Button(self.frame3, image= self.image_cursor, command=self.changeCursor).pack()
        Button(self.frame3, image=self.image_circle, command = lambda:self.drawObject('circle')).pack()
        Button(self.frame3, image=self.image_rectangle, command = lambda:self.drawObject("rectangle")).pack()
        # oval_btn = Button(self.frame3, image=self.image_oval, command =  lambda:self.oval).pack()
        Button(self.frame3, image= self.image_paint, command= self.paint).pack()
        # Button(self.frame3, image=self.image_square).pack()
        Button(self.frame3,image=self.image_triangle, command = self.triangle).pack()
        # Button(self.frame3,image=self.image_ungroup).pack()
        Button(self.frame3,image = self.image_line, command = lambda:self.drawObject("line")).pack()

        #Top buuton
        arrowopen = Button(self.frame,image=self.image_open).pack(side = 'top')
        arrownew = Button(self.frame,image=self.image_new).pack(side = 'top')
        arrowbtnsave = Button(self.frame,image=self.image_save).pack(side = 'top')
        arrowcolor = Button(self.frame,image=self.image_colorwheel, command = self.colorchooser)
        arrowcolor.pack(side = 'top')
    #**********************************************************MENU BAR IMAGE***********************************************
    
    def newFile(self):
        msg = askyesnocancel('Warning', 'Do you want to save the current File?')
        if msg == True:
            saveFile
            if file == None:
                file = ''
            else:
                self.count += 1
                self.root.title('Untitle'+ str(self.count)+ ' -GraphicsEditor')
                file = " "
                self.canva.delete(self.canva.find_all())

        elif msg == False:
            self.count += 1
            self.root.title('Untitle'+ str(self.count)+ ' -GraphicsEditor')
            file = " "
            self.canva.delete(self.canva.find_all())           

    def saveFile(self):
        self.file = asksaveasfilename(defaultextension = '.png', filetypes = [("All Files","*.*"), ("jpg",".jpg"),("png", ".png"), ("gif",".gif"),("Bitmap", ".bmp")] )
        x = self.canva.winfo_rootx()
        y = self.canva.winfo_rooty()
        x1 = x + self.canva.winfo_width()
        y1 = y + self.canva.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(self.file)
        # global file
        # if file == '':
        #     file = asksaveasfilename(defaultextension = '.png', filetypes = [('All Files', ('.png'))] )
        #     with open(file, 'w') as infile :
        #         infile.write(self.canva.get(1.0, END))
        #         #changine the window title
        #         self.root.title(os.path.basename(infile)+ '-Hindypng')
        #         showinfo('Message', 'This file has been saved')
                
        # else:
        #     with open(file, 'w') as infile : 
        #         infile.write(self.canva.get(1.0, END))
        #         #changine the window title
        #         self.root.title(os.path.basename(file)+ '-Hindypng')
        #         showinfo('Message', 'This file has been saved')

    def openFile(self):
        try:
            self.file = askopenfilename(defaultextension = '.png', filetypes = [("All Files","*.*"), ("jpg",".jpg"),("png", ".png"), ("gif",".gif"),("Bitmap", ".bmp")] )
            self.image = Image.open(self.file)
            self.image = ImageTk.PhotoImage(self.image)
            self.item_id = self.canva.create_image(400,400,image=self.image)
            # if file != '':
            #     with open (file, 'r') as infile:
            #         self.root.title(os.path.basename(file) +  '- Hindyfile')
            #         self.canva.delete(1.0, END)
            #         myfile = infile.read()
            #         self.canva.insert(1.0, myfile, END)
        except:
            pass

    def saveAs(self):
        file = asksaveasfilename(defaultextension = '.png', filetypes = [('All Files', ('.png'))] )
        with open(file, 'w') as infile :
            infile.write(self.canva.get(1.0, END))
            #changine the window title
            self.root.title(os.path.basename(infile)+ '-Hindypng')
            showinfo('Message', 'This file has been saved')
    def exit(self):
        self.root.destroy()

    def copyF(self):
        self.canva.event_generate(("<<Copy>>"))

    def pasteF(self):
        self.canva.event_generate(("<<Paste>>"))


    def cutF(self):
        self.canva.event_generate(("<<Cut>>"))


    def selectAll(self):
        try:
            self.canva.tag_add(SEL, '1.0', END)
            self.canva.mark_set(INSERT, '1.0')
            self.canva.see(INSERT)
            return 'break'

        except:
            showinfo('Warning', 'There is nothing to select')


    def deleteSel(self):
        try:
            self.canva.delete(self.canva.find_all())    
        except:
            showinfo('Warning', 'Please kindly select a portion to delete')

    def creatGUI(self):
        menubar = Menu()
        filemenu = Menu(menubar, tearoff = 0)
        helpmenu = Menu(menubar, tearoff = 0)
        editmenu = Menu(menubar, tearoff = 0)
        #for Filemenu
        filemenu.add_command(label='New', image = self.image_new , compound = 'left', command = self.newFile)
        filemenu.add_command(label='Open', image = self.image_open, compound = 'left', command= self.openFile)
        filemenu.add_command(label='Save', image =self.image_save, compound = 'left', command =  self.saveFile)
        filemenu.add_command(label='Save As',image =self.image_saveas, compound = 'left', command= self.saveAs)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', image =self.image_exit, compound = 'left', command  = self.exit)
        menubar.add_cascade(label='File', menu = filemenu)

        editmenu.add_command(label='Select All      ctrl+A',image = self.image_selectall, compound = 'left', command = self.selectAll)
        editmenu.add_command(label='Copy            ctrl+C',image= self.image_copy, compound = 'left', command = self.copyF)
        editmenu.add_command(label='Cut             ctrl+X', image = self.image_cut, compound = 'left', command = self.cutF)
        editmenu.add_command(label='Delete          ctrl+D', image = self.image_delete, compound = 'left', command = self.deleteSel)
        editmenu.add_command(label='Paste           ctrl+V',image = self.image_paste, compound = 'left', command =self.pasteF)
        editmenu.add_command(label='Change background',image = self.image_colorwheel, compound = 'left', command = self.bg_change)
        menubar.add_cascade(label='Edit', menu = editmenu)

        #For helpMenu
        helpmenu.add_command(label='View Help', image = self.image_view, compound = 'left' )
        helpmenu.add_command(label='About Vector', image = self.image_about, compound= 'left')
        menubar.add_cascade(label='Help', menu = helpmenu)
        self.root.config(menu = menubar)

        self.root.mainloop()

ge = GraphicsEditor()
