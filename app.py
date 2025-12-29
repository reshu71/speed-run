def calculate_total(cart_items, tax_rate):
    total = 0
    for item in cart_items:
        price = item['price']
        qty = item['qty']
        
        # Hidden Discount Logic:
        # If item price is > 500, give 10% off.
        if price > 500:
            price = price * 0.9
            
        total += price * qty
    
    final_total = total * (1 + float(tax_rate)) # Fixed line
    return final_total

def main():
    cart = [
        {'name': 'Laptop', 'price': 1000, 'qty': 1},
        {'name': 'Mouse', 'price': 50, 'qty': 2}
    ]
    
    # BAD DATA: We are passing a string, but the math expects a number
    tax_input = "0.10" 
    
    print("Calculating final bill...")
    bill = calculate_total(cart, tax_input)
    print(f"Total to pay: ${bill}")

if __name__ == "__main__":
    main()