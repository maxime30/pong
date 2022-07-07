from microbit import *
import speech

paddle_x = 2
paddle_y = 4
paddle_length = 2


ball_x = 2
ball_y = 0
ball_length = 1


display.scroll('Hello', wait=False)
speech.say('Hello')

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        break

for i in range(paddle_length):
    display.set_pixel(paddle_x + i, paddle_y, 9)

display.set_pixel(ball_x, ball_y, 9)
sleep(500)

while True:
    while ball_y < 4:
        if button_b.was_pressed() and paddle_x < 3:
            paddle_x += 1
            display.clear()

        if button_a.was_pressed() and paddle_x > 0:
            paddle_x -= 1
            display.clear()

        display.clear()

        for i in range(paddle_length):
            display.set_pixel(paddle_x + i, paddle_y, 9)

        if ball_x in range(paddle_x, paddle_x + paddle_length) and ball_y == 3:
            break

        ball_y += 1
        display.set_pixel(ball_x, ball_y, 9)
        sleep(500)

    if ball_y == 4:
        break

    while ball_y > 0:
        if button_b.was_pressed() and paddle_x < 3:
            paddle_x += 1
            display.clear()

        if button_a.was_pressed() and paddle_x > 0:
            paddle_x -= 1
            display.clear()
        display.clear()
        for i in range(paddle_length):
                 display.set_pixel(paddle_x + i, paddle_y, 9)
        ball_y -= 1
        display.set_pixel(ball_x, ball_y, 9)
        sleep(500)


# game over
display.clear()
display.show(Image.SAD)


