from emitter import Emitter
from receiver import Receiver
from photon import Photon
from mirror import Mirror

'''
BoardDisplayer - A helper class used to display the circuit board.
Each time a component is added to the circuit, this board is updated to 
store the component's symbol in its assigned position on the board.

'''


class BoardDisplayer:


    def __init__(self, width: int, height: int):
        '''
        Initialises a BoardDisplayer instance given a width and height 
        which is the size of the circuit board. board should be 
        initialised to the return value of the create_board method.

        width:  int             - the width of this board
        height: int             - the height of this board
        board:  list[list[str]] - a list of list of strings representing the 
                                  circuit board, having the symbol of each 
                                  component and photon in the circuit at its 
                                  assigned position

        Parameters
        ----------
        width  - the width to set this board to
        height - the height to set this board to
        '''
        self.width=width
        self.height=height
        self.board=self.create_board()


    def create_board(self) -> list[list[str]]:
        '''
        Creates a board of size width x height and returns it.

        Returns
        -------
        Returns a list of list of strings representing an empty circuit 
        board of size width x height.

        Example
        ------- 
        >>> self.width, self.height
        (8, 3)
        >>> create_board() # board split across multiple lines for readability
        [
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

        The board above has 3 rows (height), with each row having 8 columns (width).
        Each cell is initialised as a space, which represents an empty cell.
        '''
        board=[]
        i=0
        while i< self.height:
            board.append([])
            j=0
            while j< self.width:
                board[i].append(' ')
                j+=1
            i+=1
        return board
    def add_component_to_board(self, component: Emitter | Receiver | Mirror) -> None:
        '''
        Adds the symbol of the component on the board at its assigned 
        position.

        Parameters
        ----------
        component: the component to add its symbol on the board

        Hint
        ----------
        You shouldn't need to care what type of component you are adding,
        since all components have a symbol, x and y.
        
        >>> self.board # board split across multiple lines for readability
        [
         [' ', ' ', ' '], 
         [' ', ' ', ' '],
         [' ', ' ', ' ']
        ]
        >>> emitter = Emitter('A', 0, 0)
        >>> receiver = Receiver('R0', 2, 0)
        >>> self.add_component_to_board(emitter)
        >>> self.add_component_to_board(receiver)
        >>> self.board
        [
         ['A', ' ', '0'], 
         [' ', ' ', ' '],
         [' ', ' ', ' ']
        ]      
        '''
        self.board[component.get_y()][component.get_x()]=component.get_symbol() 
        return self.board


    def add_photon_to_board(self, photon: Photon) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Adds the symbol of the photon on the board at its current position. If
        there already is a component on the board at its position, it should not
        replace it.

        Parameters
        ----------
        photon: the photon to add its symbol on the board
        '''
        if self.board[photon.get_y()][photon.get_x()]==' ':
            self.board[photon.get_y()][photon.get_x()]=photon.get_symbol()

    def print_board(self) -> None:
        '''
        Prints a formatted board with the border included.

        Example 1
        ---------
        >>> self.board # board split across multiple lines for readability
        [
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]
        >>> self.print_board()
        +--------+
        |        |         
        |        |
        |        |
        +--------+

        Example 2
        ---------
        >>> self.board # board split across multiple lines for readability
        [
         ['A', ' ', ' ', ' ', ' ', ' ', ' ', '0'], 
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['B', ' ', ' ', ' ', ' ', ' ', ' ', '1']
        ]
        >>> self.print_board()
        +--------+
        |A      0|         
        |        |
        |B      1|
        +--------+

        Example 3
        ---------
        >>> self.board # board split across multiple lines for readability
        [
         ['A', '.', '.', '.', '.', '.', '.', '0'], 
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['B', '.', '.', '.', '.', '.', '.', '1']
        ]
        >>> self.print_board()
        +--------+
        |A......0|         
        |        |
        |B......1|
        +--------+
        '''
        print('+'+'-'*self.width+'+')
        i=0
        while i<len(self.board):
            row='|'
            j=0
            while j<len(self.board[0]):
                row=row+self.board[i][j]
                j+=1
            row=row+'|'
            print(row)
            i+=1
        print('+'+'-'*self.width+'+')
        return
        
           
