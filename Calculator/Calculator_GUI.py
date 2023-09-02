import tkinter

class Calculator:
  def __init__(self):
    self.window = tkinter.Tk()
    self.window.title("Calculator")
    self.main_frame = tkinter.Frame(self.window)
    self.main_frame.pack()

    self.display = tkinter.Entry(self.main_frame, font=('Arial', 22))
    self.display.grid(row=1, column=1, columnspan=4)
    self.display.config(state='disabled')

    button_configs = [
      ('C', 2, 1, self.clear),
      ('E', 2, 2, self.erase),
      ('%', 2, 3, lambda: self.add_to_display('%')),
      ('÷', 2, 4, lambda: self.add_to_display('÷')),
      ('7', 3, 1, lambda: self.add_to_display('7')),
      ('8', 3, 2, lambda: self.add_to_display('8')),
      ('9', 3, 3, lambda: self.add_to_display('9')),
      ('x', 3, 4, lambda: self.add_to_display('x')),
      ('4', 4, 1, lambda: self.add_to_display('4')),
      ('5', 4, 2, lambda: self.add_to_display('5')),
      ('6', 4, 3, lambda: self.add_to_display('6')),
      ('-', 4, 4, lambda: self.add_to_display('-')),
      ('1', 5, 1, lambda: self.add_to_display('1')),
      ('2', 5, 2, lambda: self.add_to_display('2')),
      ('3', 5, 3, lambda: self.add_to_display('3')),
      ('+', 5, 4, lambda: self.add_to_display('+')),
      ('', 6, 1, self.shift),
      ('0', 6, 2, lambda: self.add_to_display('0')),
      ('.', 6, 3, lambda: self.add_to_display('.')),
      ('=', 6, 4, self.calculate)
      ]

    buttons = []

    for label, row, column, command in button_configs:
      button = tkinter.Button(self.main_frame, text=label, command=command)
      button.grid(row=row, column=column)
      buttons.append(button)

    for button in buttons:
      button.config(width=10, height=2)
    self.window.mainloop()

  def add_to_display(self, value):
    self.display.config(state='normal')
    current_text = self.display.get()

    if value == '%':
      operators = ['+', '-', 'x', '÷']
      if current_text and (current_text[-1] in operators or current_text[-1] == '%'):
        return

      if current_text and current_text[-1].isdigit():
        next_text = current_text + value
      else:
        return
    else:
      next_text = current_text + value

    self.display.delete(0, tkinter.END)
    self.display.insert(tkinter.END, next_text)
    self.display.config(state='disabled')


  def clear(self):
    self.display.config(state='normal')
    self.display.delete(0, tkinter.END)
    self.display.config(state='disabled')

  def erase(self):
    current_text = self.display.get()
    new_text = current_text[:-1]
    self.display.config(state='normal')
    self.display.delete(0, tkinter.END)
    self.display.insert(tkinter.END, new_text)
    self.display.config(state='disabled')

  def shift(self):
    pass

  def calculate(self):
    expression = self.display.get()
    try:
      expression = expression.replace('x', '*')
      expression = expression.replace('÷', '/')
      expression = expression.replace('%', '/100')
      result = eval(expression)
      self.display.config(state='normal')
      self.display.delete(0, tkinter.END)
      self.display.insert(tkinter.END, str(result))
      self.display.config(state='disabled')
    except Exception as e:
      self.display.delete(0, tkinter.END)
      self.display.insert(tkinter.END, "Error")


interface = Calculator()

