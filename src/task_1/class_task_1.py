from src.task_1.decomposition.LU import solve_decomposition_LU
from src.task_1.decomposition.Cholesky import solve_decomposition_Cholesky
from src.task_1.iterative_procedure.Jacobi import solve_jacobiano
from src.task_1.iterative_procedure.Gauss_Seidel import solve_gauss_seidel
from src.utils.files import write_output_file

class task_1:

    def __init__(self, ICOD, matrixA, vectorB, TOLm):

        self.ICOD = ICOD
        self.matrixA = matrixA
        self.vectorB = vectorB
        self.TOLm = TOLm


    def run(self):

        content = {'solution': [],
                'useErrors': []
            }
        
        if(not isinstance(self.ICOD, int)  or (self.ICOD!=1 and self.ICOD!=2 and self.ICOD!=3 and self.ICOD!=4 )):
            content['useErrors'] = "Insira um ICOD inteiro no arquivo de configurações"
        
        else:

            if(self.ICOD==3 or self.ICOD==4):
                content = {'solution': [],
                        'useErrors': [],
                        'determinant': 0,
                        'convergenceInterationNumber': 0,
                        'historical_residues': ''
                    }

            if(self.ICOD==1):
                print("LU")
                [soluction_LU, use_errors]  = solve_decomposition_LU(self.matrixA, self.vectorB)
                content['solution'] = list(soluction_LU)
                content['useErrors'] = use_errors

            elif(self.ICOD==2):
                print("Cholesky")
                [soluction_Cholesky, use_errors] = solve_decomposition_Cholesky(self.matrixA, self.vectorB)
                content['solution'] = list(soluction_Cholesky)
                content['useErrors'] = use_errors

            elif(not isinstance(self.TOLm, float)):
                content['useErrors'] = "Insira uma valor de tolerância float no arquivo de configurações"
            
            else:
                if(self.ICOD==3):
                    print("Jacobi")
                    [soluction_Jacobi, historical_residues, step, use_errors]= solve_jacobiano(self.matrixA, self.vectorB, self.TOLm)
                    content['solution'] = list(soluction_Jacobi)
                    content['convergenceInterationNumber'] = step
                    content['historical_residues'] = historical_residues
                    content['useErrors'] = use_errors

                
                elif(self.ICOD==4):
                    print("Gauss-Seidel")
                    [soluction_gauss_seidel, historical_residues, step, use_errors]= solve_gauss_seidel(self.matrixA, self.vectorB, self.TOLm)
                    content['solution'] = list(soluction_gauss_seidel)
                    content['convergenceInterationNumber'] = step
                    content['historical_residues'] = historical_residues
                    content['useErrors'] = use_errors
                    
            
            write_output_file(content)