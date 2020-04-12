'''
@Author: your name
@Date: 2020-04-11 19:45:35
@LastEditTime: 2020-04-12 21:45:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /ToyParser/src/parser.py
'''
from nltk import Tree
from nltk import DependencyGraph

class Parser():
    '''
    针对CFG文法实现的ToyParser，能够根据给定的CFG文法对特定句子进行词法分析，判断其合法性，如果合法可以绘制其词法树
    '''
    def __init__(self):
        self.paths = {'ntrms':'../CFG/ntrms.txt', 'trms':'../CFG/trms.txt', 'realtions':'../CFG/realtions.txt'}
        self.ntrms = list() # self.ntrms[0]表示开始符号
        self.trms  = list()
        self.realtions = list() # [(ntrm, str生成式)]
        #self.load_cfg()
        self.tree  = [('root', 0), ('child1', 1), ('child2', 1),] 

    def load_cfg(self):
        # 读取cfg，对相关变量进行初始化
        for ntrm in self.iterate_row(self.paths['ntrms']):
            self.ntrms.append(ntrm)
        for trm in self.iterate_row(self.paths['trms']):
            self.trms.append(trm)
        for line in self.iterate_row(self.paths['relations']):
            [left, right] = line.split('|-')
            relation = (left, right)
            self.realtions.append(relation)
        
    def iterate_row(self, path):
        # 遍历文件每一行并返回
        with open(path, 'r') as f:
            for line in f.readlines():
                yield line.strip()

    def parser(self, sentence):
        # 对句子进行词法分析，如果合法返回True，并将词法树存储在self.tree中
        pass

    def draw(self):
        # 绘制词法树
        par_result = ''
        for node in self.tree:
            par_result += "\t" + node[0] + "\t" + 'null' + "\t" + str(node[1]) + "\n"
        conlltree = DependencyGraph(par_result)  
        tree = conlltree.tree()  # 构建树结构
        tree.draw()  # 显示输出的树

parser = Parser()
parser.draw()