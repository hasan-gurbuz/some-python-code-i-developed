def clockwise(X):
    if X == 'N':
        return 'E'
    elif X == 'E':
        return 'S'
    elif X == 'S':
        return 'W'
    elif X == 'W':
        return 'N'
    else:
          return None
wise = input()
clockwise(wise)
print(clockwise(wise))