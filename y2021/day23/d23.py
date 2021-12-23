import functools
import itertools


def rooms_to_state(rooms):
    state = ('',) * 2
    for room in rooms:
        state += (room,) + ('',)

    state += ('',)

    return state


def read_input(filename, add_extra=False):
    if filename == "example.txt":
        rooms = [('b', 'a'), ('c', 'd'), ('b', 'c'), ('d', 'a')]
    else:
        rooms = [('a', 'b'), ('c', 'a'), ('b', 'd'), ('d', 'c')]

    if add_extra:
        extra_beasts = [('d', 'd'), ('c', 'b'), ('b', 'a'), ('a', 'c')]
        rooms = [r[:1] + eb + r[-1:] for r, eb in zip(rooms, extra_beasts)]

    state = rooms_to_state(rooms)

    return state


def valid_hallway_positions(state, room_pos):

    def crawler(d):
        pos = room_pos + d
        while -1 < pos < len(state):
            if pos in ROOM_POS:  # Cannot stop in front of room
                pos += d
                continue

            if state[pos]:  # hallway blocked
                break

            yield pos

            pos += d

    return itertools.chain(crawler(-1), crawler(1))


def is_blocked(state, hallway_pos, room_pos):
    if room_pos < hallway_pos:
        lower = room_pos
        upper = hallway_pos
    else:
        lower = hallway_pos + 1
        upper = room_pos

    for i in range(lower, upper):
        if i in ROOM_POS:
            continue
        if state[i]:
            return True

    return False


def beast_to_hallway(state, room_pos, hallway_pos):
    new_state = state[:hallway_pos] + (state[room_pos][0],) + state[hallway_pos + 1:]
    new_state = new_state[:room_pos] + (state[room_pos][1:],) + new_state[room_pos + 1:]

    return new_state


def beast_to_room(state, room_pos, hallway_pos):
    new_state = (
            state[:room_pos] +
            ((state[hallway_pos],) + state[room_pos],) +
            state[room_pos + 1:]
    )
    new_state = new_state[:hallway_pos] + ('',) + new_state[hallway_pos + 1:]

    return new_state


@functools.cache
def best_cost_to_done(state):
    if state == DONE:
        return 0

    best_cost = 999999999999

    # Now we need to make moves

    # Room -> Hallway
    for room_pos in ROOM_POS:
        room = state[room_pos]

        if not room:  # room is empty
            continue

        beast = room[0]

        # Check if the beast should move out
        if all(CORRECT_ROOM[b] == room_pos for b in room):
            continue

        steps_out_room = ROOM_SIZE - len(room) + 1  # steps to reach hallway outside room

        for hallway_pos in valid_hallway_positions(state, room_pos):

            tot_moves = abs(room_pos - hallway_pos) + steps_out_room
            moves_cost = tot_moves * COSTS[beast]

            best_cost = min(
                best_cost,
                moves_cost + best_cost_to_done(
                    beast_to_hallway(state, room_pos, hallway_pos)
                )
            )

    # Hallway -> Room
    for hallway_pos in HALLWAY_POS:
        if not state[hallway_pos]:
            continue

        beast = state[hallway_pos]
        correct_room_pos = CORRECT_ROOM[beast]

        # Check if the beast should move home
        if not all(CORRECT_ROOM[b] == correct_room_pos for b in state[correct_room_pos]):
            continue

        # Check if the beast can move home
        if is_blocked(state, hallway_pos, correct_room_pos):
            continue

        moves_to_room = abs(correct_room_pos - hallway_pos)
        moves_in_room = ROOM_SIZE - len(state[correct_room_pos])
        tot_moves = moves_in_room + moves_to_room
        move_cost = tot_moves * COSTS[beast]

        best_cost = min(
            best_cost,
            move_cost + best_cost_to_done(
                beast_to_room(state, correct_room_pos, hallway_pos)
            )
        )

    return best_cost



if __name__ == "__main__":
    do_example = False
    input_file = "example.txt" if do_example else "input.txt"

    HALLWAY_POS = [0, 1, 3, 5, 7, 9, 10]
    ROOM_POS = [2, 4, 6, 8]
    CORRECT_ROOM = {'a': 2, 'b': 4, 'c': 6, 'd': 8}

    COSTS = {'a': 1, 'b': 10, 'c': 100, 'd': 1000}

    initial_state = read_input(input_file, add_extra=False)

    ROOM_SIZE = len(initial_state[ROOM_POS[0]])
    DONE = rooms_to_state([(t, ) * ROOM_SIZE for t in ['a', 'b', 'c', 'd']])

    res = best_cost_to_done(initial_state)

    print('Part 1:', res)

    initial_state = read_input(input_file, add_extra=True)

    ROOM_SIZE = len(initial_state[ROOM_POS[0]])
    DONE = rooms_to_state([(t,) * ROOM_SIZE for t in ['a', 'b', 'c', 'd']])  # noqa

    res = best_cost_to_done(initial_state)

    print('Part 2:', res)
