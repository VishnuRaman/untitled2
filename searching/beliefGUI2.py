import ManageNode,Linking,GuiArray,Algorithms
import  math,numpy

import pickle
from tkinter import *
# import Tkinter
import tkinter.filedialog
from tkinter.simpledialog import askstring

root = Tk()
topFrame = Frame(root)
topFrame.pack(fill=X)
topFrame2 = Frame(root)
topFrame2.pack(fill=X)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# canvas
canvas = Canvas(root, width=1000,height=600,bg="light gray")
canvas.pack(expand=1,fill=BOTH)

#creating objects - link to the classes in the folder
GA=GuiArray.guiArray(canvas)
MN=ManageNode.manageNode()
LK=Linking.Graph()
AL=Algorithms.algorithms(LK.vert_dict)

global coordinates
coordinates=[]

#drop down list

# create buttons
button1 = Button(topFrame,text="Create Node")
button2 = Button(topFrame,text="Create Probability Tables")
button3 = Button(topFrame,text="Create Link")
button4 = Button(topFrame,text="Set True Probability")
button5 = Button(topFrame,text="Set False Probability")
button6 = Button(topFrame,text="Set Observation")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)

# methods called by buttons
node_id_Dic={}
prob_table_id={}
# draw on the canvas
def drawNode(e):
    #if not means if it's empty then do operation

    #canvas enclosed creates a space around where you click and checks no other objects are in that area
    #if objects are present it wont create a node there

    #if is empty then creates the oval

    if not canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105):
        oval=canvas.create_oval(e.x-50,e.y-50,e.x+50,e.y+40)

        value = askstring('value', 'Please enter a title')

      #MN.inc means increase that method by 1 as new node was created

        nodeID=MN.inc()

        nodeName=value

        #nickname given to each node
        nickname=canvas.create_text(e.x,e.y,text=str(value))

    coordinateSet=[nodeName,[e.x,e.y]]

    GUIset = [nodeName, nodeID, {}]  # number object / oval object / dictionary for linking

    node_id_Dic[oval] = nodeID
    LK.add_vertex(nodeID)
    GA.addNode(GUIset,nodeID)
    GA.addCoords(coordinateSet,nodeID)

# listen to mouse action
def CreateNode(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",drawNode)

# need to change these values so it includes table try a smaller size
#try another method so it connects to the edge of the oval
#alt try it adds a weight but just doesnt show it
def ArcPoint2(e):
    if len(canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105))==2:
        toNode=node_id_Dic[canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105)[0]]#the node is created before num so it is at [0]
        if (fromNode is not toNode)and(LK.check_edge_existed(fromNode,toNode)==False):
            root.config(cursor="")
            arrow = canvas.create_line(x,y,e.x,e.y,arrow="last")#fill="turquoise" can change color

            # weight = canvas.create_text(0.5 * (x + e.x), 0.5 * (y + e.y) - 10, text=" ")

            GA.addBeliefArrow(fromNode, toNode, arrow)

            # #this method produces the connection

            LK.add_edge(fromNode,toNode)

            canvas.bind("<Button-1>",ArcPoint1)

# listen to the first click for the line
def ArcPoint1(e):
    #==2 need to change this to == length of string input +1
    if len(canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105))==2:
    #global equivalent of instance variable
    #used this so its able to be used by different methods
    #x,y =location and fromNode = the id of the node you pick up - the one you draw FROM
        global x,y,fromNode
        x,y=e.x,e.y
        fromNode=node_id_Dic[canvas.find_enclosed(e.x-105,e.y-105,e.x+105,e.y+105)[0]]
        root.config(cursor="cross")
        canvas.bind("<Button-1>",ArcPoint2)
# listen to the mouse action
def CreateArc(event):
    root.config(cursor="")
    canvas.bind("<Button-1>",ArcPoint1)

def probTable(e):

# run through nodes and find parents
# then create the grids according to the coordinates for location
# and the parents for the no. of rows you need

#     # need to factor these tables into the above
#     # draw the node first then the table afterwards
        probTable=canvas.create_rectangle(e.x-60,e.y-30,e.x-140,e.y+30)
        tableHorizLine2 = canvas.create_line(e.x-60,e.y,e.x-140,e.y)
        tableVertLine = canvas.create_line(e.x - 100, e.y - 30, e.x - 100, e.y + 30)
        falseLabel=canvas.create_text(e.x-80,e.y-15,text="F")
        trueLabel = canvas.create_text(e.x-120,e.y-15,text="T")

        for n in GA.coordList:
            if n[2]==0:
                print("aaaaa")

def parentProb(event):
    root.config(cursor="cross")
    canvas.bind("<Button-1>",probTable)
#
#
def setTrueProb(e):

    valueT = askstring('value', 'Please enter a true probability value')

    valueT = getdouble(valueT)

    # error message aspect
    # # need to change this so it doesnt print the value too
    # if valueT>1.0:
    #     print("Please enter a value below 1")

#need to add nodeID to the front before the T and the F like the test oens
    valueTrueSet=["T", valueT]

    print(valueTrueSet)

    for i in coordinates[2][0]:
        if e.x in range(0,i):
            print("qwerty")

    #need to sort out error handling here if no value entered/cancelled

    #if true box is clicked enter value
    if not canvas.find_enclosed(e.x-20, e.y, e.x+20, e.y+30):
        canvas.create_text(e.x, e.y, text=valueT)


def ParentTrueProb(event):
    root.config(cursor="cross")
    canvas.bind("<Button-1>", setTrueProb)
#
#
def setFalseProb(e):
    valueF = askstring('value', 'Please enter a false probability value')

    valueF = getdouble(valueF)


    valueFalseSet = ["F" , valueF]


    print(valueFalseSet)

    # need to sort out error handling here if no value entered/cancelled

    # if false box is clicked enter value
    if not canvas.find_enclosed(e.x - 20, e.y, e.x + 20, e.y + 30):
        canvas.create_text(e.x, e.y, text=valueF)


def ParentFalseProb(event):
    root.config(cursor="cross")
    canvas.bind("<Button-1>", setFalseProb)
#
# def setTF(e): #change this to run the algorithm too
#
#     #alternatively do a drop down list of all the nodes from the dictionary
#     #instead of an entry box
#
#
#         Label(root, text="Select Node:").pack(side=LEFT)
#
#         e1 = Entry(root)
#
#         e1.pack(side=LEFT)
#
#         chosenNode = e1.get()
#
#     #check after input then print
#     #alt create a button that confirms the input then prints
#     #store in a list - as order is necessary must be t/f then value
#
#         print("aaaaaa")
#         print(chosenNode) #not printing????
#         print("bbbb")
#
#
#         global truevar
#
#         truevar = IntVar()
#
#         true = Checkbutton(root, text="True", variable=truevar)
#         true.pack(side=LEFT)
#
#         falsevar=IntVar()
#         false = Checkbutton(root, text="False", variable=falsevar)
#         false.pack(side=LEFT)
#         falsevar.get()
#         # print(falsevar.get())
#
#
#         print("eeeee")
#         truevar.get()
#
#         print(truevar.get())
#
#
#         # need to check if its selected
#
#     # if truevar.get() == 0:
#         #      print("T")
#         #
#         # else:
#         #     print("F")
#
#         print("ccccc")
#
# def SetObs(event):
#     root.config(cursor="cross")
#     canvas.bind("<Button-1>", setTF)


button1.bind("<Button-1>",CreateNode)
button2.bind("<Button-1>",parentProb)
button3.bind("<Button-1>",CreateArc)
button4.bind("<Button-1>",ParentTrueProb)
button5.bind("<Button-1>",ParentFalseProb)
# button6.bind("<Button-1>", SetObs)


root.mainloop()
