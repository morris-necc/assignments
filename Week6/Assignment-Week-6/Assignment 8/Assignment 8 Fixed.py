pokemon_names = "audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask"

def shiritori(names): #I put it all inside a function in case you want to use it for a different word set for some reason
    ordered_dictionary = {}
    for string in names.split():
        if string[-1] not in ordered_dictionary:
            ordered_dictionary[string[-1]] = []
        if string[0] in ordered_dictionary:
            ordered_dictionary[string[0]].append(string)
        else:
            ordered_dictionary[string[0]] = [string]
        
    longest_sequence = []
    length = 0

    def find_longest(temp_sequence, choices):
        nonlocal longest_sequence, length, ordered_dictionary

        if choices: #if sequence leads somewhere, explore every possibility
            for next_word in choices:
                if next_word not in temp_sequence:
                    find_longest(temp_sequence+[next_word], ordered_dictionary[next_word[-1]])
        else: #if sequence has no more choices, check if it's longest
            if len(temp_sequence) > len(longest_sequence):
                longest_sequence, length = temp_sequence, len(temp_sequence)

    for name in names.split():
        find_longest([name], ordered_dictionary[name[-1]])
    
    print(longest_sequence, length)

shiritori(pokemon_names)