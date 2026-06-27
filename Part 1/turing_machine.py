import logging
from itertools import islice


class TuringMachine:
    def __init__(self, transitions, start_state='q0', accept_state='qa', reject_state='qr', blank_symbol=''):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol

    def run(self, input_):
        symbols = list(input_)
        right_hand_side = []
        left_hand_side = []
        if not symbols:
            current_symbol = self.blank_symbol
        else:
            current_symbol = symbols[0]
            right_hand_side = symbols[1:]
        
        state = self.start_state
        while True:
            configuration = {
                "state" : state,
                "left_hand_side" : left_hand_side[:],
                "symbol" : current_symbol,
                "right_hand_side" : right_hand_side[:]
            }

            if state == self.accept_state:
                yield ('Accept', configuration)
                break
            elif state == self.reject_state:
                yield ('Reject', configuration)
                break
            else:
                yield (None, configuration)

            if (state, current_symbol) not in self.transitions:
                state = self.reject_state
                continue

            to_exe = self.transitions[(state, current_symbol)]

            state = to_exe[0]
            if to_exe[2] == 'R':
                left_hand_side.insert(0, to_exe[1])    
                if right_hand_side:
                    current_symbol = right_hand_side.pop(0)
                else:
                    current_symbol = self.blank_symbol
            elif to_exe[2] == 'L':
                right_hand_side.insert(0, to_exe[1])  
                if left_hand_side:
                    current_symbol = left_hand_side.pop(0)
                else:
                    logging.warning("Crossed left boundary of singly-infinite tape")
                    current_symbol = self.blank_symbol     
            else:
                raise ValueError(f"Invalid direction: {to_exe[2]}")
            
    def accepts(self, input_, step_limit=100):
        for action, _ in islice(self.run(input_), step_limit):
            if action == 'Accept':
                return True
            elif action == 'Reject':
                return False
            
        logging.warning("Step limit reached without halting")
        return None

    def rejects(self, input_, **kwargs):
        result = self.accepts(input_, **kwargs)
        if result is None:
            return None
        return not result

    def debug(self, input_, step_limit=100, colored=False):
        for i, (action, configuration) in enumerate(islice(self.run(input_), step_limit)):
            state = configuration['state']
            left = configuration['left_hand_side']
            symbol = configuration['symbol']
            right = configuration['right_hand_side']
            left_part = ''.join(reversed(left))
            right_part = ''.join(right)

            if colored:
                tape_str = f"{left_part}\033[91m[{symbol}]\033[0m{right_part}"
            else:
                tape_str = f"{left_part}[{symbol}]{right_part}"

            print(f"Step {i}: state={state}, tape={tape_str}")

            if action in ('Accept', 'Reject'):
                print(f"Finished with {action}")
                break
