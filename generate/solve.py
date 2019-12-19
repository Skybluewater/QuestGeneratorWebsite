from fractions import Fraction


class solvable:
    prior = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, '(': -1}

    def solve(self, num1: Fraction, num2: Fraction, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num2 - num1
        elif operator == '/':
            if num1 == 0:
                return 'not solvable'
            return num2 / num1
        elif operator == '*':
            return num2 * num1
        elif operator == '^':
            k1 = num2.denominator
            k2 = num2.numerator
            if num1 == 0:
                return Fraction(1, 1)
            elif num1 >= 5 or num1 <= 0.2 or num2 >= 100 or num2 <= 0.01:
                return 'not solvable'
            k2 = pow(int(k2), num1)
            k1 = pow(int(k1), num1)
            if type(k1) == int and type(k2) == int:
                return Fraction(k2, k1)
            else:
                return 'not solvable'

    def Calculator(self, line):
        opt = []
        data = []
        i = 0
        while i < len(line):
            start = i
            if line[i] == '(':
                if line[i + 1] == '-':
                    i += 1
                    while line[i + 1].isdigit() and i + 1 < len(line):
                        i += 1
                    data.append(Fraction(int(line[start + 1:i + 1]), 1))
                    i += 1
                else:
                    opt.append(line[i])
            elif line[i].isdigit():
                while i + 1 < len(line) and line[i + 1].isdigit():
                    i += 1
                data.append(Fraction(int(line[start:i + 1]), 1))
            elif line[i] == ')':
                while opt[-1] != '(':
                    k = self.solve(data.pop(), data.pop(), opt.pop())
                    if k == 'not solvable':
                        return 'not solvable'
                    data.append(k)
                opt.pop()
            else:
                while opt and self.prior[line[i]] <= self.prior[opt[-1]]:
                    k = self.solve(data.pop(), data.pop(), opt.pop())
                    if k == 'not solvable':
                        return 'not solvable'
                    data.append(k)
                opt.append(line[i])
            i += 1
        while opt:
            k = self.solve(data.pop(), data.pop(), opt.pop())
            if k == 'not solvable':
                return 'not solvable'
            data.append(k)
        k = data.pop()
        if k.denominator > 5000 or k.numerator > 5000:
            return 'not solvable'
        return k
