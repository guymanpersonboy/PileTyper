def organize_words_to_js_array(file_path, output_file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()

    js_array = 'const wordsArray = ['

    w = 0
    for word in words:
        w += 1
        js_array += f'"{word}", '
        if (w % 1000 == 0):
            js_array += f'\n'

    js_array = js_array.rstrip(', ')
    js_array += '];'

    with open(output_file_path, 'w') as output_file:
        output_file.write(js_array)


# Example usage
input_file_path = 'words.txt'  # Replace with the path to your input file
output_file_path = 'output.js'  # Replace with the desired output file path
organize_words_to_js_array(input_file_path, output_file_path)
