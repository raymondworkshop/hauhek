import jieba_fast as jieba

jieba.load_userdict("./data/dict.txt")


if __name__ == "__main__":
    sents = ["呢幾日天氣成日變，你要小心保重身體。",
             "呢段時間過得順唔順吖？做嘢好辛苦嘞？",
             "叔叔，唔該你送俾我嘅禮物，我好中意。",
             "我真係冇諗到會搞成噉㗎，原諒我好唔好？",
             "佢真係唔係幾識曹太架"]

    for i in range(len(sents)):
        words = jieba.cut(sents[i])
        print('-'.join(words) + '\n')
