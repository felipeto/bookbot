def get_num_words(content):
    list_words = content.split()
    return len(list_words)

def character_count(content):
    content = content.lower()
    stats = {}
    for character in content:
        if character in stats:
            stats[character] += 1
        else:
            stats[character] = 1
    return stats

def sort_on(dict):
    return dict["num"]

def create_report(counts, character_stats):
    character_report = []
    for single_character in character_stats:
        single_character_dict = {
            "name": single_character,
            "num": character_stats[single_character]
        }
        character_report.append(single_character_dict)

    print(f"----------- Word Count ----------")
    print(f"Found {counts} total words")

    print(f"--------- Character Count -------")
    character_report.sort(reverse=True, key=sort_on)
    for single_character_report in character_report:
        print(f"{single_character_report['name']}: {single_character_report['num']}")
    
