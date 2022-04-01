import sqlite3
import translate

name_table = "dictionary"

def wrire_data(english, russian):
    con = sqlite3.connect('data_base.db')
    cur = con.cursor()
    # Create table
    try:
        cur.execute(f"CREATE TABLE {name_table} (english text, russian text)")
    except:
        print("table create ago")
    write_row = True
    for row in cur.execute(f'SELECT * FROM {name_table}' ):
        if row[0] == english and row[1] == russian:
            write_row = False
    if write_row:
        cur.execute(f"INSERT INTO {name_table} VALUES (?, ?)", (english, russian))
    con.commit()
    con.close()
    return write_row

def return_word(word, language="en"):
    """language=en, ру"""
    con = sqlite3.connect('data_base.db')
    cur = con.cursor()
    word_list=[]
    if language == "ру":
        test = f"SELECT english FROM {name_table} WHERE russian ='{word}'"
    else:
        test = f"SELECT russian FROM {name_table} WHERE english ='{word}'"
    for row in cur.execute(test):
        word_list.append(row[0])
    con.close()
    string_word = ""
    for i in word_list:
        if len(word_list) == 1:
            string_word = i
            break
        string_word = string_word + str(i) + ", "
    if string_word[-2:] == ", ":
        string_word = string_word[:-2]
    return string_word

def dictionary_list():
    con = sqlite3.connect('data_base.db')
    cur = con.cursor()
    word_list = []
    for i in cur.execute("SELECT distinct english FROM dictionary;"):
        word_list.append(i[0])
    translate_list = ""
    for i in word_list:
        translate_list = translate_list + i + " - "
        for j in cur.execute(f"SELECT russian FROM dictionary WHERE english = '{i}';"):
            if translate_list[-2:] == "- ":
                translate_list = translate_list + j[0]
            else:
                translate_list = translate_list + ", " + j[0]
        translate_list = translate_list + "\n"
    translate_list = translate_list[:-1]
    con.close()
    return translate_list

def search_word(word):
    """En word, Ру слово"""
    language = word.split(" ")[0].lower()
    word = word.split(" ")[1]
    word_in_base = return_word(word=word, language=language)
    if word_in_base == "":
        translate_word = translate.translate(word=word, language=language)
        if language == "en":
            wrire_data(english=word, russian=translate_word)
        else:
            wrire_data(english=translate_word, russian=word)
        word_in_base = return_word(word=word, language=language)
    return word_in_base

def add_to_dictionary(text):
    word = text.split(" - ")[0]
    translate_word = text.split(" - ")[1]
    if wrire_data(english=word, russian=translate_word):
        text = "add to dictionaty"
    else:
        text = "the word is already in the dictionary"
    return text

def wrire_data_weather(data_weather, list_temp):
    name_table = "weather"
    con = sqlite3.connect('data_base.db')
    cur = con.cursor()
    # Create table
    try:
        cur.execute(f"CREATE TABLE {name_table} (data text, temp_9 text, temp_12 text, temp_15 text, temp_18 text)")
    except:
        print("table create ago")
    write_row = True
    for row in cur.execute(f'SELECT data FROM {name_table} WHERE data ="{data_weather}"' ):
        print("it data was written")
        write_row = False
    if write_row:
        cur.execute(f"INSERT INTO {name_table} VALUES (?, ?, ?, ?, ?)", (data_weather, list_temp[0], list_temp[1], list_temp[2], list_temp[3]))
    con.commit()
    con.close()
    return write_row

def read_data_weather(data_weather):
    name_table = "weather"
    con = sqlite3.connect('data_base.db')
    cur = con.cursor()
    for row in cur.execute(f'SELECT * FROM {name_table} WHERE data = "{data_weather}"' ):
        tuple_term = row
    return [tuple_term[1], tuple_term[2], tuple_term[3], tuple_term[4] ]

if __name__ == "__main__":
    english, russian = "word", "слово"
    assert english == return_word(word = russian, language="ру")
    assert russian == return_word(english)
    english, russian = "animal", "зверь"
    assert english == return_word(word = russian, language="ру")
    assert "животное, зверь" == return_word(english)
    assert "the word is already in the dictionary" == add_to_dictionary("text - текст")
    assert "word - слово" in dictionary_list()
    assert "слово" == search_word("En word")
    assert "животное, зверь" == search_word("En animal")
    assert "animal" == search_word("ру животное")
    assert "собака" == search_word("en dog")

    assert False == wrire_data_weather("2022-03-29", ['+4°', '+7°', '+6°', '+10°'])
    assert ['+4°', '+7°', '+6°', '+10°'] == read_data_weather("2022-03-29")
