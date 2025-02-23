import sys
import input_parser
from emitter import Emitter
from receiver import Receiver
from mirror import Mirror
from laser_circuit import LaserCircuit
'''
run - Runs the entire program. It needs to take in the inputs and process them
into setting up the circuit. The user can specify optional flags to perform
additional steps, such as -RUN-MY-CIRCUIT to run the circuit and -ADD-MY-MIRRORS
to include mirrors in the circuit.

'''


def is_run_my_circuit_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Returns whether or not '-RUN-MY-CIRCUIT' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    i=0
    while i< len(args):
        if args[i]=='-RUN-MY-CIRCUIT':
            return True
        i+=1
    return False


def is_add_my_mirrors_enabled(args: list[str]) -> bool:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Returns whether or not '-ADD-MY-MIRRORS' is in args.
    
    Parameters
    ----------
    args - the command line arguments of the program
    '''
    i=0
    while i< len(args):
        if args[i]=='-ADD-MY-MIRRORS':
            return True
        i+=1
    return False


def initialise_circuit() -> LaserCircuit:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Gets the inputs for the board size, emitters and receivers and processes
    it to create a LaserCircuit instance and return it. You should be using
    the functions you have implemented in the input_parser module to handle
    validating each input.

    Returns
    -------
    A LaserCircuit instance with a width and height specified by the user's
    inputted size. The circuit should also include each emitter and receiver
    the user has inputted.
    '''
    print('Creating circuit board...')
    while True:
        x=input('> ')
        board=input_parser.parse_size(x)
        if board is not None:
            break
    width,height=board
    circuit=LaserCircuit(width,height)
    print(f'{width}x{height} board created.\n')
    print('Adding emitter(s)...')
    count=0
    while count<10:
        x=input('> ')
        if x=='END EMITTERS':
            break
        emitter=input_parser.parse_emitter(x)
        if emitter is not None:
            add=circuit.add_emitter(emitter)
            if add !=False:
                count+=1
    print(f'{count} emitter(s) added.\n')
    print('Adding receiver(s)...')
    count=0
    while count<10:
        x=input('> ')
        if x=='END RECEIVERS':
            break
        receiver=input_parser.parse_receiver(x)
        if receiver is not None:
            add=circuit.add_receiver(receiver)
            if add !=False:
                count+=1
    print(f'{count} receiver(s) added.\n')
    return circuit

def set_pulse_sequence(circuit: LaserCircuit, file_obj) -> None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Handles setting the pulse sequence of the circuit. 
    The lines for the pulse sequence will come from the a file named
    /home/input/<file_name>.in. 
    You should be using the functions you have implemented in the input_parser module 
    to handle validating lines from the file.

    Parameter
    ---------
    circuit - The circuit to set the pulse sequence for.
    file_obj - A file like object returned by the open()
    '''
    print('Setting pulse sequence...')
    name=[]
    i=0
    count=0
    while i< len(circuit.get_emitters()):
        name+=circuit.get_emitters()[i].get_symbol()
        i+=1
    check=True
    while check:
        line=file_obj.readline()
        if line !='':
            remain='-- ('
            j=0
            while j< len(name):
                remain+=name[j]+', '
                j+=1
            print(remain.strip(', ')+')')   
            count+=1
            print(f'Line {count}: {line.strip()}')
            pulse=input_parser.parse_pulse_sequence(line)
            if pulse==None:
                continue
            symbol, frequency,direction=pulse
            i=0
            while i< len(circuit.get_emitters()):
                if symbol==circuit.get_emitters()[i].get_symbol():
                    if circuit.get_emitters()[i].is_pulse_sequence_set():
                        print(f"Error: emitter '{symbol}' already has its pulse sequence set")
                        break
                    else:
                        circuit.get_emitters()[i].set_pulse_sequence(frequency,direction)
                        name.remove(symbol)
                        break
                i+=1
                if i==len(circuit.get_emitters()):
                    print(f"Error: emitter '{symbol}' does not exist")
        else:
            print('Pulse sequence set.')
            check=False
        
def add_mirrors(circuit: LaserCircuit) -> None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Handles adding the mirrors into the circuit. You should be using the
    functions you have implemented in the input_parser module to handle
    validating each input. 
    
    Parameters
    ----------
    circuit - the laser circuit to add the mirrors into
    '''
    print('Adding mirror(s)...')
    count=0
    while True:
        x=input('> ')
        if x=='END MIRRORS':
            break
        mirror=input_parser.parse_mirror(x)
        if mirror is not None:
            add=circuit.add_mirror(mirror)
            if add !=False:
                count+=1
    print(f'{count} mirror(s) added.')


def main(args: list[str]) -> None:
    # only requires implementation once you reach GET-MY-INPUTS
    # will require extensions in RUN-MY-CIRCUIT and ADD-MY-MIRRORS
    '''
    Responsible for running all code related to the program.

    Parameters
    ----------
    args - the command line arguments of the program
    '''
    run=initialise_circuit()
    if is_add_my_mirrors_enabled(args):
        print('<ADD-MY-MIRRORS FLAG DETECTED!>')
        print()
        add_mirrors(run)
        print()
    run.print_board()
    print()
    if is_run_my_circuit_enabled(args):
        print('<RUN-MY-CIRCUIT FLAG DETECTED!>')
        print()
        try:
            with open('/home/input/pulse_sequence.in','r') as f:
                set_pulse_sequence(run,f)
                print()
                run.run_circuit()
        except FileNotFoundError:
            print('Error: -RUN-MY-CIRCUIT flag detected but /home/input/pulse_sequence.in does not exist')

    
    
    




if __name__ == '__main__':
    '''
    Entry point of program. We pass the command line arguments to our main
    program. We do not recommend modifying this.
    '''
    main(sys.argv)
