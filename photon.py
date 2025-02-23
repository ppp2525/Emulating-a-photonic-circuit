'''

Photon - A particle of light that are emitted by emitters and travels along the
circuit board. Photons have a frequency (THz) and direction. They can interact 
with components in the circuit in which it may be absorbed. When a photon is
absorbed, they no longer move.

'''


class Photon:


    def __init__(self, x: int, y: int, frequency: int, direction: str):
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Initialises a Photon instance given an x and y position, as well as a
        frequency and direction. symbol is '.' and absorbed is False by
        default.

        symbol:    str  - the symbol of this photon ('.')
        x:         int  - x position of this photon
        y:         int  - x position of this photon
        frequency: int  - the frequency (THz) of this photon
        direction: str  - the direction in which this photon will travel 
                          ('N', 'E', 'S' or 'W')
        absorbed:  bool - whether or not this photon has been absorbed

        Parameters
        ----------
        x         - the x position to set this photon to
        y         - the y position to set this photon to
        frequency - the frequency to set this photon to
        direction - the direction to set this photon to
        '''
        self.symbol='.'
        self.x=x
        self.y=y
        self.frequency=frequency
        self.direction=direction
        self.absorbed=False


    def move(self, board_width: int, board_height: int) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Updates this photon's position to move one unit based on its direction.
        Do not move the photon if it has been absorbed.

        After moving the photon, if it is out-of-bounds based on the board_width
        and board_height given, you will need to update this photon to be 
        absorbed and set its position back so it's not out-of-bounds.

        Parameters
        ----------
        board_width  - width of circuit board 
        board_height - height of circuit board
        '''
        if self.is_absorbed():
            return
        if self.direction=='N':
            self.y-=1
            if self.y<0:
                self.y+=1
                self.got_absorbed()
        if self.direction=='E':
            self.x+=1
            if self.x==board_width:
                self.x-=1
                self.got_absorbed()
        if self.direction=='W':
            self.x-=1
            if self.x<0:
                self.x+=1
                self.got_absorbed()
        if self.direction=='S':
            self.y+=1
            if self.y==board_height:
                self.y-=1
                self.got_absorbed()
        

        

    def interact_with_component(self, component: object, timestamp: int) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        # will require extensions in ADD-MY-MIRRORS
        '''
        Handles this photon interacting with the passed in component where
        timestamp is when the photon collided with component. This method
        should return out early if the photon has already been absorbed.

        - If component is an emitter, nothing happens.
        - If component is a receiver, the receiver absorbs this photon and
          stores its energy.
        - If component is a mirror, the mirror reflects it off its surface.
        
        Parameters
        ----------
        component - the component to interact with, being an Emitter, Receiver 
                    or Mirror 
        timestamp - the time in nanoseconds when the photon collided with the
                    component

        Note
        ----
        If you need to query the type of component, use the component_type
        attribute. You cannot import the classes in this module due to
        circular dependencies.

        Example:
        >>> component.get_component_type()
        'emitter'
        '''
        if component.get_component_type()=='emitter':
            return
        if component.get_component_type()=='receiver':
            component.absorb_photon(self,timestamp)
        if component.get_component_type()=='mirror':
            component.reflect_photon(self)


        


    def got_absorbed(self) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Updates the absorbed attribute to represent an absorption.'''
        self.absorbed=True


    def is_absorbed(self) -> bool:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns absorbed.'''
        return self.absorbed


    def set_direction(self, direction: str) -> None:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''
        Sets the direction attribute of this photon. If the direction passed
        in is not 'N', 'E', 'S' or 'W', it does not set it.

        Parameters
        ----------
        direction - the new direction to set for this photon
        '''
        check='NEWS'
        i=0
        while i< len(check):
            if direction==check[i]:
                self.direction=direction
            i+=1


    def get_direction(self) -> str:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns direction.'''
        return self.direction

        
    def get_frequency(self) -> int:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns frequency.'''
        return self.frequency


    def get_symbol(self) -> str:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns symbol.'''
        return self.symbol

    
    def get_x(self) -> int:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns x.'''
        return self.x


    def get_y(self) -> int:
        # only requires implementation once you reach RUN-MY-CIRCUIT
        '''Returns y.'''
        return self.y
