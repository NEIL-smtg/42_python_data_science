from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def clean_data(data: list) -> list:
    """
    if val end with k or m, ignore last ch and multiply k
    or M and typecast to int
    """
    new = []
    for x in data:
        if x.endswith('k'):
            val = float(x[:-1]) * 1000
            new.append(int(val))
        elif x.endswith('M'):
            val = float(x[:-1]) * 1e7
            new.append(int(val))
        else:
            new.append(int(val))
    return new


def get_ylabels(val, _):
    """
    using dict to store formatter
    and return the value using val as key
    """
    labels = {
        2e8: '20M',
        4e8: '40M',
        6e8: '80M'
    }
    return labels.get(val)


def plotting(data: pd.DataFrame):
    """
    since there are only 300 col values, it
    starts at 1800 and ends with 2100
    so -50 or 251 as limit will be the upper
    bound of the plot
    """
    year = data.columns[1:-50].tolist()
    c1 = clean_data(data.values[0, 1:-50].tolist())
    c2 = clean_data(data.values[1, 1:-50].tolist())
    c1_name = data.values[0, 0]
    c2_name = data.values[1, 0]

    plt.plot(year, c1, label=c1_name, color='b')
    plt.plot(year, c2, label=c2_name, color='g')
    plt.title('Population Projection')
    plt.xlabel('Year')
    plt.ylabel('Population')

    xticks = year[::40]
    xlabels = [x for x in xticks]
    plt.xticks(xticks, xlabels)

    plt.yticks([2e8, 4e8, 6e8])
    ax = plt.gca()
    ax.yaxis.set_major_formatter(plt.FuncFormatter(get_ylabels))
    plt.legend(loc='lower right')
    plt.show()


def aff_pop():
    """
    set target and origin and search
    then plot
    """
    try:
        file = 'population_total.csv'
        err_msg = "AssertionError : csv not loaded."
        df = load(file)
        assert df is not None, err_msg

        target = 'France'
        origin = 'Malaysia'
        db = df[(df['country'] == target) | (df['country'] == origin)]
        plotting(db)
    except AssertionError as msg:
        print(msg)
    except KeyboardInterrupt:
        print("trl+c pressed...Exiting")


if __name__ == '__main__':
    aff_pop()
