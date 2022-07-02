import tkinter as tk
import textwrap

# Constants
SOFTWARE_NAME = "Calculator"

# Global variables
the_math = ""
the_result = 0

# The display screen of the calculator
class DisplayScreen:
    def __init__(self, parent, grid_row = None, grid_col = None) -> None:
        global the_math, the_result
        self.screen = tk.Label (
            master = parent,
            height = 2,
            text = the_math + "\n" + str(the_result),
            font = "Consolas, 20",
            anchor = 'e',
            justify = tk.RIGHT,
            background = 'white'
        )
        self.screen.grid(row = grid_row, column = grid_col, sticky = 'news')
    
    # Update screen content
    def update(self):
        global the_math, the_result
        lines = textwrap.wrap(the_math, width = 22)
        math_to_show = ""
        self.screen['height'] = 2 if len(lines) <= 0 else len(lines) + 1
        for line in lines:
            math_to_show += line + "\n"
        self.screen['text'] = math_to_show[:-1] + "\n" + str(the_result)

# Class for buttons of calculator
class Button:
    def __init__(self, parent, grid_row = None, grid_col = None, text = "Empty", feature = None) -> None:
        self.button = tk.Button (
            master = parent, text = text, command = feature,
            padx = 5, pady = 5, width = 10
        )
        self.button.grid(row = grid_row, column = grid_col, sticky = 'news')

    def backspace():
        global the_math, display_screen
        the_math = the_math[0:-1]
        display_screen.update()

    def clear():
        global the_math, the_result, display_screen
        the_math = ""
        the_result = 0
        display_screen.update()

    def insert_math(character):
        global the_math, display_screen, the_result
        if the_result != 0:
            the_math = str(the_result) if 'math error' not in str(the_result).lower() else ""
            the_result = 0
        the_math += character
        display_screen.update()

# Class for calculation
class Calculator:
    def calculate(expression):
        return eval(expression)

    def do_the_math():
        global the_math, the_result, display_screen
        try:
            the_result = Calculator.calculate(the_math)
        except:
            the_result = "Math Error"
        display_screen.update()

# The main window of software
class MainWindow:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.resizable(width = False, height = False)

        self.window.title(SOFTWARE_NAME)
        
        # Create a display frame
        display_frame = tk.Frame (
            self.window, background = 'black',
            border = 2
        )
        display_frame.pack(side = tk.TOP, fill = 'both')

        # Add the display screen to top of root frame
        display_frame.grid_rowconfigure(index = 0, weight = 1)
        display_frame.grid_columnconfigure(index = 0, weight = 1)
        global display_screen
        display_screen = DisplayScreen(display_frame, grid_row = 0, grid_col = 0)

        # Add a frame for buttons to bottom of root frame
        buttons_frame = tk.Frame (
            self.window, background = 'gray', border = 2
        )
        buttons_frame.pack(fill = 'both')

        # Add buttons to buttons frame

        # Backspace button
        buttons_frame.grid_rowconfigure(0, weight = 1)
        buttons_frame.grid_columnconfigure(0, weight = 1)
        backspace_button = Button (
            buttons_frame, grid_row = 0, grid_col = 0,
            text = "Backspace", feature = Button.backspace
        )

        # Clear button
        buttons_frame.grid_rowconfigure(0, weight = 1)
        buttons_frame.grid_columnconfigure(1, weight = 1)
        clear_button = Button (
            buttons_frame, grid_row = 0, grid_col = 1,
            text = "Clear", feature = Button.clear
        )

        # Open bracket button
        buttons_frame.grid_rowconfigure(0, weight = 1)
        buttons_frame.grid_columnconfigure(2, weight = 1)
        open_button = Button (
            buttons_frame, grid_row = 0, grid_col = 2,
            text = "(", feature = lambda: Button.insert_math("(")
        )

        # Divide button
        buttons_frame.grid_rowconfigure(1, weight = 1)
        buttons_frame.grid_columnconfigure(3, weight = 1)
        divide_button = Button (
            buttons_frame, 1, 3,
            text = "/", feature = lambda: Button.insert_math("/")
        )

        # Seven button
        buttons_frame.grid_rowconfigure(1, weight = 1)
        buttons_frame.grid_columnconfigure(0, weight = 1)
        seven_button = Button (
            buttons_frame, 1, 0,
            text = "7", feature = lambda: Button.insert_math("7")
        )
        
        # Eight button
        buttons_frame.grid_rowconfigure(1, weight = 1)
        buttons_frame.grid_columnconfigure(1, weight = 1)
        eight_button = Button (
            buttons_frame, 1, 1,
            text = "8", feature = lambda: Button.insert_math("8")
        )

        # Nine button
        buttons_frame.grid_rowconfigure(1, weight = 1)
        buttons_frame.grid_columnconfigure(2, weight = 1)
        nine_button = Button (
            buttons_frame, 1, 2,
            text = "9", feature = lambda: Button.insert_math("9")
        )

        # Multiply button
        buttons_frame.grid_rowconfigure(2, weight = 1)
        buttons_frame.grid_columnconfigure(3, weight = 1)
        mult_button = Button (
            buttons_frame, 2, 3,
            text = "*", feature = lambda: Button.insert_math("*")
        )

        # Four button
        buttons_frame.grid_rowconfigure(2, weight = 1)
        buttons_frame.grid_columnconfigure(0, weight = 1)
        four_button = Button (
            buttons_frame, 2, 0,
            text = "4", feature = lambda: Button.insert_math("4")
        )

        # Five button
        buttons_frame.grid_rowconfigure(2, weight = 1)
        buttons_frame.grid_columnconfigure(1, weight = 1)
        five_button = Button (
            buttons_frame, 2, 1,
            text = "5", feature = lambda: Button.insert_math("5")
        )

        # Six button
        buttons_frame.grid_rowconfigure(2, weight = 1)
        buttons_frame.grid_columnconfigure(2, weight = 1)
        six_button = Button (
            buttons_frame, 2, 2,
            text = "6", feature = lambda: Button.insert_math("6")
        )

        # Minus button
        buttons_frame.grid_rowconfigure(3, weight = 1)
        buttons_frame.grid_columnconfigure(3, weight = 1)
        minus_button = Button (
            buttons_frame, 3, 3,
            text = "-", feature = lambda: Button.insert_math("-")
        )

        # One button
        buttons_frame.grid_rowconfigure(3, weight = 1)
        buttons_frame.grid_columnconfigure(0, weight = 1)
        one_button = Button (
            buttons_frame, 3, 0,
            text = "1", feature = lambda: Button.insert_math("1")
        )

        # Two button
        buttons_frame.grid_rowconfigure(3, weight = 1)
        buttons_frame.grid_columnconfigure(1, weight = 1)
        two_button = Button (
            buttons_frame, 3, 1,
            text = "2", feature = lambda: Button.insert_math("2")
        )

        # Three button
        buttons_frame.grid_rowconfigure(3, weight = 1)
        buttons_frame.grid_columnconfigure(2, weight = 1)
        three_button = Button (
            buttons_frame, 3, 2,
            text = "3", feature = lambda: Button.insert_math("3")
        )

        # Add button
        buttons_frame.grid_rowconfigure(4, weight = 1)
        buttons_frame.grid_columnconfigure(3, weight = 1)
        add_button = Button (
            buttons_frame, 4, 3,
            text = "+", feature = lambda: Button.insert_math("+")
        )

        # Close bracket button
        buttons_frame.grid_rowconfigure(0, weight = 1)
        buttons_frame.grid_columnconfigure(3, weight = 1)
        close_button = Button (
            buttons_frame, 0, 3,
            text = ")", feature = lambda: Button.insert_math(")")
        )

        # Zero button
        buttons_frame.grid_rowconfigure(4, weight = 1)
        buttons_frame.grid_columnconfigure(1, weight = 1)
        zero_button = Button (
            buttons_frame, 4, 1,
            text = "0", feature = lambda: Button.insert_math("0")
        )

        # Dot button
        buttons_frame.grid_rowconfigure(4, weight = 1)
        buttons_frame.grid_columnconfigure(0, weight = 1)
        dot_button = Button (
            buttons_frame, 4, 0,
            text = ".", feature = lambda: Button.insert_math(".")
        )

        # Calc button
        buttons_frame.grid_rowconfigure(4, weight = 1)
        buttons_frame.grid_columnconfigure(2, weight = 1)
        calc_button = Button (
            buttons_frame, 4, 2,
            text = "=", feature = Calculator.do_the_math
        )

        self.window.mainloop()

# Entry point
main_window = MainWindow()