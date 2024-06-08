import pandas as pd


def get_song_data(show_pre=False, show_new=False):
    pre_data = pd.read_excel("Arcaea_songs.xlsx", "Table 0")
    pre_data = pre_data.drop(columns=['record_pst',
                           'record_prs',
                           'record_ftr',
                           'record_byd',
                           'record_etr'],axis=1)
    pre_data.fillna(0, inplace=True)
    
    new_data = pd.read_excel("web_data.xlsx", "Table 0")
    new_data.fillna(0, inplace=True)

    if show_pre == True:
        print(pre_data)
    if show_new == True:
        print(new_data)
    
    return pre_data, new_data

def get_song_info(data):
    song_info = []
    for index, row in data.iterrows():
        song_info.append([row['曲目'],row['PST'],row['PRS'],
                          row['FTR'],row['BYD'],row['ETR']])
    return song_info

def find_unmatched_songs(pre_song_info, new_song_info):
    unmatched_songs = []
    for new_song in new_song_info:
        if not any(pre_song == new_song for pre_song in pre_song_info):
            unmatched_songs.append(new_song)
    return unmatched_songs

def create_new_dataframe(unmatched_songs):
    new_dataframe = pd.DataFrame(unmatched_songs, columns=['Name', 'PST', 'PRS', 'FTR', 'BYD', 'ETR'])
    return new_dataframe

    
def check_main():
    pre_data, new_data = get_song_data()
    pre_song_info = get_song_info(pre_data)
    new_song_info = get_song_info(new_data)

    unmatched_songs = find_unmatched_songs(pre_song_info, new_song_info)
    print("\n---UNMATCHED SONGS---")
    if unmatched_songs:
        new_dataframe = create_new_dataframe(unmatched_songs)
        new_dataframe.index += 1
        print(new_dataframe)
    else:
        print("No unmatched songs.")
    print()


if __name__ == "__main__":
    check_main()
