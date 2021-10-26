#create a pie chart that intakes the data from the database and creates a pie chart 
#that shows the percentage of each category for device type and updates the pie chart everytime the page is refreshed
def data_pie(data):
    labels = []
    values = []
    for i in data:
        labels.append(i[0])
        values.append(i[1])
    return values, labels
    