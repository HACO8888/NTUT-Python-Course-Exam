import csv
from collections import Counter
import re
import operator

def count_characters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        characters = re.findall(r'[\u4e00-\u9fff]', text)
        character_counts = Counter(characters)
        sorted_counts = sorted(character_counts.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_counts
      
def save_counts_to_csv(counts, output_file):
    with open(output_file, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Character', 'Count'])
        for char, count in counts:
            writer.writerow([char, count])
            
if __name__ == "__main__":
    input_file = 'poem.txt'
    output_file = 'ex3-poem.csv'
    counts = count_characters(input_file)
    print('[' + '，'.join([f'（{char}：{count}）' for char, count in counts]) + ']')
    save_counts_to_csv(counts, output_file)