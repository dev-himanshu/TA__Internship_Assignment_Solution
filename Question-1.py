# 1- Print the following patterns with a py script -
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
def half_right_side_pyramid(rows):
    for row in range(1, rows + 1):
        for space in range(row, rows):
            print(" ", end=" ")
        for star in range(row):
            print("*", end=" ")
        print()


# A
# B C
# D E F
# G H I J
# K L M N O
def half_left_side_pyramid_of_alphabet(rows):
    character = 65
    for row in range(1, rows + 1):
        for col in range(row):
            print(chr(character), end=" ")
            character += 1
        print()


if __name__ == "__main__":
    while True:
        choice = int(input(
            "1. Half Right Pyramid Of Star.\n2. Half Left Pyramid Of Alphabet.\n3. Exit.\nEnter Your Choice : "))
        if choice == 1:
            half_right_side_pyramid(int(input("Enter number of rows: ")))
        elif choice == 2:
            half_left_side_pyramid_of_alphabet(int(input("Enter number of rows for alphabet pyramid: ")))
        elif choice == 3:
            exit("Good Bye!!!")
        else:
            print("!!! Wrong Input Selection.\n")
