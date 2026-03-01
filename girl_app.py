import turtle
import tkinter as tk
import math

def draw_girl():
    t.clear()
    t.speed(4)

    # --- Skin color ---
    skin = "peachpuff"

    # ================= HEAD =================
    t.penup()
    t.goto(0, 140)
    t.pendown()
    t.color("black", skin)
    t.begin_fill()
    t.circle(45)
    t.end_fill()

    # ================= EYES =================
    for x in (-18, 18):
        t.penup()
        t.goto(x, 165)
        t.pendown()
        t.color("black", "white")
        t.begin_fill()
        t.circle(6)
        t.end_fill()

        t.penup()
        t.goto(x, 168)
        t.pendown()
        t.color("black")
        t.circle(2)

    # ================= SHY SMILE =================
    t.penup()
    t.goto(-15, 145)
    t.setheading(-40)
    t.pendown()
    t.circle(25, 90)

    # ================= BINDI =================
    t.penup()
    t.goto(0, 162)
    t.color("red")
    t.begin_fill()
    t.circle(3)
    t.end_fill()

    # ================= NOSE RING =================
    t.penup()
    t.goto(15, 150)
    t.color("gold")
    t.circle(4, 200)

    # ================= EARRINGS =================
    for x in (-35, 35):
        t.penup()
        t.goto(x, 140)
        t.pendown()
        t.color("gold")
        t.circle(6)

    # ================= HAIR (LONG WAVY) =================
    t.color("black", "saddlebrown")
    t.penup()
    t.goto(-45, 185)
    t.pendown()
    t.begin_fill()
    for i in range(200):
        t.forward(1)
        t.right(0.9)
    t.goto(45, 185)
    for i in range(200):
        t.forward(1)
        t.right(0.9)
    t.goto(-45, 185)
    t.end_fill()

    # ================= FLOWER IN HAIR =================
    t.penup()
    t.goto(-30, 170)
    t.color("white")
    for _ in range(6):
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.left(60)

    # ================= BODY (DREAMY TILT) =================
    t.penup()
    t.goto(5, 140)
    t.setheading(-95)
    t.pendown()
    t.color("black")
    t.forward(70)

    # ================= RED SAREE =================
    t.color("black", "red")
    t.begin_fill()
    t.left(35)
    t.forward(80)
    t.right(85)
    t.forward(160)
    t.right(95)
    t.forward(80)
    t.end_fill()

    # ================= SAREE PALLU =================
    t.color("darkred")
    t.penup()
    t.goto(-20, 90)
    t.setheading(210)
    t.pendown()
    t.begin_fill()
    t.forward(110)
    t.left(50)
    t.forward(90)
    t.left(100)
    t.forward(120)
    t.end_fill()

    # ================= LEGS =================
    t.color("black")
    for x in (-15, 15):
        t.penup()
        t.goto(x, 20)
        t.setheading(-90)
        t.pendown()
        t.forward(60)

    # ================= ARMS =================
    t.penup()
    t.goto(-45, 100)
    t.setheading(200)
    t.pendown()
    t.forward(60)

    t.penup()
    t.goto(45, 100)
    t.setheading(-10)
    t.pendown()
    t.forward(60)

# ===== GUI WINDOW =====
root = tk.Tk()
root.title("Dreamy Girl Art 💖")

canvas = turtle.ScrolledCanvas(root, width=520, height=520)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
t.hideturtle()

btn = tk.Button(root, text="Draw Her ✨", font=("Arial", 14), command=draw_girl)
btn.pack(pady=10)

root.mainloop()
