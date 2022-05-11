from chessdotcom import get_leaderboards


def print_leaderboards():
    data = get_leaderboards()
    print(data.json)


print_leaderboards()
