# -*- coding: utf-8 -*-
from io import open
from vnspliter.sentence_spliter import SentenceSpliter
import re
def check_re():
    reg = re.compile("(T[pP]\.)\s?[A-ZÁÀÃẢẠẮẰẲẶẴÂẤẦẨẬẪĐÉÈẺẼẸÊẾỀỄỂỆÍÌỈỊÓÒỏỎÕỌÔốỐồỒổỔỖỘƠớỚỜỞỠỢÚÙủỦŨỤƯứỨỪỬỮỰÝỲỶỹỸỴ]\w+",re.UNICODE)
    sen = u"Tp. Tiền Giang"
    s= reg.search(sen)
    print s
def demo_file():
    sentence_spliter = SentenceSpliter(new_rule_path="new_rules.dat")
    while True:
        cmd = raw_input("Cmd 1 = Cont 0 = Quit:")
        if len(cmd) < 1:
            continue

        f = open("input.dat",encoding="UTF-8")
        file = "\n".join(f.readlines())
        print file
        f.close()
        list_sens = sentence_spliter.split(file, True)
        f = open("output.dat","w",encoding="UTF-8")
        for sen in list_sens:
            print sen
            f.write("%s\n"%sen)
        f.close()

def demo_cml():
    sentence_spliter = SentenceSpliter()
    while True:
        par = raw_input("Enter paragraph: ")
        try:
            par = unicode(par)
        except:
            par = unicode(par, encoding="UTF-8")
        print "\nParagraph: ",par
        if len(par) <2:
            continue
        print "--------------------------------"
        print "Result:"
        list_sens= sentence_spliter.split(par, True)
        for sen in list_sens:
            print sen
        #sentence_spliter.feature_model.gen_ve
def train():
    sentence_spilter = SentenceSpliter(is_training=True)
    sentence_spilter.train()

if __name__=="__main__":
   #train()
   demo_file()
   #demo_cml()
   #check_re()


