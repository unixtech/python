# INPUT DATA
data = [
    (1000, 10),
    (2000, 17),
    (2500, 170),
    (2500, -170),
]
# Print the header for reference
print('REVENUE | PROFIT | PERCENT')
# This template aligns and displays the data in the proper format
TEMPLATE = '{revenue:>7,} | {profit:>+6} | {percent:>7.2%}'

# Print data rows
for revenue, profit in data:
    row = TEMPLATE.format(revenue=revenue, profit=profit, percent=profit/revenue)
    print(row)
