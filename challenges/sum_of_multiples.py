def calc_sum_multiples(limit, divisor1, divisor2):
    sum_multiples = 0
    for n in range(1, limit):
        if (n%divisor1 == 0) or (n%divisor2 == 0):
            sum_multiples+=n
    
    return sum_multiples

print(calc_sum_multiples(1000, 3, 5))