import itertools

main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

courses = []
prices = []
threshold = 30

for a, b, c in itertools.product(main_courses, desserts, drinks):
    courses.append(f'{a} {b} {c}')

for d, e, f in itertools.product(price_main_courses, price_desserts, price_drinks):
    sum_comp = d + e + f
    prices.append(sum_comp)

for g, h in zip(courses, prices):
    if h <= threshold:
        print(g, h)

# Alternative
dishes = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)
result_list = list(zip(dishes, prices))
for b in result_list:
    if sum(b[1]) <= 30:
        print(f'{" ".join(b[0])} {sum(b[1])}')


