from task_1.class_task_1 import task_1
from task_2.class_task_2 import task_2

from utils.files import read_matrix_file, read_vector_file, read_json_file


def main():

    task = int(input("Escolha a task desejada: "))

    load_config = read_json_file("../../data/inputs/config.json")

    if(task == 1):

        matrix_a = read_matrix_file(load_config["Path_Matrix_A"])
        vector_b = read_vector_file(load_config["Path_Vector_B"])

        task_object = task_1(load_config["ICOD"],matrix_a, vector_b, load_config["TOLm"])

        task_object.run()

    elif(task == 2):
    
        matrix_a = read_matrix_file(load_config["Path_Matrix_A"])

        task_object = task_2(load_config["ICOD"],
                             load_config["IDET"], matrix_a, load_config["TOLm"])

        task_object.run()


if __name__ == "__main__":
    main()