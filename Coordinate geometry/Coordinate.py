class Coordinate:
    def __init__ (self):
        print("Coordinate Geometry Calculator.")
        self.menu()
    def menu(self):
        print(""" 
1 : for-distance from origin.
2 : for-distance between two points.
3 : for-check point is on line or not.
4 : for-distance between line and point.
5 : for-Area of triangle △.
6 : for-Mid Point of line.
7 : for-Centroid of triangle △.
8 : for-Slope of Line.
9 : for-Exit. """)
        self.x = input("Your input from above option-- ")
        if self.x == "1":
            return self.origin()
        elif self.x == "2":
            return self.two_point_dist()
        elif self.x == "3":
            return self.check_on_line()
        elif self.x == "4":
            return self.line_distance()
        elif self.x == "5":
            return self.area_triangle()
        elif self.x == "6":
            return self.mid_point()
        elif self.x == "7":
            return self.centroid()
        elif self.x == "8":
            return self.slope()
        elif self.x == "9":
            return self.exit()
        else:
            return self.wrong()
    def origin(self):
        self.px,self.py = map(int,input("Give me x,y for your point--").split(","))
        result = round(((self.px)**2 + (self.py)**2)**0.5,2) 
        print(f"Distance between origin(0,0) and ({self.px},{self.py}) is {result}") 
        self.menu()

    def two_point_dist(self):
        self.px,self.py = map(int,input("Give me x,y for your first point--").split(","))
        self.x2,self.y2 = map(int,input("Give me x,y for Second point--").split(","))
        result = round(((self.px-self.x2)**2 + (self.py-self.y2)**2)**0.5,2)
        print(f"Distance between ({self.x2},{self.y2}) and ({self.px},{self.py}) is {result}")
        self.menu()

    def check_on_line(self):
        self.px,self.py = map(int,input("Give me x,y for your point--").split(","))
        print("Give input according to aX + bY + C = 0")
        self.lx,self.ly,self.lc = map(int,input("Give me cooficient of X and Y and Constaint C in this way a,b,c --").split(","))
        result = self.px*self.lx + self.py*self.ly + self.lc
        if result == 0:
            print(f"point ({self.px},{self.py}) is on line!")
        else:
            print(f"point ({self.px},{self.py}) is not on line!")
        self.menu()

    
    def line_distance(self):
        self.px,self.py = map(int,input("Give me x,y for your point--").split(","))
        print("Give input according to aX + bY + C = 0")
        self.lx,self.ly,self.lc = map(int,input("Give me cooficient of X and Y and Constaint C in this way a,b,c --").split(","))
        result = abs(round((self.px*self.lx + self.py*self.ly + self.lc)/(self.lx**2 +self.ly**2)**0.5,2))
        print(f"Distance between point ({self.px},{self.py}) and line is {result}")
        self.menu()

    
    def slope(self):
        self.x1,self.y1 = map(int,input("Give me x,y for your first point--").split(","))
        self.x2,self.y2 = map(int,input("Give me x,y for your second point--").split(","))
        if (self.x2-self.x1) == 0:
            print("Your Denominator is Zero.Give Right Coordinate Point")
            self.menu()
        else:
            rs = round(((self.y2 - self.y1)/(self.x2-self.x1)),2)
            print(f"Slope of line is {rs}")
            self.menu()

    def area_triangle(self):
        self.x1,self.y1 = map(int,input("Give me x,y for your first point--").split(","))
        self.x2,self.y2 = map(int,input("Give me x,y for your second point--").split(","))
        self.x3,self.y3 = map(int,input("Give me x,y for your third point--").split(","))
        result = round(abs(0.5*(self.x1*(self.y2-self.y3)+self.x2*(self.y3-self.y1)+self.x3*(self.y1-self.y2))),2)
        print(f"Area of triangle △ is {result}")
        self.menu()

    def mid_point(self):
        self.x1,self.y1 = map(int,input("Give me x,y for your first point--").split(","))
        self.x2,self.y2 = map(int,input("Give me x,y for your second point--").split(","))
        rx = round((self.x1 + self.x2)/2,2)
        ry = round((self.y1 + self.y2)/2,2)
        print(f"Mid point of line is ({rx},{ry})")
        self.menu()
        
    def centroid(self):
        self.x1,self.y1 = map(int,input("Give me x,y for your first point--").split(","))
        self.x2,self.y2 = map(int,input("Give me x,y for your second point--").split(","))
        self.x3,self.y3 = map(int,input("Give me x,y for your third point--").split(","))
        rx= round((self.x1 + self.x2 + self.x3)/3,2)
        ry= round((self.y1 + self.y2+self.y3)/3,2)
        print(f"Centroid of triangle △ is ({rx},{ry})")
        self.menu()

    def exit(self):
        print("Thank you for using coordinate geometry calculator !!!")
        exit()
    def wrong(self):
        print("Please Enter Valid Input !!")
        self.menu()

a = Coordinate()


