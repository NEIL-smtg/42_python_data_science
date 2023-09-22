from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def filtering_data(data: pd.DataFrame) -> pd.DataFrame:
    return (data.loc[:, '1900'])


def get_xlabel(val, _):
    labels = {
        300: '300',
        1000: '1k',
        10000: '10k'
    }
    return labels.get(val)


def plotting(gdp, expectancy):

    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.scatter(gdp, expectancy)
    plt.xscale('log')
    plt.xticks([300, 1000, 10000])
    ax = plt.gca()
    ax.xaxis.set_major_formatter(plt.FuncFormatter(get_xlabel))
    plt.show()


def projection_life():
    try:
        err_msg = 'AssertionError: File not loaded'
        expectancy_file = 'life_expectancy_years.csv'
        gdp_file = 'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        expectancy = load(expectancy_file)
        gdp = load(gdp_file)
        assert expectancy is not None and gdp is not None, err_msg
        plotting(filtering_data(gdp), filtering_data(expectancy))
    except AssertionError as msg:
        print(msg)


if __name__ == '__main__':
    projection_life()
