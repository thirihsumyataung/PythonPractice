

print(3 **2)

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result
# index = 0 => 1(result) * 3(base_num) = 3
# index = 1 => 3(result) * 3(base_num) = 9 (Final Result)

print(raise_to_power(3,2))
print(raise_to_power(3,3))

# index = 0 => 1(result) * 2(base_num) = 2
# index = 1 => 2(result) * 2(base_num) = 4
# index = 2 => 4(result) * 2(base_num) = 8 (Final Result)

print(raise_to_power(2,3))

