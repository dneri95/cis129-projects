#Dominic Neri
#My Coffee Shop
#Prints receipt
print(' ***************************************\n My Coffee and Muffin Shop')

#input numbers
coffee = int(input(' Number of coffees bought?\n '))
muffin = int(input(' Number of muffins bought?\n '))
fruits = int(input(' Number of fruits bought?\n '))
smoothies = int(input(' Number of smoothies bought?\n '))

#price of total cost of products individually
coffee_total = coffee * 5.00
muffin_total = muffin * 4.00
fruits_total = fruits * 2.00
smoothies_total = smoothies * 6.00

#tax of total price added together
tax = (coffee_total + muffin_total + fruits_total + smoothies_total) * .06

#total price added together
total = coffee_total + muffin_total + fruits_total + smoothies_total + tax

#print receipt
print(' ***************************************\n\n ***************************************\n My Coffee and Muffin Shop Receipt\n',
      coffee, 'Coffee at $5 each: $', coffee_total, '\n' ,muffin, 'Muffin at $4 each: $',
      muffin_total, '\n', fruits, 'Fruits at $2 each: $', fruits_total, '\n', smoothies, 'Smoothies at $6 each: $', smoothies_total, 
      '\n', '6% tax: $', tax, '\n', '---------\n', 'Total: $', total, '\n', '***************************************')

#message to customer
print(' Dont have a good day, Have a great day!')
