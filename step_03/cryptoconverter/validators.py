def esFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
