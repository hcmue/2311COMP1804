# import all classes/methods 
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
  
# The main tkinter window 
root = Tk() 
  
# setting the title and  
root.title('Plotting in Tkinter') 
  
# setting the dimensions of the main window 
root.geometry("500x500") 



def plot():  
    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5), dpi = 100) 
  
    # list of squares 
    y = [i**2 for i in range(101)] 
  
    # adding the subplot 
    plot1 = fig.add_subplot(111) 
  
    # plotting the graph 
    plot1.plot(y) 
  
    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, master = root)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, root) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack()
  
# button that would displays the plot 
plot_button = Button(master = root, 
                     height = 2, 
                     width = 10, 
                    text = "Plot",
                    command=plot) 
# place the button into the window 
plot_button.pack() 
  
# run the gui 
root.mainloop()