from difflib import get_close_matches
from config import key_words


def get_pair(data_string : str):
    data_string_split = data_string.split()
    value = data_string.split()
    not_key_words_in_a_row = 0
    key = ''
    for i,word in enumerate(data_string_split):
        ans = get_close_matches(word.lower(), key_words, n=1)
        if len(ans) != 0:
            data_string_split[i] = ans[0]
            last_key_index = i+1
            not_key_words_in_a_row = 0
            key = ' '.join(data_string_split[:last_key_index])
            value = data_string_split[last_key_index:]
        else:
            not_key_words_in_a_row += 1
        if not_key_words_in_a_row == 4:
            return key, ' '.join(value)
    return key, ' '.join(value)


if __name__ == '__main__':
    print(get_pair("Гр;тправитель Обособленное подразделение ООО Комус 454008, Челябинская обл., г.Челябинск, улАвтодорожная, 19-а, тел. 8-800-200-33-83 факс 8-800-200-33-83"))
    print(get_pair("Грузополучатель:ОООУЦСБ 620100, Свердловская обл., г.Екатеринбург, ул.Ткачей, 6, тел 3433799834"))
    print(get_pair("Грузополучатель: ОООУЦСБ 620100, Свердловская обл., г.Екатеринбург, ул.Ткачей, 6, тел 3433799834"))
    print(get_pair("ООУЦСБ 620100, Свердловская обл., г.Екатеринбург, ул.Ткачей, 6, тел 3433799834"))
    print(get_pair("Грузополучатель три случаенных слова Грузоотправите, Свердловская обл., г.Екатеринбург, ул.Ткачей, 6, тел 3433799834"))
    print(get_pair("Грузополучатель пять самых очень случаенных слова Грузоотправите, Свердловская обл., г.Екатеринбург, ул.Ткачей, 6, тел 3433799834"))

