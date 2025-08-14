# Ask user for inputs
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)  # convert % to decimal
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get result and print
final_price = calculate_discount(price, discount_percent)
print(f"Your total price is {final_price}")
