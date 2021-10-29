def card():
    m = ['пики', 'трефы', 'бубны', 'червы']
    d = ['валет', 'дама', 'король', 'туз']
    mN = int(input('номер масти')) - 1
    if mN > len(m):
        return False
    dN = int(input('номер достоинства'))
    if dN >= 15:
        return False
    if dN > 10:
        dN -= 11
        return