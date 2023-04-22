from src.task_2.jacobi_method import solve_jacobi_method
from src.task_2.power_method import solve_power_method
from src.utils.files import write_output_file

class task_2:

    def __init__(self, ICOD, IDET, matrix_a, TOL_m):
    
        self.ICOD = ICOD
        self.IDET = IDET
        self.matrix_a = matrix_a
        self.TOL_m = TOL_m

    def run(self):
    
        content = {'eigen_values': [],
                'eigen_vectors': [],
                'useErrors': '',
                'determinant': 0,
                'convergenceInterationNumber': 0,
            }

        if(not isinstance(self.ICOD, int) or (self.ICOD!=1 and self.ICOD!=2)):
            content['useErrors'] = "Insira um ICOD (1 ou 2) no arquivo de configurações"
        
        else:

            if(not isinstance(self.TOL_m, float)):
                content['useErrors'] = "Insira uma valor de tolerância float no arquivo de configurações"
            
            else:

                if(self.ICOD==1):
                    print("Power Method")
                    [eigen_value, eigen_vectors, steps, use_errors] = solve_power_method(self.matrix_a, self.TOL_m)
                    content['eigen_values'] = eigen_value
                    content['eigen_vectors'] = list(eigen_vectors)
                    content['convergenceInterationNumber'] = steps
                    content['useErrors'] = use_errors



                elif(self.ICOD==2):
                    print("Jacobi Method")
                    [eigen_values, eigen_vectors, steps, determinant, use_errors] = solve_jacobi_method(self.matrix_a, self.TOL_m)
                    content['eigen_values'] = list(eigen_values)
                    content['eigen_vectors'] = list(eigen_vectors)
                    content['convergenceInterationNumber'] = steps
                    content['useErrors'] = use_errors

            if(not isinstance(self.IDET, int)):
                content['useErrors'] = "Insira um IDET inteiro no arquivo de configurações"
            
            else:   
                if(self.IDET>0):

                    content["determinant"] = solve_jacobi_method(self.matrix_a, self.TOL_m)[3]

        write_output_file(content)