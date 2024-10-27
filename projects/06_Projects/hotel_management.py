from tkinter import simpledialog, messagebox

rooms = {
    1:'',
    2:'',
    3:''
}

def check_in_or_out():
    checkin = simpledialog.askstring(None, prompt="would you like to check in or out a quest?")
    if checkin == "check in":
       pass
    elif checkin == "check out":
        pass
    else:
        messagebox.showinfo(None, message="try saying check in or check out")