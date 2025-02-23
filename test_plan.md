

**Test Cases**
Table 1. Summary of test cases for parse_pulse_sequence
| File Name             | Function Name   | Description                                            | Expected Error Message(s) (if any)    | Pass/Fail |
| --------------------- | ----------------| ------------------------------------------------------ | ------------------------------------- | --------- |
| pulse_sequence1.in    | positive_test_1 | Positive Case - Configure the frequency and direction  |No message                             | Pass      |
|                       |                 |  of 3 emitters(A,B,C).                                 |                                       |           |
| pulse_sequence2.in    | positive_test_2 | Positive Case - Configure the frequency and direction  |No message                             | Pass      |
|                       |                 |  of 3 emitters(A,B,C).                                 |                                       |           |
| pulse_sequence3.in    | negative_test_1 | Negative case: File containing invalid frequency(less  |Error: frequency must be greater than  | Pass      |
|                       |                 |  than zero) -> C -350 E                                | zero                                  |           |
| pulse_sequence4.in    | negative_test_2 | Negative case: File containing invalid emitter(not     |Error: emitter 'D' does not exist      | Pass      |
|                       |                 |  exist) -> D 350 E                                     |                                       |           |
| pulse_sequence5.in    | edge_test_1     | Edge case: File containing emitter B being called twice|Error: emitter 'B' already has its     | Pass      |                              
|                       |                 |  ->B 200 E                                             | pulse sequence set                    |           |
|                       |                 |    B 150 E                                             |                                       |           |
| pulse_sequence6.in    | edge_test_2     | Edge case: File containing a blank line between another|Error: <symbol> <frequency> <direction>| Pass      |
|                       |                 |  sequences ->A 100 N                                   |                                       |           | 
|                       |                 |              (blank)                                   |                                       |           | 
|                       |                 |              B 200 E                                   |                                       |           | 
|                       |                 |              C 350 E                                   |                                       |           | 

