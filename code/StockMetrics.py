
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        """pt1
        """
        averages = []
        for row in self.data:
            new_row = [float(x) for x in row[1:] if len(x.strip(" ")) > 0]
            averages.append(round(sum(new_row) / len(new_row), 3))
        return averages

    def median02(self):
        """pt2
        """
        medians = []
        for row in self.data:
            new_row = [float(x) for x in row[1:] if len(x.strip(" ")) > 0]
            medians.append(stats.median(new_row))
        return medians

    def stddev03(self):
        """pt3
        """
        deviations = []
        for row in self.data:
            new_row = [float(x) for x in row[1:] if len(x.strip(" ")) > 0]
            deviations.append(round(stats.stdev(new_row), 3))
        return deviations
