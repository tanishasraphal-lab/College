# This code extracts date and money expressions from a given text using regular expressions.
import re
text = "John paid $500 on 12/05/2026 and another ₹2000 on 15-06-2026."
#Date Pattern
date_pattern = r'\b\d{2}[/-]\d{2}[/-]\d{4}\b'
#Money Pattern
money_pattern = r'[\$₹]\d+'
dates = re.findall(date_pattern, text)
money = re.findall(money_pattern, text)
print("Date Expressions:")
for d in dates:
    print(d, "-> DATE")
print("\nMoney Expressions:")
for m in money:
    print(m, "-> MONEY")