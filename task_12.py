def generate_primes():
    n = 2  # Починаємо з найменшого простого числа
    while True:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):  # Ділимо до √n
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n  # Якщо число просте, повертаємо його
        n += 1

primes = generate_primes()

for i, prime in enumerate(primes):
    if i >= 10:
        break
    print(f"index: {i}, result: {prime}")
