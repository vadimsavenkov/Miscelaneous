def main():
    import pandas as pd
    dataset = pd.read_csv('time-series.txt')
    month = pd.to_datetime(dataset['month'], format='%b').dt.month
    timestamp = pd.DataFrame({'year': dataset['year'],'month': month,'day':1})
    dataset['timestamp'] = pd.to_datetime(timestamp)
    print(dataset)
    return dataset
main()
