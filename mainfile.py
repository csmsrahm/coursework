########################################
#        2024-4216COMP-Group17         #
########################################
########################################
#             Imports                  #
########################################
import pandas as pd 
import matplotlib.pyplot as plt  

########################################
#            Main Code                 #
########################################
#
# User Interface
menu = True

while menu:
    # Menu
    print("------------------Menu---------------------")
    print("Please select one of the following options:")
    print("A:- View Dataset A")
    print("B:- View Dataset B")
    print("C:- Questions regarding the datasets")
    print("D:- Exit")
    userChoice = input("Choose an option please: ").upper()

    # Dataset A (netflix_stock_dataset.csv) is read and then displayed
    if userChoice == "A":
        netflixData = pd.read_csv(r"C:\coursework-1\netflix_stock_dataset (1).csv")
        print(netflixData)
       # Plotting Netflix stock prices
        plt.plot(netflixData['Date'], netflixData['Close'])
        plt.title('Netflix Stock Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.show()


    # Dataset B (GOOG.csv) is read then displayed
    elif userChoice == "B":
        googleData = pd.read_csv(r"C:\coursework-1\GOOG (1).csv")
        print(googleData)
        # Plotting Google stock prices
        plt.plot(googleData['Date'], googleData['Close'])
        plt.title('Google Stock Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.xticks(rotation=45)
        plt.show()
          
        
        
    # Questions need deciding and implemented under this if statement
    elif userChoice == "C":
        print("------------------Questions---------------------")
        print("A:- Which stock saw the most change over the years?")
        print("B:- What was the highest and lowest price of stock over the years?")
        print("C:-")
        print("D:-")
        print("E:-")
        UserChoice2 = input("Choose a question please: ").upper()
        
        if UserChoice2 == "A":
            print(UserChoice2)

        elif UserChoice2 == "B":
            # Reads dataset A and puts contents into nData variable
            nData = pd.read_csv("C:\coursework-1\netflix_stock_dataset (1).csv")
            # Two variables store the rows containing the highest and lowest stock prices
            highPriceR = nData.loc[nData["Close"].idxmax()]
            lowPriceR = nData.loc[nData["Close"].idxmin()]
            #Extracts the Date of the highest price and the stock price
            highDate = highPriceR["Date"]
            highPrice = highPriceR["Close"]
            #Extracts the date of the lowest price and the stock price
            lowDate = lowPriceR["Date"]
            lowPrice = lowPriceR["Close"]
            #Outputs the date and prices of the highest and lowest stocks 
            print(f"The Highest Netflix stock price occured on {highDate} and was valued at £{highPrice}")
            print(f"The Lowest Netflix stock price occured on {lowDate} and was valued at £{lowPrice}")
            
            #Reads dataset B and puts contents into gData variable
            gData = pd.read_csv("C:\coursework-1\GOOG (1).csv")
            # Two variables store the rows containing the highest and lowest stock prices
            highPriceR = gData.loc[nData["Close"].idxmax()]
            lowPriceR = gData.loc[nData["Close"].idxmin()]
            #Extracts the Date of the highest price and the stock price
            highDate = highPriceR["Date"]
            highPrice = highPriceR["Close"]
            #Extracts the date of the lowest price and the stock price
            lowDate = lowPriceR["Date"]
            lowPrice = lowPriceR["Close"]
            #Outputs the date and prices of the highest and lowest stocks 
            print(f"The Highest Google stock price occured on {highDate} and was valued at £{highPrice}")
            print(f"The Lowest Google stock price occured on {lowDate} and was valued at £{lowPrice}")









    # elif statement allows the user to close the program through inputting "D" when prompted
    elif userChoice == "D":
        print("Thank you for using this program!")
        menu = False

    # Input Validation
    else:
        print("Input is invalid, please use one of the displayed options!")
        