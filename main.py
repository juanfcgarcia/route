from tkinter import Tk, Frame, Label, Button, Spinbox
from tkinter.ttk import Notebook, Entry
from multiprocessing import Process, Manager
import time
import dijsktra as dj
import data_structure as ds

origins = []
destinations = []
entry_label = []
interface_messages = ["Do you want to find more than one route?",
                      "Please enter the number of routes you want to find"]

control_count = False
optionStatus = False

window = Tk()
window.title("Route")
window.geometry("1280x720")
window.configure(background="#111111")

frame = Frame(window)
frame.config(bg="#de411b")

ui_message = Label()

count_requests = 0
ui_count_routes = Spinbox(window, from_=1, to=4)

table = Notebook(frame)

tab1 = Frame(table)
tab1.config(bg="#DE411B")


def ui_static_elements(space_1, space_2):
    txt_header = Label(window, text="Route",
                       height=1, width=184,
                       bg="#222222",
                       fg="#DE411B",
                       font=("helvetica", 32, "bold"))
    txt_header.pack()
    spacing2.pack()
    spacing1.pack()


def show_solution():
    spacing5 = Label(window, text="")
    spacing5.config(bg="#111111",
                    height=1)
    txt_solution = Label(window, text="Fastest Route: " + str(routes_results),
                         height=1,
                         width=184,
                         bg="#111111",
                         fg="#F0F0F0",
                         font=("Arial", 16, "bold"))

    txt_weight = Label(window, text="Weight: " + str(weights_results),
                       height=1,
                       width=184,
                       bg="#111111",
                       fg="#F0F0F0",
                       font=("Arial", 16, "bold"))
    spacing5.pack()
    txt_solution.pack()
    txt_weight.pack()


def route_request():
    final_graph = ds.create_graph()
    processes_list = []
    time_init = time.time()

    for processes in range(count_requests):
        process_route = Process(target=dj.dijkstra, args=(final_graph, origins[processes], destinations[processes], routes_results, weights_results))
        process_route.start()
        processes_list.append(process_route)

    for p in processes_list:
        p.join()

    time_end = time.time() - time_init
    print("Time: " + str(time_end))
    show_solution()



def create_ui_tables():
    for row in range(count_requests):
        for column in range(2):
            label = Entry(tab1,
                          text="Row : " + str(row) + " , Column : " + str(column),
                          justify="center")
            label.config(font=("Arial", 14))

            entry_label.append(Entry(tab1, text="Row : " + str(row) + " , Column : " + str(column)))
            label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
            tab1.grid_columnconfigure(column, weight=1)
    frame.pack(fill="both")
    table.add(tab1, text="Init")


def get_from_tables():
    counter = 0
    origins.clear()
    destinations.clear()
    for row in range(count_requests):
        for column in range(2):
            if column == 0:
                origins.append(str(entry_label[counter].get()))
            else:
                destinations.append(str(entry_label[counter].get()))
            counter += 1


def setDataInicial(btn):
    get_from_tables()
    route_request()


def create_table():
    global count_requests
    if optionStatus == True:
        count_requests = int(ui_count_routes.get())
    else:
        count_requests = 1
    ui_message.config(text="From                              To", height=1, width=184, bg="#111111",
                      fg="#F0F0F0", font=("Arial", 16, "bold"))

    create_ui_tables()
    table.pack(fill="none", side="bottom")
    tab1.pack(fill="none", side="bottom")
    create_tab.destroy()
    ui_count_routes.destroy()
    btn_set = Button(window, text="Find route", command=setDataInicial, bg="#DE411B", fg="white",
                     borderwidth=0, font=("Arial", 16, "bold"))
    btn_set["command"] = lambda btn=btn_set: setDataInicial(btn)
    spacing4 = Label(window, text="")
    spacing4.config(bg="#111111", height=1)
    spacing4.pack()
    btn_set.pack()


def yes_op():
    global control_count
    global optionStatus
    optionStatus = True
    control_count = True
    btnYes.destroy()
    btnNo.destroy()
    messages_interface()
    spinner_count()
    spacing3 = Label(window, text="")
    spacing3.config(bg="#111111", height=1)
    spacing3.pack()
    create_tab.pack()


def no_op():
    global control_count
    global optionStatus
    optionStatus = False
    btnYes.destroy()
    btnNo.destroy()
    control_count = True
    create_table()


def messages_interface():
    global ui_message
    if not control_count:
        ui_message = Label(window, text=interface_messages[0], height=1, width=184, bg="#111111",
                           fg="#F0F0F0", font=("Arial", 16, "bold"))
        ui_message.pack()
    else:
        ui_message.config(text=interface_messages[1], height=1, width=184, bg="#111111",
                          fg="#F0F0F0", font=("Arial", 16, "bold"))


def spinner_count():
    global ui_count_routes
    ui_count_routes.config(bg="#222222", borderwidth=0, fg="#DE411B", justify="center", font=("Arial", 14))
    ui_count_routes.pack()


spacing1 = Label(window, text="")
spacing1.config(bg="#111111")
spacing2 = Label(window, text="")
spacing2.config(bg="#111111", height=16)

create_tab = Button(window, text="Confirm", command=create_table, borderwidth=0)
create_tab.config(font=("Arial", 16, "bold"), bg="#DE411B", fg="white")

ui_static_elements(spacing1, spacing2)

if not control_count:
    btnNo = Button(window, text="No", command=no_op, borderwidth=0)
    btnNo.config(font=("Arial", 16), bg="#000000", fg="white")
    btnNo.place(x=580, y=364)
    btnYes = Button(window, text="Yes", command=yes_op, bg="#55575D", fg="white", borderwidth=0, font=("Arial", 16))
    btnYes.place(x=630, y=364)
    messages_interface()

if __name__ == "__main__":
    manager = Manager()
    routes_results = manager.list()
    weights_results = manager.list()
    window.mainloop()
