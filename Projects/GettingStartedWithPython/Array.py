var_array = [1 for i in range(101)]

total = 0

for num in var_array:
    total += num

count = len(var_array)

result = total/count

print(f"Rata-rata dari elemen array adalam {result}")