import sqlMovies
option = ""

# Displays menu for input as long as the user doesn't press 'q'
while option != "q":
    option = input("1. Create table\n 2. Insert Row\n 3. Update Row\n "
                   "4. Delete Row\n 5. Display All Rows\n 6. Display Single Row\n Or enter q to quit\n")
    if option == '1':
        # Creates Table
        sqlMovies.CreateMovieTable()

    elif option == '2':
        # Inserts new row and collects the input from user
        name = input("Enter Name: ")
        length = input("Enter Movie Length In Minutes: ")
        director = input("Enter Director: ")
        writer = input("Enter Writer: ")
        lead = input("Enter Lead Actor: ")
        releaseDate = input("Enter Original Theatrical Release: ")

        sqlMovies.AddNewRow(name, length, director, writer, lead, releaseDate)

    elif option == '3':
        # Updates row but displays the table first to allow user to look for what they want to change
        sqlMovies.DisplayTable()

        column = input('enter column name you want to update: ')
        newValue = input('Enter New Value: ')
        ID = input('Enter Id of row you want to update: ')

        sqlMovies.UpdateRow(column, newValue, ID)

    elif option == '4':
        # Displays table so user can find id of row they want to delete
        sqlMovies.DisplayTable()

        ID = input('Enter Id Of Row You Want To Delete: ')
        sqlMovies.DeleteRow(ID)

    elif option == '5':
        sqlMovies.DisplayTable()

    elif option == '6':
        ID = input('Enter Id Of Row You Want To See: ')
        sqlMovies.DeleteRow(ID)

    elif option == 'q':
        # quits program and displays table
        print('Goodbye!')
        sqlMovies.CloseDatabase()

    else:
        print(option + " is not a valid option.")