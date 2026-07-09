"""
Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
"""


def discount_price(original_price, discount_percent):
    discount_amount = (discount_percent / 100) * original_price
    final_amount = original_price - discount_amount
    print(f"You will get discount of Rs.{discount_amount}")
    print(f"Your final amount is Rs.{final_amount}")


discount_price(100, 50)
discount_price(4324532, 33)
