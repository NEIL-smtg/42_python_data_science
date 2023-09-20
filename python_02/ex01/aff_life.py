from load_csv import load
from matplotlib import pyplot as plt


def aff_life():
    try:
        file = 'life_expectancy_years.csv'
        err_msg = "DataFrame not loaded"
        df = load(file)
        assert df is not None, err_msg

        db = df[df['country'] == 'France']

        # Extract the years and life expectancy values as lists
        years = db.columns[1:].tolist()
        life_expectancy = db.values[0, 1:].tolist()

        # Plotting the data
        plt.figure(figsize=(10, 6))  # Adjust figure size as needed

        # Specify the x-axis tick locations and labels with a larger step
        x_ticks = years[::10]  # Adjust the step size as needed

        x_labels = [str(x) for x in x_ticks]
        plt.plot(years, life_expectancy, linestyle='-', color='b')
        plt.title('Life Expectancy in France')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')

        # Set the x-axis tick locations and labels
        # Rotate labels for better visibility
        plt.xticks(x_ticks, x_labels, rotation=45)
        plt.show()
    except KeyboardInterrupt:
        print("trl+c pressed...Exiting")
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    aff_life()
