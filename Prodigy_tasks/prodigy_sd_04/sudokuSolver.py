import tkinter as tk
from tkinter import messagebox

# Sudoku solving functions
def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        puzzle[row][col] = -1

    return False

# GUI
class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.puzzle = [[-1 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()
        
        for r in range(9):
            for c in range(9):
                entry = tk.Entry(frame, width=5, font=('Arial', 18), justify='center')
                entry.grid(row=r, column=c, padx=5, pady=5)
                self.entries[r][c] = entry

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.pack()

    def solve(self):
        try:
            for r in range(9):
                for c in range(9):
                    value = self.entries[r][c].get()
                    if value == '':
                        self.puzzle[r][c] = -1
                    else:
                        self.puzzle[r][c] = int(value)
            
            if solve_sudoku(self.puzzle):
                for r in range(9):
                    for c in range(9):
                        self.entries[r][c].delete(0, tk.END)
                        self.entries[r][c].insert(0, str(self.puzzle[r][c]))
            else:
                messagebox.showinfo("Sudoku Solver", "this puzzle is not solvable.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter numbers between 1 and 9.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
