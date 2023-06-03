#Kenneth Tran
#structure and debugging with the help of ChatGPT
class TuringMachine:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4'}
        self.input_alphabet = {'a', 'b'}
        self.tape_alphabet = {'a', 'b', 'E'}
        self.blank_symbol = 'E'
        self.initial_state = 'q0'
        self.accept_state = 'q4'
        self.reject_state = None
        self.transitions = {
            ('q0', 'a'): ('q1', 'a', 'R'),
            ('q0', 'b'): ('q0', 'b', 'R'),
            ('q0', 'E'): ('q4', 'b', 'L'),
            ('q1', 'a'): ('q2', 'a', 'L'),
            ('q1', 'b'): ('q0', 'b', 'R'),
            ('q1', 'B'): ('q2', 'B', 'L'),
            ('q2', 'a'): ('q3', 'E', 'R'),
            ('q3', 'a'): ('q0', 'E', 'R'),
        }

    def run(self, input_string):
        tape = list(input_string)
        tape.append('E')  # Appending blank symbol at the end
        current_state = self.initial_state
        head_position = 0

        while current_state != 'q4':
            current_symbol = tape[head_position]
            transition = self.transitions.get((current_state, current_symbol))

            if transition is None:
                current_state = self.reject_state
                break

            new_state, new_symbol, move_direction = transition
            tape[head_position] = new_symbol

            if move_direction == 'L':
                head_position -= 1
            elif move_direction == 'R':
                head_position += 1

            current_state = new_state

            # Display snapshot
            self.display_snapshot(current_state, tape, head_position)

        if current_state == self.accept_state:
            print("Input accepted.")
        elif current_state == self.reject_state:
            print("Input rejected.")

    def display_snapshot(self, current_state, tape, head_position):
        tape_str = "".join(tape)
        snapshot = f"State: {current_state}\nTape:  {tape_str}\n" + " " * (7 + head_position) + "^"
        print(snapshot)
        print()


# Example usage
input_string = input("Enter input string: ")
tm = TuringMachine()
tm.run(input_string)
