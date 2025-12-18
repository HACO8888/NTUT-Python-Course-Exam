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
      
def save_counts_to_file(counts, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('[')
        for i, (char, count) in enumerate(counts):
            file.write(f'（{char}：{count}）')
            if i < len(counts) - 1:
                file.write('，')
        file.write(']')
        
if __name__ == "__main__":
    input_file = 'poem.txt'
    output_file = 'ex2-poem.txt'
    counts = count_characters(input_file)
    print('[' + '，'.join([f'（{char}：{count}）' for char, count in counts]) + ']')
    save_counts_to_file(counts, output_file)