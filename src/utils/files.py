import json
import os
import numpy as np

def read_txt_file(path):
    with open(path, 'r') as f:
        content = f.readlines()
    return content


def read_json_file(path):
    
    path = os.path.join(os.path.dirname(__file__), path)
    with open(path, encoding='utf-8-sig') as f:
        content = json.load(f)
    return content

def format_matrix(matrix):
    newMatrix = []
    for i in matrix:
        newLine = i.replace('\n', '').split(' ')
        for j in range(len(newLine)):
            newLine[j] = float(newLine[j])
        newMatrix.append(newLine)

    return np.array(newMatrix)

def write_output_file(content):

    path = "..\\..\\data\\outputs\\output.json"
    path = os.path.join(os.path.dirname(__file__), path)

    print("leia o arquivo de saída: \n", content)

    with open(path, 'w') as outfile:
        json.dump(content, outfile, indent=4)

def read_matrix_file(path):
    
    path = os.path.join(os.path.dirname(__file__), path)


    with open(path, 'r',  encoding='utf-8-sig') as f:
        content = f.readlines()
    
    matrix = []
    for line in content:
        matrix.append([float(n) for n in line.split()])

    return np.array(matrix)

def read_vector_file(path):
    
    path = os.path.join(os.path.dirname(__file__), path)


    with open(path, 'r',  encoding='utf-8-sig') as f:
        content = f.readlines()
    
    matrix = []
    for line in content:
        matrix.append(float(line.split()[0]))

    return np.array(matrix)

def read_pairs_file(path):
    
    path = os.path.join(os.path.dirname(__file__), path)


    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.readlines()
    
    values_x = []
    values_y = []
    for line in content:
        [x, y] = line.split()
        values_x.append(float(x))
        values_y.append(float(y))

    return [np.array(values_x), np.array(values_y)]