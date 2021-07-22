import csv
import pandas as pd
from config.settings import DATA_DIRS


class MyAnalysis:
    def forage(self, ott):
        df = pd.read_csv(DATA_DIRS[0] + '/MoviesOnStreamingPlatforms_updated.csv')
        df.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True)
        df['Age'].replace('all', '0+', inplace=True)
        AgeList = [0 for _ in range(5)]
        AgeRange = ['0+', '+7', '+13', '+16', '18+']

        for i in range(len(df)):
            if df.iloc[i][ott] == 1:
                if df.iloc[i]['Age'] == '0+':
                    AgeList[0] += 1
                elif df.iloc[i]['Age'] == '7+':
                    AgeList[1] += 1
                elif df.iloc[i]['Age'] == '13+':
                    AgeList[2] += 1
                elif df.iloc[i]['Age'] == '16+':
                    AgeList[3] += 1
                elif df.iloc[i]['Age'] == '18+':
                    AgeList[4] += 1
                else:
                    continue
        result = []
        for i in range(len(AgeRange)):
            d = []
            d.append(AgeRange[i])
            d.append(AgeList[i])
            result.append(d)
        print(result)
        return result

    def ImdbScatter(self, ott):
        df = pd.read_csv(DATA_DIRS[0] + '/MoviesOnStreamingPlatforms_updated.csv')
        df.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True)
        df = df.dropna(subset=["IMDb", "Runtime"])
        setott = df[ott] == 1
        setrun = df['Runtime'] <= 180
        x = df[setott & setrun]

        scatterdata = []
        colors = {'Netflix': '#C8FAC8', 'Hulu': '#ED561B', 'Prime Video': '#B4B4FF',
                  'Disney+': '#FF28A7'}

        for i in range(len(x)):
            run_im = []
            run_im.append(x.iloc[i]['Runtime'])
            run_im.append(x.iloc[i]['IMDb'])
            scatterdata.append(run_im)

        result = [
            {'name': ott, 'color': colors[ott], 'data': scatterdata}
        ]
        print(result)
        return result

    def ImdbRate(self, ott):
        df = pd.read_csv(DATA_DIRS[0] + '/MoviesOnStreamingPlatforms_updated.csv')
        df.drop(['Unnamed: 0', 'ID'], axis=1, inplace=True)
        x = df[df[ott] == 1]
        newdf = x.dropna(subset=["IMDb"])

        im1 = newdf[newdf['IMDb'] < 5]
        im2 = newdf[(newdf['IMDb'] >= 5) & (newdf['IMDb'] < 6)]
        im3 = newdf[(newdf['IMDb'] >= 6) & (newdf['IMDb'] < 7)]
        im4 = newdf[(newdf['IMDb'] >= 7) & (newdf['IMDb'] < 8)]
        im5 = newdf[(newdf['IMDb'] >= 8) & (newdf['IMDb'] < 9)]
        im6 = newdf[(newdf['IMDb'] >= 9) & (newdf['IMDb'] <= 10)]

        data = [{
            'name': '0.0~4.9', 'y': len(im1) / len(newdf) * 100
        }, {
            'name': '5.0~5.9', 'y': len(im2) / len(newdf) * 100
        }, {
            'name': '6.0~6.9', 'y': len(im3) / len(newdf) * 100
        }, {
            'name': '7.0~7.9', 'y': len(im4) / len(newdf) * 100
        }, {
            'name': '8.0~8.9', 'y': len(im5) / len(newdf) * 100
        }, {
            'name': '9.0~10.0', 'y': len(im6) / len(newdf) * 100
        }]
        return data


if __name__ == '__main__':
    # MyAnalysis().forage('Netflix')
    # MyAnalysis().ImdbScatter('Disney+')
    MyAnalysis().ImdbRate('Netflix')
