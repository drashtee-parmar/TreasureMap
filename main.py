# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal_position = int(position[0]) # column
vertical_position = int(position[1])  # row

# print(map[vertical_position])
# print(map[3 - 1])


# selected_row = map[vertical_position -1]
# selected_row[horizontal_position - 1] = "X"

map[vertical_position - 1][horizontal_position -1] = "X"




#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

