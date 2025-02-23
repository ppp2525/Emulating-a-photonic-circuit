'''

This test program checks if the set_pulse_sequence function is implemented
correctly.

'''


from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence


def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    """Positive test case to verify the set_pulse_sequence function.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    """
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    # Check if emitter's A pulse sequence is correctly set up
    assert my_circuit.emitters[0].get_symbol() == 'A', 'This should be emitter A'
    assert my_circuit.emitters[0].get_frequency() == 150, 'Emitter A has wrong frequency'
    assert my_circuit.emitters[0].get_direction() == 'S', 'Emitter A has wrong direction'
    # Check if emitter's B pulse sequence is correctly set up
    assert my_circuit.emitters[1].get_symbol() == 'B', 'This should be emitter B'
    assert my_circuit.emitters[1].get_frequency() == 200, 'Emitter B has wrong frequency'
    assert my_circuit.emitters[1].get_direction() == 'W', 'Emitter B has wrong direction'
    # Check if emitter's C pulse sequence is correctly set up
    assert my_circuit.emitters[2].get_symbol() == 'C', 'This should be emitter C'
    assert my_circuit.emitters[2].get_frequency() == 400, 'Emitter C has wrong frequency'
    assert my_circuit.emitters[2].get_direction() == 'N', 'Emitter C has wrong direction'
    
    file_obj.close()


def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    """Positive test case to verify the set_pulse_sequence function.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    """
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    # Check if emitter's A pulse sequence is correctly set up
    assert my_circuit.emitters[0].get_symbol() == 'A', 'This should be emitter A'
    assert my_circuit.emitters[0].get_frequency() == 120, 'Emitter A has wrong frequency'
    assert my_circuit.emitters[0].get_direction() == 'N', 'Emitter A has wrong direction'
    # Check if emitter's B pulse sequence is correctly set up
    assert my_circuit.emitters[1].get_symbol() == 'B', 'This should be emitter B'
    assert my_circuit.emitters[1].get_frequency() == 210, 'Emitter B has wrong frequency'
    assert my_circuit.emitters[1].get_direction() == 'S', 'Emitter B has wrong direction'
    # Check if emitter's C pulse sequence is correctly set up
    assert my_circuit.emitters[2].get_symbol() == 'C', 'This should be emitter C'
    assert my_circuit.emitters[2].get_frequency() == 350, 'Emitter C has wrong frequency'
    assert my_circuit.emitters[2].get_direction() == 'E', 'Emitter C has wrong direction'
    
    file_obj.close()

def negative_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    """Negative test case to verify the set_pulse_sequence function.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    """
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    # Check if emitter's A pulse sequence is correctly set up
    assert my_circuit.emitters[0].get_symbol() == 'A', 'This should be emitter A'
    assert my_circuit.emitters[0].get_frequency() == 100, 'Emitter A has wrong frequency'
    assert my_circuit.emitters[0].get_direction() == 'N', 'Emitter A has wrong direction'
    # Check if emitter's B pulse sequence is correctly set up
    assert my_circuit.emitters[1].get_symbol() == 'B', 'This should be emitter B'
    assert my_circuit.emitters[1].get_frequency() == 200, 'Emitter B has wrong frequency'
    assert my_circuit.emitters[1].get_direction() == 'E', 'Emitter B has wrong direction'
    # Check if emitter's C pulse sequence is correctly set up
    assert my_circuit.emitters[2].get_symbol() == 'C', 'This should be emitter C'
    assert my_circuit.emitters[2].get_frequency() == 350, 'Emitter C has wrong frequency'
    assert my_circuit.emitters[2].get_direction() == 'E', 'Emitter C has wrong direction'
    
    file_obj.close()

def negative_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    """Negative test case to verify the set_pulse_sequence function.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    """
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    # Check if emitter's A pulse sequence is correctly set up
    assert my_circuit.emitters[0].get_symbol() == 'A', 'This should be emitter A'
    assert my_circuit.emitters[0].get_frequency() == 100, 'Emitter A has wrong frequency'
    assert my_circuit.emitters[0].get_direction() == 'N', 'Emitter A has wrong direction'
    # Check if emitter's B pulse sequence is correctly set up
    assert my_circuit.emitters[1].get_symbol() == 'B', 'This should be emitter B'
    assert my_circuit.emitters[1].get_frequency() == 200, 'Emitter B has wrong frequency'
    assert my_circuit.emitters[1].get_direction() == 'E', 'Emitter B has wrong direction'
    # Check if emitter's C pulse sequence is correctly set up
    assert my_circuit.emitters[2].get_symbol() == 'C', 'This should be emitter C'
    assert my_circuit.emitters[2].get_frequency() == 350, 'Emitter C has wrong frequency'
    assert my_circuit.emitters[2].get_direction() == 'E', 'Emitter C has wrong direction'
    
    file_obj.close()

def edge_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    """Edge test case to verify the set_pulse_sequence function.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    """
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    # Check if emitter's A pulse sequence is correctly set up
    assert my_circuit.emitters[0].get_symbol() == 'A', 'This should be emitter A'
    assert my_circuit.emitters[0].get_frequency() == 100, 'Emitter A has wrong frequency'
    assert my_circuit.emitters[0].get_direction() == 'N', 'Emitter A has wrong direction'
    # Check if emitter's B pulse sequence is correctly set up
    assert my_circuit.emitters[1].get_symbol() == 'B', 'This should be emitter B'
    assert my_circuit.emitters[1].get_frequency() == 200, 'Emitter B has wrong frequency'
    assert my_circuit.emitters[1].get_direction() == 'E', 'Emitter B has wrong direction'
    # Check if emitter's C pulse sequence is correctly set up
    assert my_circuit.emitters[2].get_symbol() == 'C', 'This should be emitter C'
    assert my_circuit.emitters[2].get_frequency() == 350, 'Emitter C has wrong frequency'
    assert my_circuit.emitters[2].get_direction() == 'E', 'Emitter C has wrong direction'
    
    file_obj.close()

def edge_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: 
    """Edge test case to verify the set_pulse_sequence function.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    """
    file_obj = open(pulse_file_path)
    set_pulse_sequence(my_circuit, file_obj)
    
    # Check if emitter's A pulse sequence is correctly set up
    assert my_circuit.emitters[0].get_symbol() == 'A', 'This should be emitter A'
    assert my_circuit.emitters[0].get_frequency() == 100, 'Emitter A has wrong frequency'
    assert my_circuit.emitters[0].get_direction() == 'N', 'Emitter A has wrong direction'
    # Check if emitter's B pulse sequence is correctly set up
    assert my_circuit.emitters[1].get_symbol() == 'B', 'This should be emitter B'
    assert my_circuit.emitters[1].get_frequency() == 200, 'Emitter B has wrong frequency'
    assert my_circuit.emitters[1].get_direction() == 'E', 'Emitter B has wrong direction'
    # Check if emitter's C pulse sequence is correctly set up
    assert my_circuit.emitters[2].get_symbol() == 'C', 'This should be emitter C'
    assert my_circuit.emitters[2].get_frequency() == 350, 'Emitter C has wrong frequency'
    assert my_circuit.emitters[2].get_direction() == 'E', 'Emitter C has wrong direction'
    
    file_obj.close()

if __name__ == '__main__':
    # Run each function for testing
    positive_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence1.in')
    positive_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence2.in')
    negative_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence3.in')
    negative_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence4.in')
    edge_test_1(get_my_lasercircuit(), '/home/input/pulse_sequence5.in')
    edge_test_2(get_my_lasercircuit(), '/home/input/pulse_sequence6.in')

                   

