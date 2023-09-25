# Code understanding......to extend the code and apply recent understandings 

# List of metro city : (list used cause more cities can be added to it in future)
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
# Each metro city defined as a tuple to avoid modification in individual city('Ciity name','Country Symbol','I don't know What',(Lattitude, longitude))
def main():
    print(f'{"City":9} | {"latitude":9} | {"longitude":>9}')  # Header of the Table(:9 or :>9) is the string format specifier 
# :> means indented rightwards, :< means indented leftwards, : (default) is right indented
    for name, _, _, (lat, lon) in metro_areas:  # most important part of code which helps excecute the pattern matching with name,_,_,(lat,lon)
        if lon >= 0:                          # to screen out cities with longitude less than 0
            print(f'{name:9} | {lat:9.4f} | {lon:9.4f}') #(:9) is string format specifier (:9.4f)---9 specifies 9 spaces to be left for string formatting
# .4f- means long and lat to be printed upto 4 decimel points

if __name__ == '__main__':# __name__ returns the name of fountion which is ecectuded when code is run 
    print(f"__name__ returns: {__name__}\n")
    main() # above line  will return __main__ because the main founction is defined in the same module
# If we had impoted the main() fountion from a different file/module it would have returned the name of the file/module and printing in format won't be excecuted