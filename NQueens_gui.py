import tkinter as tk

#%% Set initial info

n = 4

pos_list = [0] * n
#%% Define functions

def count_conflicts():
    n_pieces = len(pos_list)
    # don't need to check column conflicts because each queen in separate column
    
    # check number of diagonal and row conflicts
    diag_conflicts = 0
    row_conflicts = 0
    for i in range(n_pieces):
        for j in range(i+1,n_pieces):
            if abs(pos_list[j] - pos_list[i]) == j - i:
                diag_conflicts += 1
            if pos_list[i] == pos_list[j]:
                row_conflicts += 1
                
    lbl_conflicts.config(text = "Current Conflicts: {}".format(row_conflicts + diag_conflicts))

#%% Make the window
window = tk.Tk()
window.title("N Queens")

frm_board = tk.Frame(master=window)
lbl_board = tk.Label(master=frm_board, text="Board Label")
lbl_board.pack()

frm_info = tk.Frame(master=window)
lbl_conflicts = tk.Label(master=frm_info, text="Current Conflicts: not calculated")
lbl_instr = tk.Label(master=frm_info, text="Click a square to move the column's queen there")
btn_recalc = tk.Button(master=frm_info, text="Recalculate Conflicts", command=count_conflicts)
lbl_conflicts.pack()
lbl_instr.pack()
btn_recalc.pack()

frm_board.grid(row=0, column=0, sticky="ew")
frm_info.grid(row=0, column=1, sticky="ew")

window.mainloop()