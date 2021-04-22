import csv
import random
import math
from constants import ALL_DIMENSIONS

def get_initial_means(sports_data, dimensions, num_clusters):
    """
       randomly chooses points from sports_data as initial means
    """
    sports_data_keys = list(sports_data)
    initial_means = []
    sample_sports = random.sample(list(range(len(sports_data_keys))), num_clusters)
    initial_means = [sports_data[sports_data_keys[sample]] for sample in sample_sports]
    return initial_means

def distance(point1, point2):
    assert len(point1) == len(point2)
    return math.sqrt(sum([((point1[i] - point2[i]) ** 2) for i in range(len(point1))]))

def get_closest_mean(point, means):
    distances = [distance(point, m) for m in means]
    return distances.index(min(distances))

def calculate_means(sports_dimensions_data, clusters, num_dimensions):
    means = []
    for cluster in clusters:
        cluster_mean = []
        cluster_length = len(cluster)
        for i in range(num_dimensions):
            dimensional_sum = 0
            for sport in cluster:
                dimensional_sum += sports_dimensions_data[sport][i]
            dimensional_mean = dimensional_sum / cluster_length
            cluster_mean.append(dimensional_mean)
        means.append(cluster_mean)
    return means

def lloyds_algorithm(means, sports_dimensions_data, num_dimensions, num_clusters, max_iterations=100):  
    clusters = [[] for i in range(num_clusters)]
    clusters_changed = False
    num_sports = len(sports_dimensions_data)

    sport_to_cluster = {}
    count = 0

    while True:
        new_clusters = [[] for i in range(num_clusters)]
        for sport in sports_dimensions_data:
            closest_mean = get_closest_mean(sports_dimensions_data[sport], means)
            if (sport not in sport_to_cluster or sport_to_cluster[sport] != closest_mean):
                clusters_changed = True
            new_clusters[closest_mean].append(sport)
            sport_to_cluster[sport] = closest_mean
        if count == max_iterations or not clusters_changed:
            return [new_clusters, means]

        clusters = new_clusters 
        means = calculate_means(sports_dimensions_data, new_clusters, len(dimensions))
        count += 1


def validate_dimensions(dimensions_input):
    dimensions_input = dimensions_input.split(',')
    dimensions_list = []
    try:
        for dim in dimensions_input:
            dim = int(dim)
            if dim < 0 or dim > 9:
                return (False, [], 'Only enter integers between 0 and 9!')
            dimensions_list.append(dim)
    except ValueError:
        return (False, [], 'Only enter integers!')

    if not dimensions_list:
        return (False, [], 'Enter at least one integer between 0 and 9!')
    return (True, dimensions_list, 'Success')


def prompt_dimensions():
    print("You can cluster sports based on these 10 dimensions:")
    print("----------------------------------------------------")
    for i in range(10):
        print(f'{ALL_DIMENSIONS[i][1]} - {ALL_DIMENSIONS[i][0]} - ({i})') 
    print("----------------------------------------------------\n")

    valid = False
    message = None
    dimensions = []
    while not valid:
        if message:
            print(message)
        dimensions_input = input("Enter a comma-separated list of the numbers for each dimension you want to cluster on (Example: 4, 7, 2, 3): ")
        valid, dimensions, message = validate_dimensions(dimensions_input)

    dimension_names = list(set([ALL_DIMENSIONS[i][0] for i in dimensions]))
    print('Chosen dimensions: ' + ', '.join(dimension_names))
    return dimensions

def validate_num_clusters(num_clusters_input):
    try:
        num_clusters = int(num_clusters_input)
        return True, num_clusters, None
    except ValueError:
        return False, None, 'Enter integer between 2 and 59!'

def prompt_num_clusters():
    valid = False
    message = None
    num_clusters = 2

    while not valid:
        if message:
            print(message)
        num_clusters_input = input("How many clusters do you want to build? Enter integer value between 2 and 59: ")
        valid, num_clusters, message = validate_num_clusters(num_clusters_input)
    return num_clusters

def get_sports_data_from_csv():
    f = open('sports_rankings.csv')
    csv_reader = csv.reader(f, delimiter='\t')
    next(csv_reader)    #skip first line (header)

    sports_data = {}
    for line in csv_reader:
        sports_data[line[0]] = [float(value) for value in line[1:]]

    return sports_data

def get_required_dimensions(sports_data, dimensions):
    sports_dimensions_data = {}
    for sport in sports_data:
        sports_dimensions_data[sport] = [sports_data[sport][dim] for dim in dimensions]
    return sports_dimensions_data


dimensions = prompt_dimensions()
num_clusters = prompt_num_clusters()
all_sports_data = get_sports_data_from_csv()
sports_dimensions_data = get_required_dimensions(all_sports_data, dimensions)
initial_means = get_initial_means(sports_dimensions_data, dimensions, num_clusters)
clusters, means = lloyds_algorithm(initial_means, sports_dimensions_data, len(dimensions), num_clusters, max_iterations=1000)

# displaying results
dimension_string = ""
dimension_names = [ALL_DIMENSIONS[dim][0] for dim in dimensions]
dimension_text = ', '.join(dimension_names)

for i in range(len(clusters)):
    print("Cluster # " + str(i))
    print(dimension_text)
    print([round(mean, 2) for mean in means[i]])
    for sport in clusters[i]:
        print("\t" +  sport)

