#Dominic Neri
#My Coffee Shop
#Prints receipt
print(' ***************************************\n My Coffee and Muffin Shop')

#input numbers
coffee = int(input(' Number of coffees bought?\n '))
muffin = int(input(' Number of muffins bought?\n '))

#price of total cost of products individually
coffee_total = coffee * 5.00
muffin_total = muffin * 4.00

#tax of total price added together
tax = (coffee_total + muffin_total) * .06

#total price added together
total = coffee_total + muffin_total + tax

#print receipt
print(' ***************************************\n\n ***************************************\n My Coffee and Muffin Shop Receipt\n',
      coffee, 'Coffee at $5 each: $', coffee_total, '\n' ,muffin, 'Muffin at $4 each: $',
      muffin_total, '\n', '6% tax: $', tax, '\n', '---------\n', 'Total: $', total, '\n', '***************************************')
