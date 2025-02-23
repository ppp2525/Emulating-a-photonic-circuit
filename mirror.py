from photon import Photon

'''
Mirror - A surface that reflect photons, changing the direction in which they 
travel. A photon may also become lost depending on the type of mirror and the
photon's initial direction when it reaches the mirror.

'''


class Mirror:
    

    def __init__(self, symbol: str, x: int, y: int):
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        Initialises a Mirror instance given a symbol, x and y value. 

        component_type: str - represents the type of component ('mirror')
        symbol:         str - the symbol of this mirror
                              ('/', '\', '>', '<', '^' or 'v')
        x:              int - x position of this mirror
        y:              int - y position of this mirror
        
        Parameters
        ----------
        symbol: str - the symbol to set this mirror to
        x:      int - the x position to set this mirror to
        y:      int - the y position to set this mirror to
        '''
        self.symbol=symbol
        self.x=x
        self.y=y
        self.component_type='mirror'



    def reflect_photon(self, photon: Photon) -> None:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''
        Reflects a photon off the surface of this mirror. If the photon has
        already been absorbed, you should return out early.
        
        Otherwise, the photon will travel in a new direction depending on the 
        type of mirror and its current direction. If the reflection causes the
        photon to be absorbed, the direction is not changed but the photon
        should be updated to get absorbed.

        Parameter
        ---------
        photon - the photon to reflect off this mirror
        '''
        if photon.is_absorbed():
            return
        if self.get_symbol()=='\\':
            if photon.get_direction()=='E':
                photon.direction='S'
            elif photon.get_direction()=='S':
                photon.direction='E'
            elif photon.get_direction()=='W':
                photon.direction='N'
            elif photon.get_direction()=='N':
                photon.direction='W'
        elif self.get_symbol()=='/':
            if photon.get_direction()=='E':
                photon.direction='N'
            elif photon.get_direction()=='N':
                photon.direction='E'
            elif photon.get_direction()=='W':
                photon.direction='S'
            elif photon.get_direction()=='S':
                photon.direction='W'
        elif self.get_symbol()=='>' or self.get_symbol()=='<':
            if photon.get_direction()=='S' or photon.get_direction()=='N':
                if self.get_symbol()=='>':
                    photon.direction='E'
                if self.get_symbol()=='<':
                    photon.direction='W'
            elif photon.get_direction()=='E':
                photon.got_absorbed()
            elif photon.get_direction()=='W':
                photon.got_absorbed()
        elif self.get_symbol()=='^' or self.get_symbol()=='v':
            if photon.get_direction()=='E' or photon.get_direction()=='W':
                if self.get_symbol()=='^':
                    photon.direction='N'
                if self.get_symbol()=='v':
                    photon.direction='S'
            elif photon.get_direction()=='N':
                photon.got_absorbed()
            elif photon.get_direction()=='S':
                photon.got_absorbed()
        
        
        
        


    def get_component_type(self) -> str:
        '''Returns component type.'''
        return self.component_type


    def get_symbol(self) -> str:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns symbol.'''
        return self.symbol

    
    def get_x(self) -> int:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns x.'''
        return self.x


    def get_y(self) -> int:
        # only requires implementation once you reach ADD-MY-MIRRORS
        '''Returns y.'''
        return self.y 
