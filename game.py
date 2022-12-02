"""
Emily Tran        A00990221
Sean Sollestre    A01333807
"""
import title_screen
import map
import encounter


def game():  # called from main
    """

    :return:
    """
    title_screen.title_screen()
    character = encounter.make_character()
    achieved_goal = False
    while not achieved_goal and character["health"] > 0:
        directions = ['w', 'a', 's', 'd']
        # commands = ['1','2','3','q']
        map.m.print_scenario()
        encounter.execute_glowup_protocol(character)
        valid_moves = enumerate(["Display character information", "Pick a fight", "Display Map"], 1)
        print("Actions available:\n")
        for count, value in valid_moves:
            print(str(count) + ":", value)
        print("q: Quit")
        move = input("\nPlease enter an action or direction [w, a, s, d]:")
        if move == '1':
            encounter.display_character_info(character)
        elif move == '2':
            encounter.execute_challenge_protocol(character)
        elif move == '3':
            map.m.print_map()
        elif move == 'q':
            break
        elif move in directions:
            map.m.move(move)
            encounter.chance_encounter(character)
        achieved_goal = encounter.check_if_goal_attained(character)
    if achieved_goal:
        title_screen.end_screen()


def main():
    """

    """
    game()
    # rows = 5
    # columns = 5
    # board = make_board(rows, columns)
    # character = make_character("Player name")
    # achieved_goal = False
    # while not achieved_goal:
    #     describe_current_location(board, character)
    #     direction = get_user_choice()
    #     valid_move = validate_move(board, character, direction)
    #     if valid_move:
    #         move_character(character)
    #         describe_current_location(board, character)
    #         there_is_a_challenge = check_for_challenges()
    #     if there_is_a_challenge:
    #         execute_challenge_protocol(character)
    #     if character_has_leveled():
    #         execute_glow_up_protocol()
    #         achieved_goal = check_if_goal_attained(board, character)
    #     else:
    #         print("A wall blocks your path.")
    # print("you have successfully escaped")


if __name__ == "__main__":
    main()
