for root in range(11112, 14949):
    num = root ** 2
    divs = [root]
    for div in range(2, root):
        if num % div == 0:
            divs.append(div)
            divs.append(num // div)
            if len(divs) > 3:
                break
    if len(divs) == 3:
        print(num, max(divs))