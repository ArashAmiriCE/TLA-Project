from turing_machine import TuringMachine
from test_turing_machine import print_states

transitions = {
        ('q0', '1'): ('q1', '', 'R'),
        ('q0', '0'): ('q7', '', 'R'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', '0'): ('q2', '0', 'R'),
        ('q2', 'a'): ('q2', 'a', 'R'),
        ('q2', 'b'): ('q5', 'b', 'L'),
        ('q2', '1'): ('q3', 'a', 'R'),
        ('q3', '1'): ('q3', '1', 'R'),
        ('q3', 'b'): ('q3', 'b', 'R'),
        ('q3', '') : ('q4', 'b', 'L'),
        ('q4', '1'): ('q4', '1', 'L'),
        ('q4', 'b'): ('q4', 'b', 'L'),
        ('q4', 'a'): ('q2', 'a', 'R'),
        ('q5', 'a'): ('q5', '1', 'L'),
        ('q5', '0'): ('q6', '0', 'L'),
        ('q6', '1'): ('q6', '1', 'L'),
        ('q6', '') : ('q0', '', 'R'),
        ('q7', '1'): ('q7', '', 'R'),
        ('q7', 'b'): ('q7', '1', 'R'),
        ('q7', '') : ('q8', '', 'L'),
        ('q8', '1'): ('q8', '1', 'L'),
        ('q8', '') : ('qa', '', 'R')
}
if __name__ == "__main__":
    print_states(transitions)
    machine = TuringMachine(transitions)

    def run(input_):
        w = input_
        print("Input:",w)
        print("Accepted" if machine.accepts(w, step_limit=1000) else "Rejected")
        machine.debug(w, step_limit=1000, colored=True)

        print()

    # SHOULD ACCEPT
    run("110111")
    # outputs 111111

    # SHOULD ACCEPT
    run("11101111")
    # outputs 111111111111

    run("01111")
