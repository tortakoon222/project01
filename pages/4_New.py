def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print("*" * width)
        else:
            print("*" + " " * (width - 2) + "*")

# กำหนดความกว้างและความสูงของกรอบสี่เหลี่ยม
width = 20
height = 10

# เรียกใช้ฟังก์ชันเพื่อวาดกรอบสี่เหลี่ยม
draw_rectangle(width, height)
