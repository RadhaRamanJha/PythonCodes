class patterns:

    def pattern_choice(defaultchoice):
    # def pattern_choice(choice = " "):
                           
        if defaultchoice == True :
            choice = defaultchoice
            
        else:
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
                11. hollow_mxn_star_rectangle
                12. hollow_square_without_top
                13. square_ladder_with_top_and_bottom
                14. pyramid
                15. diamomd
                16. inverted_pyramid
                17. big_ladder
                18. v_pattern
                19. dumroo_pattern''')
    
            choice = int(input("Enter your choice: "))
        
        print(choice)
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
        elif choice == 12:
            patterns.hollow_square_without_top()
        elif choice == 13:
            patterns.square_ladder_with_top_and_bottom()
        elif choice == 14:
            patterns.pyramid()
        elif choice == 15:
            patterns.diamond()
        elif choice == 16:
            patterns.inverted_pyramid()
        elif choice == 17:
            patterns.big_ladder()
        elif choice == 18:
            patterns.v_pattern()
        elif choice == 19:
            patterns.dumroo_pattern()
            
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
            if (i==1)or (i==rows):
                print(" X "*columns)
            else:
                for j in range (1,columns+1):
                    if(j==1) or (j==columns):
                        print(" X ",end="")
                    else:
                        print("   ",end="")

    def hollow_square_without_top():
        stars_per_side = int(input("Enter the total number of stars desired per side of square: "))
        for row in range(1,stars_per_side+1):
            if (row == stars_per_side):
                print("* "*stars_per_side)
            else:
                for column in range(1,stars_per_side+1):
                    if (column == 1 or column == stars_per_side ):
                        print("*",end=" ")
                    # elif (column == stars_per_side):
                    #    print("*",end=" ")
                    else:
                        print(" ",end=" ")
            print()
        
    def square_ladder_with_top_and_bottom():
        num_of_stars_at_each_step_of_ladder = int(input("Enter the number of '*' at each step of ladder: "))
        for row in range (1,num_of_stars_at_each_step_of_ladder+1):
            if (row%2 != 0):
                print("* "*num_of_stars_at_each_step_of_ladder,end="")
            elif ( row%2 == 0):
                for column in range (1,num_of_stars_at_each_step_of_ladder+1):
                    if (column == 1) or ( column == num_of_stars_at_each_step_of_ladder):
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
            print()

    def pyramid():
        num_o_star_at_base = int(input("Enter the total number of '*' at base: "))
        for row in range(1,num_o_star_at_base+1):
            front_space = " "*(num_o_star_at_base-row)
            seprator_pattern = "* "*row
            print(front_space,seprator_pattern)
    

    def diamond(): 
        maximum_stars_in_line = int(input("The postion of line having maximum stars: "))
        for line in range(0,maximum_stars_in_line + 1):
            front_space = " "*(maximum_stars_in_line-line)
            seprator_pattern = "*"*(2*line-1)
            ender = " "
            print(front_space,seprator_pattern,ender)
            print()
        end_line = 2*maximum_stars_in_line-1
        for line in range(maximum_stars_in_line,end_line+1):
            front_space = " "*(line-(maximum_stars_in_line-1))
            seprator_space = end_line - line
            seprator_pattern = "*"*(2*seprator_space-1)
            ender = " "
            print(front_space,seprator_pattern,ender)
            print()

    def inverted_pyramid():
        no_stars_in_first_line = int(input("Enter the number of stars in first line : "))
        for line in range(no_stars_in_first_line,0,-2):
            front_space = " "*int((no_stars_in_first_line-line)/2)
            pattern = "*"*line
            print(front_space,pattern)


    def big_ladder():
        m = int(input("Enter the number of Tab seperated star in first line: "))
        n = int(input("Enter the total number of lines: "))
        for line in range (1,n+1):
            if line % 3 == 1:
                for stars_per_line in range(1,m+1):
                    print("*",end=" ")
                print()
            else:
                for stars_per_line in range(1,m+1):
                    if ((stars_per_line == 1) or (stars_per_line == m)):
                        print("*",end= " ")
                    else:
                        print(" ",end=" ")
                print()

    def v_pattern():
        m = int(input("Enter the number of characters in first row: "))
        if (m%2) == 0 :
            print("V-Pattern cannont be drawn for Even Numbers")
        else:
            for row in range (1,(m+1)//2+1):
                last_position_of_star = m-row+1
                if(row<last_position_of_star):
                    for column in range(1,m+1):            
                        if(column == row) or (column == last_position_of_star):
                            print("*",end=" ")
                        else:
                            print(" ",end=" ")
                elif(row == m//2+1):
                    print("  "*int(m//2), end="*")
                print()

    def dumroo_pattern(): # to edit
        m = int(input("Enter the number of characters in first row: "))
        if (m%2) == 0 :
            print("dumroo_attern cannont be drawn for Even Numbers")
        else:
            for row in range (1,m+1,2):
                last_position_of_star = m-row+1
                for column in range(row,last_position_of_star+1):            
                    print("*",end=" ")
                    if(row == m//2+1):
                        print("  "*int(m//2), end="*")
                print()
                for row in range (1,m+1,2):
                    last_position_of_star = m-row+1
                    for column in range(row,last_position_of_star+1):            
                        print("*",end=" ")
                    print()
                


                

patterns.pattern_choice()
# patterns.hollow_mxn_star_rectangle()