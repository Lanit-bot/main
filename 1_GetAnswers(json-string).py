#1-й кусок из 4-х кусков в плане Артёма
import json

with open("questionary-2.json", "r", encoding="utf-8-sig") as read_file:
    raw_data = json.load(read_file)
big_array = []

for index in raw_data[0]['participations'].keys():
    array = []
    array.append(index)
    if type(raw_data[0]['participations'][index]) == list:
        for info_segment in raw_data[0]['participations'][index]:
            if type(info_segment) == dict and 'questionId' in info_segment.keys() and 'answer' in info_segment.keys():
                if info_segment['questionId'] == '1' or info_segment['questionId'] == '4':
                    array.append(info_segment['answer'])
    big_array.append(array)    
