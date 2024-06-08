import pandas
import pandas as pd
import get_songs as mySongs
import dataframe_image as dfi
import numpy as np

number = 40
difficulty_name = ['PST', 'PRS', 'FTR', 'BYD', 'ETR']


class Potential:
    name: str = None
    difficulty: int = 0
    level: float = 0.0
    record: int = 0
    ptt: float = 0.0

    def __init__(self, song: mySongs.Song, difficulty: int):
        self.name = song.name
        self.difficulty = difficulty
        self.level = song.levels[difficulty - 1]
        self.record = song.records[difficulty - 1]

    def __lt__(self, other):
        return self.ptt < other.ptt

    def __gt__(self, other):
        return self.ptt > other.ptt

    def __eq__(self, other):
        return self.ptt == other.ptt

    def calculate_ptt(self):
        if self.record >= 10000000:
            self.ptt = self.level + 2.0

        elif self.record >= 9800000:
            self.ptt = self.level + 1.0 + (self.record - 9800000) / 200000

        else:
            self.ptt = max(self.level + (self.record - 9500000) / 300000, 0)


def generate_sorted_ptt(songs: list) -> list:
    """
    产生降序单曲ptt对象列表
    """
    ptts = []
    for song in songs:
        for i in [1, 2, 3, 4, 5]:
            ptt = Potential(song, i)
            ptt.calculate_ptt()
            ptts.append(ptt)
    sorted_ptt = sorted(ptts, reverse=True)
    return sorted_ptt


def generate_b30_val(sorted_ptt: list) -> float:
    """
    计算b30的值
    """
    ptt_number = []
    for ptt_obj in sorted_ptt[0:29]:
        ptt_number.append(ptt_obj.ptt)
    return float(np.mean(ptt_number))


def generate_best_frame(sorted_ptt: list):
    """
    生成记录b40信息的dataframe
    """
    names = []
    difficulties = []
    levels = []
    records = []
    potentials = []
    b30_val = generate_b30_val(sorted_ptt)
    for i in range(number):
        names.append(sorted_ptt[i].name)
        difficulties.append(difficulty_name[sorted_ptt[i].difficulty - 1])
        levels.append(sorted_ptt[i].level)
        records.append(int(sorted_ptt[i].record))
        potentials.append(sorted_ptt[i].ptt)
    best_frame = pd.DataFrame({
        '歌名': names,
        '难度': difficulties,
        '定数': levels,
        '分数': records,
        'ptt (b30=%.2f)' % b30_val: potentials
    })
    best_frame.index = range(1, number + 1)
    return best_frame


def generate_image(best_frame: pandas.DataFrame):
    import time
    current_time = time.localtime()
    year = current_time.tm_year
    month = current_time.tm_mon
    day = current_time.tm_mday
    dfi.export(best_frame, f'{year:04d}-{month:02d}-{day:02d}-b{number}.png')


def calculate_main():
    songs = mySongs.get_songs_main()
    potentials = generate_sorted_ptt(songs)
    best_frame = generate_best_frame(potentials)
    generate_image(best_frame)


if __name__ == "__main__":
    calculate_main()
    print("calculate_ptt")
