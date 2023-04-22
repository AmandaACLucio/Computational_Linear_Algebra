from src.task_1.decomposition.LU import solve_decomposition_LU
from src.task_1.decomposition.Cholesky import solve_by_cholesky
from src.task_1.iterative_procedure.Jacobi import jacobiano
from src.task_1.iterative_procedure.Gauss_Seidel import gauss_seidel
from src.utils.files import write_output_file
from src.task_2.jacobi_method import solve_jacobi_method


class task_1:

    def __init__(self, order, ICOD, IDET, matrixA, vectorB, TOLm):

        self.order=order
        self.ICOD = ICOD
        self.IDET = IDET
        self.matrixA = matrixA
        self.vectorB = vectorB
        self.TOLm = TOLm


    def run(self):

        content = {'solution': [],
                'useErrors': [],
                'determinant': 0,
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
                content['solution'] = soluction_LU
                content['useErrors'] = use_errors

            elif(self.ICOD==2):
                print("Cholesky")
                [soluction_Cholesky, use_errors] = solve_by_cholesky(self.matrixA, self.vectorB)
                content['solution'] = soluction_Cholesky
                content['useErrors'] = use_errors

            elif(not isinstance(self.TOLm, float)):
                content['useErrors'] = "Insira uma valor de tolerância float no arquivo de configurações"
            
            else:
                if(self.ICOD==3):
                    print("Jacobi")
                    [soluction_Jacobi, historical_residues, step, use_errors]= jacobiano(self.matrixA, self.vectorB, self.TOLm)
                    content['solution'] = soluction_Jacobi
                    content['convergenceInterationNumber'] = step
                    content['historical_residues'] = historical_residues
                    content['useErrors'] = use_errors

                
                elif(self.ICOD==4):
                    print("Gauss-Seidel")
                    [soluction_gauss_seidel, historical_residues, step, use_errors]= gauss_seidel(self.matrixA, self.vectorB, self.TOLm)
                    content['solution'] = soluction_gauss_seidel
                    content['convergenceInterationNumber'] = step
                    content['historical_residues'] = historical_residues
                    content['useErrors'] = use_errors


            if(not isinstance(self.IDET, int)):
                content['useErrors'] = "Insira um IDET inteiro no arquivo de configurações"
            
            else:   
                if(self.IDET>0):

                    content["determinant"] = solve_jacobi_method(self.matrixA, self.TOLm)[3]
                    
            
            write_output_file(content)