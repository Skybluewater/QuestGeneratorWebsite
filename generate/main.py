from generate import OriginRequest as Qr


def answer(quantity: int, list: list, if_fraction=0):
    i = 0
    correct = 0
    while i < list.__len__():
        if i % 2 == 0:
            print(list[i], '=')
        else:
            if if_fraction:
                st = input('answer:')
                if st == list[i]:
                    correct += 1
                else:
                    print('incorrect')
            else:
                st = input('answer:')
                st = float(st)
                if st == float(list[i]):
                    correct = correct + 1
                else:
                    print('incorrect')
        i = i + 1
    print('correct num', correct)
    print('wrong num', quantity - correct)


def main(quantity, operators, if_negative, if_pow, _max):
    g = Qr.QuestGenerator()
    g.generate(quantity=quantity, operators=operators, if_false=if_negative, if_pow=if_pow, _max=9)
    with open('out.txt', 'w', encoding='utf-8') as f:
        for out in g.output_list:
            f.write(out + '\n')
    return g.output_list

