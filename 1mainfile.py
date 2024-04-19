########################################
#        2024-4216COMP-Group17         #
########################################
########################################
#             Imports                  #
########################################
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Define file paths using raw strings
netflix_file_path = r"C:\coursework-1\netflix_stock_dataset (1).csv"
google_file_path = r"C:\coursework-1\GOOG (1).csv"

# Read the first dataset (Netflix)
netflixData = pd.read_csv(netflix_file_path)

# Read the second dataset (Google)
googleData = pd.read_csv(google_file_path)

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

    # Dataset A (Netflix) is read and then displayed
    if userChoice == "A":
        print(netflixData)
        # Plotting Netflix stock prices
        plt.plot(netflixData['Date'], netflixData['Close'])
        plt.title('Netflix Stock Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')

        # Customize x-axis to improve date visibility
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())  # Auto date locator
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format date labels as Year-Month
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.show()

    # Dataset B (Google) is read then displayed
    elif userChoice == "B":
        print(googleData)
        # Plotting Google stock prices
        plt.plot(googleData['Date'], googleData['Close'])
        plt.title('Google Stock Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Price')

        # Customize x-axis to improve date visibility
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())  # Auto date locator
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format date labels as Year-Month
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.show()
        
    # Questions section
    elif userChoice == "C":
        print("------------------Questions---------------------")
        print("A:- Which stock saw the most change over the years?")
        print("B:- What was the highest and lowest price of stock over the years?")
        print("C:- Compare the average trading volume of Netflix and Google stocks")
        print("D:- Stock volume per company over the years")
        userChoice2 = input("Choose a question please: ").upper()

        # Question A: Which stock saw the most change over the years?
        if userChoice2 == "A":
            try:
                # Calculate the total change in 'Open' prices for each dataset
                changes1 = netflixData['Open'].diff().abs().sum()
                changes2 = googleData['Open'].diff().abs().sum()

                # Plotting the bar chart
                plt.bar(['Netflix', 'Google'], [changes1, changes2])
                plt.xlabel('Stock')
                plt.ylabel('Total Change in Open Price')
                plt.title('Total Change in Open Price for Netflix and Google')
                plt.show()

                # Comparing the total change and printing the result
                if changes1 > changes2:
                    print(f"Netflix saw the most change in 'Open' prices with a total change of {changes1}.")
                elif changes1 < changes2:
                    print(f"Google saw the most change in 'Open' prices with a total change of {changes2}.")
                else:
                    print("Both Netflix and Google have the same amount of change.")
            except KeyError:
                print("Error: 'Open' column not found in the dataset.")

        # Question B: What was the highest and lowest price of stock over the years?
        elif userChoice2 == "B":
            try:
                # Highest and lowest prices and corresponding dates for Netflix
                n_highest_price_row = netflixData.loc[netflixData["Close"].idxmax()]
                n_lowest_price_row = netflixData.loc[netflixData["Close"].idxmin()]

                # Highest and lowest prices and corresponding dates for Google
                g_highest_price_row = googleData.loc[googleData["Close"].idxmax()]
                g_lowest_price_row = googleData.loc[googleData["Close"].idxmin()]

                # Extract highest and lowest prices and their corresponding dates for Netflix
                n_highest_price = n_highest_price_row["Close"]
                n_highest_date = n_highest_price_row["Date"]
                n_lowest_price = n_lowest_price_row["Close"]
                n_lowest_date = n_lowest_price_row["Date"]

                # Extract highest and lowest prices and their corresponding dates for Google
                g_highest_price = g_highest_price_row["Close"]
                g_highest_date = g_highest_price_row["Date"]
                g_lowest_price = g_lowest_price_row["Close"]
                g_lowest_date = g_lowest_price_row["Date"]

                # Plotting
                plt.figure(figsize=(10, 6))
                plt.plot(netflixData["Date"], netflixData["Close"], label="Netflix Stock Price")
                plt.plot(googleData["Date"], googleData["Close"], label="Google Stock Price")

                # Mark Netflix prices in red
                plt.scatter(n_highest_date, n_highest_price, color='red', label=f'Highest Netflix Price: £{n_highest_price}', zorder=5)
                plt.scatter(n_lowest_date, n_lowest_price, color='red', label=f'Lowest Netflix Price: £{n_lowest_price}', zorder=5)

                # Mark Google prices in red
                plt.scatter(g_highest_date, g_highest_price, color='red', label=f'Highest Google Price: £{g_highest_price}', zorder=5)
                plt.scatter(g_lowest_date, g_lowest_price, color='red', label=f'Lowest Google Price: £{g_lowest_price}', zorder=5)

                # Adding labels and title
                plt.title('Stock Prices with Highest and Lowest Points Marked')
                plt.xlabel('Date')
                plt.ylabel('Stock Price (£)')
                plt.xticks(rotation=45)
                plt.legend()
                plt.grid(True)

                # Show plot
                plt.tight_layout()
                plt.show()
            except ValueError:
                print("Error: Close column not found in the dataset.")

        # Question C: Compare the average trading volume of Netflix and Google stocks
        elif userChoice2 == "C":
            # Compare the average trading volume of Netflix and Google stocks
            netflix_avg_volume = netflixData['Volume'].mean()
            google_avg_volume = googleData['Volume'].mean()

            print(f"The average trading volume of Netflix stock is {netflix_avg_volume:.2f}")
            print(f"The average trading volume of Google stock is {google_avg_volume:.2f}")

            # Plotting the bar chart
            plt.bar(['Netflix', 'Google'], [netflix_avg_volume, google_avg_volume])
            plt.xlabel('Stock')
            plt.ylabel('Average Trading Volume')
            plt.title('Average Trading Volume of Netflix and Google Stocks')
            plt.show()

            if netflix_avg_volume > google_avg_volume:
                print("Netflix has a higher average trading volume compared to Google.")
            elif netflix_avg_volume < google_avg_volume:
                print("Google has a higher average trading volume compared to Netflix.")
            else:
                print("Netflix and Google have the same average trading volume.")

        # Question D: Stock volume per company over the years
        elif userChoice2 == "D":
            # Plotting stock volume per company over the years
            plt.figure(figsize=(15, 10))
            plt.plot(netflixData['Date'], netflixData['Volume'], label='Netflix Stock Volume')
            plt.plot(googleData['Date'], googleData['Volume'], label='Google Stock Volume')

            # Adding labels and title
            plt.title('Stock Volume per Company Over the Years')
            plt.xlabel('Date')
            plt.ylabel('Volume')
            plt.legend()
            plt.xticks(rotation=45)
            plt.show()

    # Exit the program
    elif userChoice == "D":
        print("Thank you for using this program!")
        menu = False

    # Input validation
    else:
        print("Input is invalid, please use one of the displayed options!")
