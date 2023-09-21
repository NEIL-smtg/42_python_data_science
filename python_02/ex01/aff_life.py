from load_csv import load
from matplotlib import pyplot as plt
import pandas as pd


def plotting(data: pd.DataFrame, target):
    """
    -to extract year, read column and put to list,
    starting from column 1 to ignore name

    -to extract life, read values and slice from
    row 0, col 1

    -xticks = step size in x-axis (slicing = [start, stop, step])
    -xlabel = storing values of every 40 gap year into a list
    """
    year = data.columns[1:].tolist()
    life = data.values[0, 1:].tolist()

    plt.plot(year, life)
    plt.title(target + ' Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')

    xticks = year[::40]
    xlabels = [x for x in xticks]
    plt.xticks(xticks, xlabels)
    plt.show()


def aff_life():
    """
    exit when file not loaded
    df['country'] = extacting column named country
    if correspond country matches the target, it'll return true
    then search the dataframe where the row is true and store them
    into db
    """
    try:
        file = 'life_expectancy_years.csv'
        err_msg = "DataFrame not loaded"
        df = load(file)
        assert df is not None, err_msg

        target = 'France'
        db = df[df['country'] == target]
        plotting(db, target)

    except KeyboardInterrupt:
        print("trl+c pressed...Exiting")
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    aff_life()
