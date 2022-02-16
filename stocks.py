# Bianca Beltran
# stocks.py


COMISSION_RATE = float(input('What was the commission rate?:'))
NUM_SHARES = float(input('How many shares did you purchase?:'))
PURCHASE_PRICE = float(input('What was the purchase price?:'))
SELLING_PRICE = float(input('What was the selling price?:'))
print('Amount paid for stock:',NUM_SHARES * PURCHASE_PRICE)
AMOUNT_PAID = NUM_SHARES * PURCHASE_PRICE
PURCHASE_PAY = COMISSION_RATE * AMOUNT_PAID
print('Comission paid on the purchase:', PURCHASE_PAY)
SOLD_FOR = NUM_SHARES * SELLING_PRICE
print('Amount the stock sold for:', SOLD_FOR)
SALE_PAY = SOLD_FOR * COMISSION_RATE
print('Comission paid on the sale:', SOLD_FOR * COMISSION_RATE)
TOTAL_COMISSION = PURCHASE_PAY + SALE_PAY
print('Total comission paid:', TOTAL_COMISSION)
PROFIT = SOLD_FOR - AMOUNT_PAID - TOTAL_COMISSION
print('Profit (or loss if negative):', PROFIT)

