from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def clean_population(population_str):
    # Remove 'k' and 'M' characters and convert to integers
    if population_str.endswith('k'):
        return int(float(population_str[:-1]) * 1000)
    elif population_str.endswith('M'):
        return int(float(population_str[:-1]) * 1000000)
    else:
        return int(population_str)


def plotting(data: pd.DataFrame):
    # year = data.columns[1:].tolist()
    countries = data.values['country'].tolist()

    print(countries)

    # plt.title('Population Projection')
    # plt.xlabel('Year')
    # plt.ylabel('Population')

    # xticks = year[::40]
    # xlabels = [x for x in xticks]

    # plt.xticks(xticks, xlabels)
    # plt.legend()
    plt.show()


def aff_pop():
    try:
        file = 'population_total.csv'
        err_msg = "AssertionError : csv not loaded."
        df = load(file)
        assert df is not None, err_msg

        target = 'France'
        origin = 'Belgium'
        db = df[(df['country'] == target) | (df['country'] == origin)]
        plotting(db)
    except AssertionError as msg:
        print(msg)
    except KeyboardInterrupt:
        print("trl+c pressed...Exiting")


if __name__ == '__main__':
    aff_pop()
