from draw_image import make_image
from twitter_interface import get_twitter_api, fetch_statues
from config import TWITTER_HANDLERS


def run():
    api = get_twitter_api()

    for handler in TWITTER_HANDLERS:
        statues, user = fetch_statues(api, handler, count=20)

        for status in statues:
            make_image(user.name, status, verbose=True)


if __name__ == '__main__':
    run()

