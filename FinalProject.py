import pandas as pd


def get_average(data):
    total = 0
    for x in data:
        total += x
    average = total / len(data)
    return average


def read_data(path):
    data_path = path
    sales = pd.read_csv(data_path)
    return sales


def get_total_sales(monthly):
    monthly_sales = monthly
    total_sales = 0
    for x in monthly_sales:
        total_sales += x
    return total_sales


def get_highest(data):
    high = 0
    for x in data:
        if x > high:
            high = x
    return high


def get_lowest(data):
    low = 10000
    for x in data:
        if x < low:
            low = x
    return low


def get_monthly_dictionary(data, months):
    monthly_dictionary = {}
    for i in range(len(data)):
        monthly_dictionary[data[i]] = months[i]
    return monthly_dictionary


def calculate_percentage_change(a, b):
    change = b - a
    percentage_change = change / a * 100
    return percentage_change


def get_monthly_change(data, months):
    change_dictionary = {}
    for i in range(len(data)):
        if i < len(data) - 1:
            p_change = calculate_percentage_change(data[i], data[i+1])
            change_dictionary[months[i]] = str(round(p_change, 2)) + '%'
    return change_dictionary


def get_highest_lowest(monthly_sales, months):
    highest = get_highest(monthly_sales)
    lowest = get_lowest(monthly_sales)
    # print("Highest: {}, Lowest: {}".format(highest, lowest))
    monthly_dictionary = get_monthly_dictionary(monthly_sales, months)
    print(monthly_dictionary)
    highest_month = monthly_dictionary[highest]
    lowest_month = monthly_dictionary[lowest]
    print("Highest month: {}, Lowest month: {}".format(highest_month, lowest_month))


def is_seasonal_product(profits):
    winter = profits[11] + profits[0] + profits[1]
    spring = profits[2] + profits[3] + profits[4]
    summer = profits[5] + profits[6] + profits[7]
    autumn = profits[8] + profits[9] + profits[10]
    return winter + summer > spring + autumn


#Work out total expenditure
def get_total_expenditure(monthly):
    monthly_expenditure = monthly
    total_expenditure = 0
    for x in monthly_expenditure:
        total_expenditure += x
    return total_expenditure


if __name__ == '__main__':
    # MUST
    # read sales.csv data
    data = read_data('sales.csv')
    # get monthly sales
    monthly_sales = data['sales'].values
    print(monthly_sales)
    # get total sales across all months
    total_sales = get_total_sales(monthly_sales)
    print("Total sales: {}".format(total_sales))
    # SHOULD
    # get average sales over months
    avg = get_average(monthly_sales)
    avg = round(avg, 3)
    print('Average sales: {}'.format(avg))
    # get highest and lowest monthly sales
    months = data['month'].values
    get_highest_lowest(monthly_sales, months)
    # create dictionary that shows percentage change as a percentage
    percentage_change_dictionary = get_monthly_change(monthly_sales, months)
    print(percentage_change_dictionary)
    # COULD #
    # calculate highest expenditure and lowest expenditure
    expenditure = data['expenditure'].values
    get_highest_lowest(expenditure, months)
    # calculate monthly profit
    profit = monthly_sales - expenditure
    print('Monthly profits: {}'.format(profit))
    # calculate monthly changes in expenditure
    monthly_expenditure_change = get_monthly_change(expenditure, months)
    print(monthly_expenditure_change)
    #  calculate seasonal profits
    print(is_seasonal_product(profit))
    # add profit to the original csv file and export it
    data['profit'] = profit
    new_data = pd.DataFrame(data)
    new_data.to_csv('new_sales.csv')
    # get monthly expenditure
    monthly_expenditure = data['expenditure'].values
    print(monthly_expenditure)
    # get total expenditure across all months
    total_expenditure = get_total_expenditure(monthly_expenditure)
    print("Total expenditure: {}".format(total_expenditure))
    # get total profit across all months
    total_profit = total_sales - total_expenditure
    print("Total profit: {}".format(total_profit))