import pandas as pd


class Song:
    ap_score = 10000000
    records: list = []
    name: str = None
    levels: list = []

    def __init__(self, name: str, levels: list):
        self.name = name
        self.levels = levels

    def set_record(self, records: list):
        self.records = records

    def __str__(self):
        return f"{self.name}\t{self.levels}\t{self.records}"


def create_songs() -> list:
    """
    生成曲目信息列表
    """
    songs_data = pd.read_excel("Arcaea_songs.xlsx", "Table 0")
    songs_data.columns = ['name', 'PST', 'PRS', 'FTR', 'BYD', 'ETR',
                          'record_pst', 'record_prs', 'record_ftr',
                          'record_byd', 'record_etr']
    number = len(songs_data.index)
    songs_data.fillna(0, inplace=True)
    songs = []  # 曲库列表
    for i in range(number):
        song = Song(songs_data.loc[i, 'name'],
                    [songs_data.loc[i, 'PST'],
                     songs_data.loc[i, 'PRS'],
                     songs_data.loc[i, 'FTR'],
                     songs_data.loc[i, 'BYD'],
                     songs_data.loc[i, 'ETR']])

        song.set_record([songs_data.loc[i, 'record_pst'],
                         songs_data.loc[i, 'record_prs'],
                         songs_data.loc[i, 'record_ftr'],
                         songs_data.loc[i, 'record_byd'],
                         songs_data.loc[i, 'record_etr']])

        songs.append(song)

    return songs


def get_songs_main():
    songs = create_songs()
    print("get_songs")
    return songs


if __name__ == "__main__":
    get_songs_main()
