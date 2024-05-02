 
# result =  [15, 100, 500, 2000, 7000, 50000, 1000000, 123456789]
# result = result[::-1]
# for i in result:
#     print(i,result.index(i))
    
    
cookie_score = [15, 100, 500, 2000, 7000, 50000, 1000000, 123456789]
cookie_score = cookie_score[::-1]
print(cookie_score)

cookie_score =[123456789, 1000000, 50000, 7000, 2000, 500, 100, 15]
max_value=7000
max_indexes = [len(cookie_score)-index for index, score in enumerate(cookie_score) if score <= max_value]

print("En büyük değerin index(leri):", max(max_indexes))
       