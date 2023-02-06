class patterns:

    def pattern_choice():

        print('''Select the founction numeral to be excecuted:-
            1. stars_in_same_line
            2. nxm_star_rectangle
            3. mirror_right_angled_triangle
            4. mirror_right_angled_triangle_of_whole_number
            5. inverted_right_angled_pattern
            6. right-angled triangle pattern
            7. right_angled_triangle_from_number_1ton
            8. mirror_right_angled_triangle_of_whole_number
            9. inverted_right_angled_triangle_of_whole_number
            10. right_triangles_of_5multiples
            11. hollow_mxn_star_rectangle''')

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
        elif choice == 7:
            patterns.right_angled_triangle_from_number_1ton()
        elif choice == 8:
            patterns.mirror_right_angled_triangle_of_whole_number()
        elif choice == 9:
            patterns.inverted_right_angled_triangle_of_whole_number()
        elif choice == 10:
            patterns.right_triangles_of_5multiples()
        elif choice == 11:
            patterns.hollow_mxn_star_rectangle()
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
    
    def right_angled_triangle_from_number_1ton():
        n = int(input("Enter the maximum integer to print: "))
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j, end="")
            print()
    
    def mirror_right_angled_triangle_of_whole_number():
        n = int(input("Enter the maximum integer to print: "))
        for i in range(0,n+1):
            print(" "*(n-i),end="")
            for j in range(1,i+1):
                print(j, end="")
            print()

    def inverted_right_angled_triangle_of_whole_number():
        n = int(input("Enter the maximum integer to be printed on 1st line: "))
        for i in range(1,n+1):
            for j in range(1 , n-i+2):
                print(j,end="")
            print()
    
    def right_triangles_of_5multiples():
        n = int(input("Enter the maximum number of multiples to display per line: "))
        for i in range(1,n+2):
            for j in range(1,i):
                print(5*j,end="  ")
            print()
    
    def hollow_mxn_star_rectangle():
        columns = int(input("Enter the number of columns: "))
        rows = int(input("Enter the number of rows: "))
        for i in range(1,rows+1):
            if (i==1):
                print(" X "*columns)
            elif(i==rows):
                print(" X "*columns)
            else:
                for j in range (1,columns+1):
                    if(j==1):
                        print(" X ",end="")
                    elif(j==columns):
                        print(" X ",end="")
                    else:
                        print("   ",end="")
                print()
patterns.pattern_choice()
# patterns.hollow_mxn_star_rectangle()