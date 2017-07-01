import unittest,Algorithms,Linking,math

class Test_algorithm(unittest.TestCase):
    g=Linking.Graph()
    gd=Linking.Grid(3,3)#3*3 grid

    # 3 layer absolutely complete perfect tree
    for i in range(7):
        g.add_vertex(i)

    g.add_edge(1,4,1)
    g.add_edge(1,3,1)
    g.add_edge(2,6,1)
    g.add_edge(2,5,1)
    g.add_edge(0,2,1)
    g.add_edge(0,1,1)

    AL=Algorithms.algorithms(g.vert_dict)
    AL_gd=Algorithms.algorithms(gd.grid_dict)

#For Graph data structure
    def test_bdfs_bfs(self):
        #BFS
        self.assertEqual([0,1,4],self.AL.bdfs(0,4,'BFS'))#Test BFS final path
        qsExpect=[[0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs(self):
        #DFS
        self.assertEqual([0,1,4],self.AL.bdfs(0,4,'DFS'))#Test DFS final path
        qsExpect=[[0, [1, 2]], [2, [1, 5, 6]], [6, [1, 5]], [5, [1]], [1, [3, 4]], [4, [3]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 6], [0, 2, 6, 5], [0, 2, 6, 5, 1], [0, 2, 6, 5, 1, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs(self):
        #UCS
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'UCS'))#Test UCS final path
        qsExpect=[[0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar(self):
        #A* (manual heuristic)
        self.g.setManualHeuristic(1,1)
        self.g.setManualHeuristic(3,1)
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [2, 1]], [2, [1, 5, 6]], [1, [5, 6, 4, 3]], [5, [6, 4, 3]], [6, [4, 3]], [4, [3]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0, 2, 1, 5], [0, 2, 1, 5, 6], [0, 2, 1, 5, 6, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
        self.g.setManualHeuristic(1,0)#set it back, otherwise it will infulence other testing
        self.g.setManualHeuristic(3,0)#set it back, otherwise it will infulence other testing
        #A* (default heuristic=0)
        self.assertEqual([0,1,4],self.AL.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
    def test_bdfs_bfs_iter(self):
        #BFS
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'BFS',it=3))#Test BFS final path
        qsExpect=[[0, [1, 2]], [1, [2]], [2, []], [0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs_iter(self):
        #DFS
        self.assertEqual([0,2,5],self.AL.iterative(0,5,'DFS',it=3))#Test DFS final path
        qsExpect=[[0, [1, 2]], [2, [1]], [1, []],[0, [1, 2]], [2, [1, 5, 6]], [6, [1, 5]], [5, [1]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0], [0, 2], [0, 2, 6], [0, 2, 6, 5]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs_iter(self):
        #UCS
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'UCS',it=3))#Test UCS final path
        qsExpect=[[0, [1, 2]], [1, [2]], [2, []], [0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_iter(self):
        #A* (manual heuristic)
        self.g.setManualHeuristic(1,1)
        self.g.setManualHeuristic(3,1)
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'aStar',it=3))#Test A* final path
        qsExpect=[[0, [2, 1]], [2, [1]], [1, []], [0, [2, 1]], [2, [1, 5, 6]], [1, [5, 6, 4, 3]],[5, [6, 4, 3]], [6, [4, 3]], [4, [3]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 2], [0, 2, 1], [0], [0, 2], [0, 2, 1], [0, 2, 1, 5], [0, 2, 1, 5, 6], [0, 2, 1, 5, 6, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog
        self.g.setManualHeuristic(1,0)#set it back, otherwise it will infulence other testing
        self.g.setManualHeuristic(3,0)#set it back, otherwise it will infulence other testing
        #A* (default heuristic=0)
        self.assertEqual([0,1,4],self.AL.iterative(0,4,'aStar',it=3))#Test A* final path
        qsExpect=[[0, [1, 2]], [1, [2]], [2, []], [0, [1, 2]], [1, [2, 3, 4]], [2, [3, 4, 5, 6]], [3, [4, 5, 6]], [4, [5, 6]]]
        self.assertEqual(qsExpect,self.AL.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 2], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4]]
        self.assertEqual(visitedExpect,self.AL.getVisitedLog())#Test A* visitedLog



#For Grid data structure
    def test_bdfs_bfs_grid(self):
        #BFS
        self.assertEqual([0,1,4],self.AL_gd.bdfs(0,4,'BFS'))#Test BFS final path
        qsExpect=[[0, [1, 3]], [1, [3, 2, 4]], [3, [2, 4, 6]], [2, [4, 6, 5]], [4, [6, 5]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs_grid(self):
        #DFS
        self.assertEqual([0,3,4],self.AL_gd.bdfs(0,4,'DFS'))#Test DFS final path
        qsExpect=[[0, [1, 3]], [3, [1, 4, 6]], [6, [1, 4, 7]], [7, [1, 4, 8]], [8, [1, 4, 5]], [5, [1, 4, 2]], [2, [1, 4]], [4, [1]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 3], [0, 3, 6], [0, 3, 6, 7], [0, 3, 6, 7, 8], [0, 3, 6, 7, 8, 5], [0, 3, 6, 7, 8, 5, 2], [0, 3, 6, 7, 8, 5, 2, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs_grid(self):
        #UCS
        self.assertEqual([0,1,4],self.AL_gd.ucsAStar(0,4,'UCS'))#Test UCS final path
        qsExpect=[[0, [1, 3]], [1, [3, 2, 4]], [3, [2, 4, 6]], [2, [4, 6, 5]], [4, [6, 5]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_grid(self):
        #A* (getManhattanDist)
        self.gd.setManhattanDist(4)
        self.assertEqual([0,1,4],self.AL_gd.ucsAStar(0,4,'aStar'))#Test A* final path
        qsExpect=[[0, [1, 3]], [1, [3, 4, 2]], [3, [4, 2, 6]], [4, [2, 6]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0, 1, 3, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test A* visitedLog
    def test_bdfs_bfs_iter_grid(self):
        #BFS
        self.assertEqual([0,3,6],self.AL_gd.iterative(0,6,'BFS',it=3))#Test BFS final path
        qsExpect=[[0, [1, 3]], [1, [3]], [3, []], [0, [1, 3]], [1, [3, 2, 4]], [3, [2, 4, 6]], [2, [4, 6]], [4, [6]], [6, []]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test BFS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4], [0, 1, 3, 2, 4, 6]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test BFS visitedLog
    def test_bdfs_dfs_iter_grid(self):
        #DFS
        self.assertEqual([0,3,6],self.AL_gd.iterative(0,6,'DFS',it=3))#Test DFS final path
        qsExpect=[[0, [1, 3]], [3, [1]], [1, []],[0, [1, 3]], [3, [1, 4, 6]], [6, [1, 4]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test DFS qsLog
        visitedExpect=[[0], [0, 3], [0, 3, 1], [0], [0, 3], [0, 3, 6]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test DFS visitedLog
    def test_ucsAStar_ucs_iter_grid(self):
        #UCS
        self.assertEqual([0,3,6],self.AL_gd.iterative(0,6,'UCS',it=3))#Test UCS final path
        qsExpect=[[0, [1, 3]], [1, [3]], [3, []], [0, [1, 3]], [1, [3, 2, 4]], [3, [2, 4, 6]], [2, [4, 6]], [4, [6]], [6, []]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test UCS qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0], [0, 1], [0, 1, 3], [0, 1, 3, 2], [0, 1, 3, 2, 4], [0, 1, 3, 2, 4, 6]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test UCS visitedLog
    def test_ucsAStar_aStar_iter_grid(self):
        #A* (getManhattanDist)
        self.gd.setManhattanDist(4)
        self.assertEqual([0,1,4],self.AL_gd.iterative(0,4,'aStar',it=3))#Test A* final path
        qsExpect=[[0, [1, 3]], [1, [3]], [3, []], [0, [1, 3]], [1, [3, 4, 2]], [3, [4, 2, 6]], [4, [2, 6]]]
        self.assertEqual(qsExpect,self.AL_gd.getQsLog())#Test A* qsLog
        visitedExpect=[[0], [0, 1], [0, 1, 3], [0], [0, 1], [0, 1, 3], [0, 1, 3, 4]]
        self.assertEqual(visitedExpect,self.AL_gd.getVisitedLog())#Test A* visitedLog
    def test_miniMaxAlphaBeta_miniMax(self):
        self.g.setManualHeuristic(3,20)
        self.g.setManualHeuristic(4,10)
        self.g.setManualHeuristic(5,5)
        self.g.setManualHeuristic(6,15)
        self.assertListEqual(self.AL.miniMaxAlphaBeta(0,3,'miniMax'),[{3: 20},
                                                                 {3: 20, 1: 20},
                                                                 {3: 20, 1: 20, 4: 10},
                                                                 {3: 20, 1: 10, 4: 10},
                                                                 {3: 20, 1: 10, 4: 10, 0: 10},
                                                                 {3: 20, 1: 10, 4: 10, 0: 10, 5: 5},
                                                                 {3: 20, 1: 10, 4: 10, 0: 10, 5: 5, 2: 5},
                                                                 {3: 20, 1: 10, 4: 10, 0: 10, 5: 5, 2: 5, 6: 15}])
        self.g.setManualHeuristic(3,0)
        self.g.setManualHeuristic(4,0)
        self.g.setManualHeuristic(5,0)
        self.g.setManualHeuristic(6,0)
    def test_miniMaxAlphaBeta_alphaBeta(self):
        self.g.setManualHeuristic(3,20)
        self.g.setManualHeuristic(4,1)
        self.g.setManualHeuristic(5,5)
        self.g.setManualHeuristic(6,30)
        #without prune
        self.assertListEqual(self.AL.miniMaxAlphaBeta(0,3,'alphaBeta'),[{3: 20},
                                                                   {3: 20, 1: 20},
                                                                   {3: 20, 1: 20, 4: 1},
                                                                   {3: 20, 1: 1, 4: 1},
                                                                   {3: 20, 1: 1, 4: 1, 0: 1},
                                                                   {3: 20, 1: 1, 4: 1, 0: 1, 5: 5},
                                                                   {3: 20, 1: 1, 4: 1, 0: 1, 5: 5, 2: 5},
                                                                   {3: 20, 1: 1, 4: 1, 0: 1, 5: 5, 2: 5, 6: 30},
                                                                   {3: 20, 1: 1, 4: 1, 0: 5, 5: 5, 2: 5, 6: 30}])
        #with prune
        self.g.setManualHeuristic(3,20)
        self.g.setManualHeuristic(4,10)
        self.g.setManualHeuristic(5,5)
        self.g.setManualHeuristic(6,15)
        self.assertListEqual(self.AL.miniMaxAlphaBeta(0,3,'alphaBeta'),[{3: 20},
                                                                   {3: 20, 1: 20},
                                                                   {3: 20, 1: 20, 4: 10},
                                                                   {3: 20, 1: 10, 4: 10},
                                                                   {3: 20, 1: 10, 4: 10, 0: 10},
                                                                   {3: 20, 1: 10, 4: 10, 0: 10, 5: 5},
                                                                   {3: 20, 1: 10, 4: 10, 0: 10, 5: 5, 2: 5}])#node 6 is pruned
        self.g.setManualHeuristic(3,0)
        self.g.setManualHeuristic(4,0)
        self.g.setManualHeuristic(5,0)
        self.g.setManualHeuristic(6,0)