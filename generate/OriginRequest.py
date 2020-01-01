import random
from copy import deepcopy
from generate.solve import solvable


class BiTree:
    def getOperOrder(self, ch):
        if ch in ['+', '-']:
            return 0
        elif ch in ['*']:
            return 2
        elif ch in ['/']:
            return 3
        elif ch == '^':
            return 4

    def __init__(self, node_type=0, val=0):
        self.node_type = node_type
        self.val = val
        self.lchild = None
        self.rchild = None
        if self.node_type == 1:
            self.val = chr(self.val)
            self.this_level = self.getOperOrder(self.val)

    def set_lchild(self, lchild):
        self.lchild = lchild

    def set_rchild(self, rchild):
        self.rchild = rchild

    def to_string(self, upper_level=0):
        if self.node_type == 1:
            if upper_level > self.this_level or upper_level == self.this_level == 3 or upper_level == self.this_level \
                    == 4:
                return '(' + self.lchild.to_string(self.this_level) + self.val + self.rchild.to_string(
                    self.this_level + 1) + ')'
            else:
                return self.lchild.to_string(self.this_level) + self.val + self.rchild.to_string(self.this_level + 1)
        if int(self.val) < 0:
            return '(' + str(self.val) + ')'
        return str(self.val)


class Op:
    def __init__(self, x, if_need_delete=False, priority=0):
        self.index = x
        self.if_need_delete = if_need_delete
        self.priority = priority


class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断是否为空"""
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class QuestGenerator:
    def __init__(self):
        self.output_list = []
        self.deduplicate_set = set()

    def generate(self, quantity=1, operators=7, if_false=False, if_pow=False, Pow_Operator=False, Max=9):
        operands = ['+', '-', '*', '/', '^']
        sum = 0
        while sum < quantity:
            if if_false:
                nums = [BiTree(0, random.randint(-Max, Max)) for _ in range(operators + 1)]
            else:
                nums = [BiTree(0, random.randint(0, Max)) for _ in range(operators + 1)]
            if if_pow:
                ops = [BiTree(1, ord(operands[random.randint(0, 4)])) for _ in range(operators)]
            else:
                ops = [BiTree(1, ord(operands[random.randint(0, 3)])) for _ in range(operators)]
            unfilled_ops = ops
            filled_ops = nums
            while len(unfilled_ops):
                i = random.randint(0, len(filled_ops) - 1)
                unfilled_ops[0].set_lchild(filled_ops[i])
                filled_ops.pop(i)
                i = random.randint(0, len(filled_ops) - 1)
                unfilled_ops[0].set_rchild(filled_ops[i])
                filled_ops.pop(i)
                filled_ops.append(unfilled_ops[0])
                unfilled_ops.pop(0)
            if self.deduplicate(filled_ops[-1]):
                print('Duplicated!')
                continue
            string = filled_ops[-1].to_string()
            solve = solvable()
            k = solve.calculator(string)
            if k == 'not solvable':
                continue
            k1 = self.round_up(round(float(k.numerator / k.denominator), 3))
            sum = sum + 1
            string = self.changePowOp(string, Pow_Operator)
            print(string, '=', str(k),str(k1))
            self.output_list.append(string)
            self.output_list.append(str(k))
            self.output_list.append(str(k1))

    def deduplicate(self, root: BiTree):
        # 深拷贝 - 避免破坏原有的随机顺序
        inspect = deepcopy(root)
        QuestGenerator.format_expression(inspect)
        if inspect.to_string() in self.deduplicate_set:
            return True
        else:
            self.deduplicate_set.add(inspect.to_string())
            return False

    def format_expression(node: BiTree):
        if not node.lchild:
            return
        QuestGenerator.format_expression(node.lchild)
        QuestGenerator.format_expression(node.rchild)
        # 仅有+×可交换
        if node.val in (0, 2) and node.lchild.to_string() > node.rchild.to_string():
            tmp = node.lchild
            node.lchild = node.rchild
            node.rchild = tmp

    def round_up(self, value):
        return round(value * 100) / 100

    def changePowOp(self, string: str, Pow_Operator):
        if Pow_Operator:
            return string.replace('^', '**')
        return string
