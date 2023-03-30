import turtle
import time


# Saat çerçevesinin çizim fonksiyonu
def draw_clock_frame(radius):
    # Analog saat için çember çiz.
    frame = turtle.Turtle()
    frame.penup()
    frame.goto(0, -radius)
    frame.pendown()
    frame.circle(radius)

    # Çember boyunca yarıçapın %20'si uzunluğunda 12 adet cizgi çiz.
    for i in range(12):
        frame.penup()
        frame.goto(0, 0)
        frame.right(30)
        frame.forward(radius * 0.8)
        frame.pendown()
        frame.forward(radius * 0.2)
        frame.penup()

# Saat, dakika ve saniye kolunun çizim fonksiyonu
def draw_hands(thickness, length, color):
    hand = turtle.Turtle()
    hand.speed(0)
    hand.shape("arrow")
    hand.color(color)
    hand.shapesize(thickness, length, thickness)
    hand.penup()
    hand.goto(0, 0)
    hand.pendown()

    return hand

def main():

    draw_clock_frame(200)
    hour_hand = draw_hands(1, 10, "black")
    minute_hand = draw_hands(0.5, 13,"black")
    second_hand = draw_hands(0.3, 14, "red")

    while True:
        # Zaman bilgisini al
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        second = current_time.tm_sec

        # Saat ibrelerini ayarla
        hour_hand.setheading(90 - (30 * hour + minute / 2))
        minute_hand.setheading(90 - (6 * minute))
        second_hand.setheading(90 - (6 * second))

        turtle.update()

        time.sleep(1)

        # Saat ibrelerini temizle
        hour_hand.clear()
        minute_hand.clear()
        second_hand.clear()


if __name__ == "__main__":
    main()
