invoice = """
....4..................23................................56................73..................92.....................
....P1003              Mortrola E18                      10                420                 4200
....P1000              NOKIA 3220                        12                199.99              23899.88
....P1004              Non-TaxableItem                   5                 500.0               1000.00
....P1002              It is a Service                   3.2               255.52              817.66
....P10006             Mortrola V3 Razor Black           10                500                 5000.00 """
ProductID = slice(4,9)  # slice(x,y) :- x,y used for horizontal slicing 
Product_Description = slice(23,46)
Quantity = slice(56,59)
Unit_price = slice(73,78)
Item_Total = slice(92,None)
line_items = invoice.split("\n")[2:] # line_items are indexed vertically and '2:' is instructing python to start slicing from 2nd vertical line  
for item in line_items:
    print(f"The Product Description and Unit Price of item {item[ProductID]}: ")
    print(item[Product_Description],item[Unit_price])
    print(f"Total Price of {item[Quantity]} {item[Product_Description]} is {item[Item_Total]} Dollars\n")