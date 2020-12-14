def report_repair(expenses, n):
    i = 0
    while i + 1 < len(expenses):
        if (expenses[i] + expenses[i+1]) == n:
            return n
        i += 1




