"""
1. Напишіть програму, де клас «геометричні фігури» (Figure) містить
властивість color з початковим значенням white і метод для зміни кольору
фігури, а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи __init__ для 
завдання початкових розмірів об'єктів при їх створенні.
"""

class Figure:
    """
    A base class representing geometric figures.
    """
    def __init__(self):
        self.color = 'white'

    def change_color(self, new_color: str):
        """
        Changes the color of the figure to the specified color.
        """
        self.color = new_color

class Oval(Figure):
    """ 
    Сharacteristics of the "Oval". Accept two parameters: "Width" and "Height".
    The "Color" attribute is inherited from the superclass.
    """
    def __init__(self, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height

class Square(Figure):
    """
    A base class representing geometric figures.
    """
    def __init__(self, side_size: int):
        super().__init__()
        self.side_size = side_size


black_oval = Oval(width=25, height=30)
black_oval.change_color(new_color='Black')

blue_square = Square(side_size=10)
blue_square.change_color(new_color='Blue')


print(f"Oval color: {black_oval.color}\nOval width: {black_oval.width}\nOval height: {black_oval.height}", end='\n\n')
print(f"Square color: {blue_square.color}\nSquare side: {blue_square.side_size}")
