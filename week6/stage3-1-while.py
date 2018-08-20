
# ------------------- while -----------------

# page = 0
#
# while page < 10:
#     page += 1
#     print(page)


# -------------- while / break --------------

fibonacci = [1, 2]
first_idx = 0

while True:
    next_fibo = fibonacci[first_idx] + fibonacci[first_idx + 1]

    if next_fibo > 100:
        break

    fibonacci.append(next_fibo)
    first_idx += 1

print(fibonacci)
