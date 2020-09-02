import json
import xml.etree.ElementTree


def more_6_simbols(x):
    if len(x) > 6:
        return 1
    else:
        return 0


def find_top_10_word(list_of_news):
    one_string_news = ' '.join(list_of_news)
    list_of_words = one_string_news.split()
    filter_list_of_words = list(filter(more_6_simbols, list_of_words))
    count_words = {}.fromkeys(filter_list_of_words, 0)

    for word in filter_list_of_words:
        count_words[word] += 1
    sorted_count_words = sorted(count_words.items(), key=lambda x: x[1], reverse=True)[:10]

    top_10 = []
    for word in sorted_count_words:
        top_10.append((word[0]))
    return top_10


with open('files/newsafr.json', encoding='utf-8') as f:
    data = json.load(f)
    news_list_for_json = []
    for news in data['rss']['channel']['items']:
        current_news = news['description']
        news_list_for_json.append(current_news)
    print(find_top_10_word(news_list_for_json))

print("======================")

parser = xml.etree.ElementTree.XMLParser(encoding='utf-8')
tree = xml.etree.ElementTree.parse('files/newsafr.xml', parser)
root = tree.getroot()
news_list = root.findall('channel/item')

news_list_for_xml = []

for news in news_list:
    descript = news.find('description').text
    news_list_for_xml.append(descript)

print(find_top_10_word(news_list_for_xml))
