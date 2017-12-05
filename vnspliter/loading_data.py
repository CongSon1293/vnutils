from bs4 import BeautifulSoup
from io import open
import os.path
c_dir = os.path.abspath(os.path.dirname(__file__))

raw_data_path = "%s/data/training.xml"%c_dir
raw_none_splitter_path = "%s/data/none_spliter.dat"%c_dir

def load_sentence():
    sens = []
    with open(raw_data_path,encoding="UTF-8") as raw_data:
        data =  BeautifulSoup(raw_data,'html.parser')
        sentences = data.find_all('s')
        for sen in sentences:
            sens.append(sen.string.strip())
        raw_data.close()

    return sens

def load_none_spliter():
    sens = []
    with open(raw_none_splitter_path,encoding="UTF-8") as raw_data:
        while True:
            line = raw_data.readline()
            if line == "":
                break
            sens.append(line.strip())
        raw_data.close()
    return sens

