import re
from collections import Counter
from matplotlib import pyplot
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def NovelRe(Novel):
    content = open(Novel, 'r').read().lower()
    words = []
    pattern = r"(?<!')\b[a-zA-Z]{2}[a-zA-Z]+\b"
    tmp = re.findall(pattern, content)
    DropList = ['you','your','he','him','his','she','her','they','them','their','where','when','what','who','which','there','said','had','don','mer','for','jul','its','his','with','charles','elecbook','classics','charlotte','bront','aesop','fables','dickens','tale','and','the','that','was']
    for word in DropList:
        tmp = [x for x in tmp if x!=word]
    for x in tmp:
        words.append(x)
    Count = Counter(words).most_common(100)
    return Count
'''
#用不上
def WordListToWordDict(WordList):
    Dict = {}
    for word in WordList:
        Dict[word[0]] = word[1]
    return Dict

#用不上
def FullWordList(OldList, AddDict):
    for key in AddDict:
        OldList.append(key)
    NewList = list(set(OldList))
    return NewList
'''
def Output():
    NovelList = ['a tale of two cities(双城记).txt', 'Aesop’s Fables(伊索寓言).txt', 'Jane Eyre(简·爱).txt', 'Oliver Twist(雾都孤儿(孤星血泪)).txt', 'Romeo and Juliet(罗蜜欧和朱丽叶).txt']
    for novel in NovelList:
        print (novel[:-4]+'\n'+'========================================')
        WordList = NovelRe(novel)
        i = 1

        wordsum = 0
        for word in WordList:
            wordsum += word[1]
            
        for word in WordList:
            print (str(i) + '.'+'\t' + str(word[0]) + '\t' + str('%.5f%%' %(word[1]/wordsum)))
            i += 1
        print ('\n')
'''
#用不上
def Freq(Dict):
    WordSum = 0
    for key in Dict:
        WordSum += Dict[key]
    for key in Dict:
        Dict[key] = Dict[key]/WordSum#只是前100的单词出现总次数，不是文章总数
    return Dict

#用不上
def Style():
    NovelList = ['a tale of two cities(双城记).txt', 'Aesop’s Fables(伊索寓言).txt', 'Jane Eyre(简·爱).txt', 'Oliver Twist(雾都孤儿(孤星血泪)).txt', 'Romeo and Juliet(罗蜜欧和朱丽叶).txt']
    Dict = {}
    for novel in NovelList:
        Dict[novel[:-4]] = Freq(WordListToWordDict(NovelRe(novel)))
    WordList = []
    for key in Dict:
        WordList = FullWordList(WordList, Dict[key])
    return (WordList, Dict)

#用不上
def WordVector(WordList, Dict):
    vector = [x*0 for x in range(len(WordList))]
    for index in range(len(WordList)):
        try:
            vector[index] = Dict[WordList[index]]
        except:
            vector[index] = 0
    return vector

#用不上
def NovelVector():
    WordList, Dict = Style()
    NovelVectorDict = {}
    for key in Dict:
        NovelVectorDict[key] = WordVector(WordList, Dict[key])
    return NovelVectorDict

def Plot():
    pass
'''
def OutputForWordCloud():
    NovelList = ['a tale of two cities(双城记).txt', 'Aesop’s Fables(伊索寓言).txt', 'Jane Eyre(简·爱).txt', 'Oliver Twist(雾都孤儿(孤星血泪)).txt', 'Romeo and Juliet(罗蜜欧和朱丽叶).txt']
    WordList = []
    NovelName = []
    for novel in NovelList:
        WordList.append(NovelRe(novel))
        NovelName.append(novel[:-4])
    return NovelName, WordList

def Wordcloud(name, freq):
    wordcloud = WordCloud(max_font_size=40).fit_words(freq)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.savefig(str(name)+".jpg")
    return 0
    


if __name__ == '__main__':
    Output()
    print ('Generating wordclouds')
    NovelName, WordList = OutputForWordCloud()
    for novel, word in zip(NovelName, WordList):
        Wordcloud(novel, word)
    print ('Wordclouds saved')
    #WordList, Dict = Style()
