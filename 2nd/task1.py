with open("C:/Users/jiayi/OneDrive/ETH/Rest/AdventofCode2023/2nd/input.txt") as file:
    result = []
    condition_met = False
    for count, game in enumerate(file):
        print("1added value: ", result)
        current_game = count+1
        game_split = game.split(':')
        gamenum = game_split[0]
        batch = game_split[1]
        print("count: ", count, "batch: ", batch) # count:  97 batch:   2 blue, 3 green, 6 red; 1 green, 1 blue, 8 red; 8 red, 3 green, 1 blue; 2 blue; 8 red, 2 green, 2 blue
        batch_split = batch.split(';')

        # Reset condition_met for each game
         # problem1: on at the first error, condition_met is set to True, but current count is still being appended to results! <-> 
            # problem2: we dont get to elif green and elif red!!! -------------->>>>>>>>> if instead of elif!!!!!!! Otherwise it only goes to green if blue is true!!!
        # overwrite each array element of batch_split with ID or 0
        for batch_set in batch_split:
            set_new = batch_set.replace(',', '').replace('\n', '')
            set_split = set_new.split(' ')
            print("set_split: ", set_split)
            if 'blue' in set_split:
                blue_idx = set_split.index('blue')
                print("blue_idx", blue_idx)
                if int(set_split[blue_idx-1]) > 14:
                    condition_met = True
                    print("oh no blue! at ", count, set_split)
            if 'green' in set_split:
                green_idx = set_split.index('green')
                if int(set_split[green_idx-1]) > 13:
                    condition_met = True
                    print("oh no green! at ", count, set_split)
            if 'red' in set_split:
                red_idx = set_split.index('red')
                print("int(set_split[red_idx-1])", int(set_split[red_idx-1]))
                if int(set_split[red_idx-1]) > 12:
                    condition_met = True
                    print("oh no red! at ", count, set_split)
        print("we are at count and have condition_met = ", count, condition_met)

        if condition_met:
            print("1")
            condition_met = False
            print("2added value: ", result)
            continue
        else: 
            print("2")
            result.append(current_game)
            print("3added value: ", result)
        # If none of the conditions are met, append to the result list


    print("added value: ", result)
    endresult = sum(result)
    print(endresult)

    print(sum([1, 2, 3, 4, 6, 8, 9, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100]))
