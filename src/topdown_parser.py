'''
@Author: wxin
@Date: 2020-04-13 21:25:51
@LastEditTime: 2020-05-04 21:27:06
@LastEditors: Please set LastEditors
@Description: 实现自顶向下的句法分析算法
@FilePath: /ToyParser/src/topdown_parser.py
'''
from parser import Parser

class TDParser(Parser):
    # 利用自顶向下算法实现parser算法
    def __init__(self):
        super(TDParser, self).__init__()

    def parser(self, sentence):
        symbols   = ['S'] # 记录目前所产生的符号序列
        used_rels = []  # 记录使用过的生成式左式以及右式的index
        symb_lens = [] # 记录上一次使用生成式时symbols的长度
        cursors   = [] # 记录上一次使用生成式时cursor的位置
        cursor    = 0
        rel_index = 0 # 生成式的index
        def backtrack():
            nonlocal symbols, used_rels, symb_lens, cursors, cursor, rel_index
            if len(used_rels) == 0:
                print('symbols:', symbols)
                return False
            right_symb, rel_index = used_rels.pop() # used_rels回溯
            symb_len = symb_lens.pop() # symb_lens回溯
            print('symb_len:', symb_len)
            print('symbols:', symbols)
            symbols = symbols[:symb_len-1] + [right_symb] # symbols回溯
            cursor = cursors.pop() # cursors回溯
            print(cursor)


        while len(symbols) > 0:
            print('symbols:', symbols)
            print('used:', used_rels)
            print('symb_lens:', symb_lens)
            symb = symbols[-1]
            if symb in self.trms:
                if cursor < len(sentence) and symb == sentence[cursor]:
                    cursor += 1
                    rel_index = 0
                    symbols.pop()
                    if len(symbols) == 0 and cursor != len(sentence):
                        symbols.append(symb)
                        backtrack()
                    
                else:
                    backtrack()
                        
            else:
                left_rel = self.realtions[symb]
                if len(left_rel) != rel_index:
                    symb_lens.append(len(symbols))
                    used_rels.append((symb, rel_index+1))
                    cursors.append(cursor)
                    symbols.pop()
                    for symb in left_rel[rel_index][::-1]:
                        symbols.append(symb)
                    rel_index = 0
                    
                else:
                    backtrack()

        self.used_rels = used_rels[::-1]
        self.tree = []
        self.tree.append(('S', 0))
        self.dfs('S', 1)
        #return used_rels
        print('self.tree:', self.tree)
    '''
    def to_tree(self, used_rels):
        used_rels = used_rels[::-1]
        self.tree = [('S', 0)]
        index = 0
        while len(self.tree) > index:
            root = self.tree[index][0]
            if root in self.ntrms:
                print(root)
                left, rel_index = used_rels.pop()
                for symb in self.realtions[left][rel_index-1]:
                    self.tree.append((symb, index+1))
            index += 1

        print('self.tree:', self.tree)
    '''
    def dfs(self, root, root_index):
        left, rel_index = self.used_rels.pop()
        for symb in self.realtions[left][rel_index-1]:
            self.tree.append((symb, root_index))
            if symb in self.ntrms:
                self.dfs(symb, len(self.tree))


td_parser = TDParser()
td_parser.parser('aaabbbcc')
td_parser.draw()
