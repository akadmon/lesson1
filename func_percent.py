def bg_percent(price, discount, separator='/n'):
    discount_summ = price * discount / 100
    discounted = price - discount_summ 
    return discount_summ, discounted

price_without_discount = int(input("Цена без скидки: "))
discounter = int(input("Скидка: "))

print (bg_percent (price_without_discount, discounter))