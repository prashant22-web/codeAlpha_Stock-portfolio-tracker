stock_prices = {
    "APPLE" : 180,
    "TSLA" : 450,
    "AMZN" : 500,
    "GOOGLE" : 800,
    "FLIPKART" : 900

}
print(stock_prices)

total_portfolio = 0
portfolio = []

while True:

 stock_name = input("enter the name :").upper()
 quantity = int(input("enter the quantity :"))

 if stock_name in stock_prices:
    
    price = stock_prices[stock_name]
    print("stock_price : " , price)

    total_investment = price * quantity
    print("tottal_investment :", total_investment)

    total_portfolio = total_portfolio + total_investment
    print("total_portfolio :", total_portfolio)
    portfolio.append({
    "stock": stock_name,
    "quantity": quantity,
    "price": price,
    "investment": total_investment
})
 else:
  print("stock not found")

  again = input("do you want to add another stock ? (yes/no) : ").lower()
  if again == "no":
    break


print("\nPortfolio Summary:")

for item in portfolio:
    print(
        item["stock"],
        "- Quantity:", item["quantity"],
        "- Price:", item["price"],
        "- Investment:", item["investment"]
    )
print("Final Portfolio Value:", total_portfolio)
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio\n")
    file.write("----------------\n")

    for item in portfolio:
        file.write(
            f"{item['stock']} - "
            f"Quantity: {item['quantity']} - "
            f"Price: {item['price']} - "
            f"Investment: {item['investment']}\n"
        )

    file.write(f"\nTotal Portfolio Value: {total_portfolio}\n")

print("Portfolio saved successfully!")