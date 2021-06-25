# sip calculator

Daily_Invest_amnount = int(input("Enter the value of investment:  "))
Expected_returns = int(input("Enter the Expected Returns:  "))
Time_period = int(input("Enter the time Period:  "))

number_of_payments = Daily_Invest_amnount * Time_period

Maturity = Daily_Invest_amnount * (((1 + Expected_returns) *number_of_payments - 1 ) / Expected_returns) * (1 + Expected_returns)

print(Maturity)