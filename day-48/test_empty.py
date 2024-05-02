cookie_score = [15, 100, 500, 2000, 7000, 50000, 1000000, 123456789]
cookie_score = cookie_score[::-1]
print(cookie_score)

store_prices =[123456789, 1000000, 50000, 7000, 2000, 500, 100, 15]
max_indexes = [len(store_prices)-index for index, score in enumerate(store_prices) if score <= 520]
max_store_buy= max(max_indexes)
print("En buyuk degerin index(leri):",max_store_buy)
       