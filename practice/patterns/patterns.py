class patterns:

    def pattern_choice():
        print('''Select the founction to be excecuted:-
            1. stars_in_same_line
            2. nxm_star_rectangle
            3. mirror_right_angled_triangle
            4. mirror_right_angled_triangle_of_whole_number
            5. inverted_right_angled_pattern
            6. right-angled triangle pattern''')

        choice = int(input("Enter your choice: "))
        if choice == 1:
            patterns.stars_in_same_line()
        elif choice == 2:
            patterns.nxm_star_rectangle()
        elif choice == 3:
            patterns.mirror_right_angled_triangle()
        elif choice == 4:
            patterns.mirror_right_angled_triangle_of_whole_number()
        elif choice == 5:
            patterns.inverted_right_angled_pattern()
        elif choice == 6:
            patterns.right_angled_triangle_pattern()
        else:
            print("Entered Choice not available")

    def stars_in_same_line():
        n = int(input("Enter the number of stars to print in same line: "))
        print("*"*n)

    def nxm_star_rectangle():
        n = int(input("Enter the number of stars per line: "))
        m = int(input("Enter the number of number of line: "))
        for i in range (0,m):
            print("*"*n)

    def mirror_right_angled_triangle():
        n = int(input("Enter the maximum number of stars per line: "))
        for i in range (0,n+1):
            j = n-i
            print(" "*j, end= "")
            print("*"*i)

    def mirror_right_angled_triangle_of_whole_number():
        n = int(input("Enter the maximum integer to print: "))
        for i in range(0,n+1):
            print(" "*(n-i),end="")
            for j in range(1,i+1):
                print(j, end="")

    def inverted_right_angled_pattern():
        n = int(input("Enter the number of stars in first line: "))
        for i in range (n,0,-1):
            print("*"*i)
    
    def right_angled_triangle_pattern():
        n = int(input("Enter the number of stars in last line: "))
        for i in range (0,n+1):
            print("*"*i)
patterns.pattern_choice()