import logging
from bot.bot import Bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)


def main():
    bot = Bot(logger)
    bot.run()


if __name__ == '__main__':
    main()
