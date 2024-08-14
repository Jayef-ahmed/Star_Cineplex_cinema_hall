class Star_Cinema:
    __hall_list = []
    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)



class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        self.entry_hall(self)


    def entry_show(self, id, movie_name, time):
        mov = (id, movie_name, time)
        self.__show_list.append(mov)
        lst = [[0 for i in range(self.cols)]for j in range(self.rows)]
        self.__seats[id]=lst

    def book_seats(self, mov_id, seat_no):
        if mov_id in self.__seats:
            row, col = seat_no
            if row>=0 and row<self.rows and col>=0 and col<self.cols:
                if self.__seats[mov_id][row][col] == 0:
                    self.__seats[mov_id][row][col] = 1
                    print(f'seat ({row}, {col}) booked for show {mov_id}')
                else:
                    print("Seat is already Booked")
            else:
                print("Invalid Seat")

        else:
            print("Movie id is Invalid")

    def view_show_list(self):
        for shows in self.__show_list:
            id,name,time = shows
            print(f'MOVIE NAME:{name}({id}) SHOW ID:{id} TIME:{time}')

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            for st in self.__seats[show_id]:
                print(st)
        else:
            print("Invalid! Please Enter a valid Id")


Star_Cineplex = Hall(7,6,5)

Star_Cineplex.entry_show(111,'Deadpool & Wolverine','15/08/24 5:00 PM')
Star_Cineplex.entry_show(222,'Toffan','15/08/24 4:30 PM')
Star_Cineplex.entry_show(333,'Dune','15/08/24 4:00 PM')

while True:

    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEAT')
    print('3. BOOK TICKET')
    print('4. Exit')

    op = int(input('ENTER OPTION: '))

    if op == 1:
        print('------------')
        Star_Cineplex.view_show_list()
        print('------------')

    elif op == 2:
        id = int(input('ENTER SHOW ID: '))
        print('----------------')
        Star_Cineplex.view_available_seats(id)
        print('----------------')

    elif op == 3:
        id = int(input('ENTER SHOW ID: '))
        row = int(input('ENTER SEAT ROW: '))
        col = int(input('ENTER SEAT COL: '))
        print('----------------')
        Star_Cineplex.book_seats(id,(row,col))
        print('----------------')

    elif op == 4:
        break