def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    return price

original_price = 100
discount = 20
final_price = calculate_discount(original_price, discount)
print(f"Final price: ${final_price:.2f}")
# price =$75