import unittest

import CNYT
import CNYT2

class unit_imaginar(unittest.TestCase):
        
        def Test_AdicionVectoresComplejos(self):
                self.assertEqual(CNYT2.AdicionVectoresComplejos([[(1,2),(2,3),(3,4)]],[[(2,4),(4,6),(6,8)]],1),[[(3,6),(6,9),(9,12)]])

        def test_inversa(self):
                 self.assertEqual(CNYT2.inversaMatriz([(1,-1),(0,0),(1,1)]),[(1, -1), (0, 0), (1, 1)])

        def test_multiplicacion_escalarVector(self):
                self.assertEqual(CNYT2.EscalarporVector([(2,3),(4,5),(6,7)],5),[(10,15),(20,25),(30,35)])

        def test_adicion_matrices(self):
                self.assertEqual(CNYT2.AdicionMatricesComplejas([[(2,1),(0,0),(1,3)],[(1,0),(2,4),(3,5)]],[[(3,2),(4,3),(5,2)],[(3,2),(4,3),(5,2)]]),  [[(5, 3), (4, 3), (6, 5)], [(4, 2), (6, 7), (8, 7)]])

        def test_multiplicacion_escalar_matrices(self):
            self.assertEqual(CNYT2.multiplicacionEscalarMatrices([[(2,3),(4,5),(6,7)],[(1,3),(2,5),(8,7)],[(12,3),(24,5),(32,7)]],5),([[(10,15),(20,25),(30,35)],[(5,15),(10,25),(40,35)],[(60,15),(120,25),(160,35)]]))

        def test_transpuesta(self):
            self.assertEqual(CNYT2.traspuesta([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]),[[(1, 2), (1, 2)], [(2, 3), (2, 3)], [(3, 4), (3, 4)]])
        
    
        def test_norma(self):
            self.assertEqual(CNYT2.normaVector([[(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)]]),5.291502622129181)
        def test_distancia_entreVectores(self):
            self.assertEqual(CNYT2.distanciaEntreVectores([(1,0),(2,0)],[(1,0),(2,0)]),0)
        def test_unitaria(self):
            self.assertEqual(CNYT2.esUnitaria([[(1,3),(1,8)],[(1,2),(3,1)]]),False)

        def test_Hermitian(self):
                self.assertEqual(CNYT2.esHermitiana([[(1,3),(1,8)],[(1,2),(3,1)]]),False)          

      
unittest.main()
