def discounted(price, discount, max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except(ValueError, TypeError):
        return 'Переданы некорректные аргументы'


print(discounted('cat', 10, 20))
print(discounted(234, 30, 20))
print(discounted(3434, '44', 20))
