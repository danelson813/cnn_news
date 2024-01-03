import logging
import os.path
import pandas as pd
import sqlite3 as sql


def setup_logger() -> 'logging.Logger':
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("data/info.log")
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s | %(pathname)s - %(lineno)d | %(levelname)s: %(message)s",
                                  datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # logger.info("This is an info message")
    # logger.error("This is an error message")
    # logger.warning("This is a warning message")
    # logger.debug("This is a debug message")
    # logger.critical("This is a critical message")
    logger.info("The logger has been started . . .")
    
    return logger


def does_it_exist(filename: str) -> bool:
    path = filename
    check_file = os.path.isfile(path)
    return check_file


def dataframe(list: list) -> 'pd.core.frame.DataFrame':
    df = pd.DataFrame(list)
    df.to_csv("data/results.csv", index=False)
    return df


def to_sqlite3(df: 'pd.core.frame.DataFrame'):
    # write the new DataFrame to a new SQLite table
    conn = sql.connect('data/cnn_news.sqlite')
    df.to_sql("news", conn, if_exists='replace')
    conn.close()

if __name__ == "__main__":
    setup_logger()