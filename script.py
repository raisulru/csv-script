import pandas as pd


class QueryFromCsv:

    def __init__(self):
        self.url = 'https://press.radiocut.fm/bicycle-travels-jan-2018.csv'
        self.df = pd.DataFrame()
        self.start_time = '06:00:00'
        self.end_time = '11:59:59'
    
    def download_file(self):
        self.df = pd.read_csv(self.url)
    
    def setup_datetime_column(self):
        self.df['pickup_time'] = pd.to_datetime(self.df['pickup_time'])

    def filter_by_time_range(self):
        self.df = self.df[self.df.pickup_time.dt.strftime('%H:%M:%S').between('06:00:00','11:59:59')]

    def grouping_and_sorting_column(self):
        self.df = self.df.groupby(['source_station_name','source_station_code']).size().reset_index(name='counts')
        self.df = self.df.sort_values('counts', ascending=False)
        self.df = self.df[:5]

    def print_top_five(self):
        print(self.df)


if __name__ == "__main__":
    client = QueryFromCsv()
    client.download_file()
    client.setup_datetime_column()
    client.filter_by_time_range()
    client.grouping_and_sorting_column()
    client.print_top_five()