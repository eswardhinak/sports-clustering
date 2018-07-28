import csv
import random
import math
from operator import add

def random_initial_means(sports, data, dimensions, number_of_clusters):
	means = []
	number_of_sports = len(data)
	initial_indices = random.sample(range(0, number_of_sports), number_of_clusters)
	means = [data[sports[i]] for i in initial_indices]
	return means

def distance(point1, point2):
	assert len(point1) == len(point2)
	return math.sqrt(sum([((point1[i] - point2[i]) ** 2) for i in range(len(point1))]))

def find_closest_mean(point, means):
	distances = [distance(point, m) for m in means]
	return distances.index(min(distances))

def calculate_means(data, clusters, sports, num_dimensions):
	means = []
	for c in clusters:
		cluster_mean = []
		for i in range(num_dimensions):
			directional_sum = 0
			for j in c:
				directional_sum += data[sports[j]][i]
			directional_avg = directional_sum / len(c)
			cluster_mean.append(directional_avg)
		means.append(cluster_mean)
	return means

def lloyds_algorithm(means, data, sports, dimensions, max_iterations=100):
	clusters = [[] for i in range(len(means))]
	change_of_clusters = False
	point_cluster_map = {}
	count = 0
	while (True):
		new_clusters = [[] for i in range(len(means))]
		for i in range(len(sports)):
			closest_mean = find_closest_mean(data[sports[i]], means)
			if (i not in point_cluster_map or point_cluster_map[i] != closest_mean):
				change_of_clusters = True
			new_clusters[closest_mean].append(i)
			point_cluster_map[i] = closest_mean

		if count == max_iterations or not change_of_clusters:
			return [new_clusters, means]

		new_means = calculate_means(data, new_clusters, sports, len(dimensions))
		difference = [[a_i - b_i for a_i,b_i in zip(new_means[i], means[i])] for i in range(len(means))]

		magnitudes = []
		for center in difference:
			sum_dimensions = 0
			for dimension in center:
				sum_dimensions = dimension ** 2
			magnitudes.append(math.sqrt(sum_dimensions))
		print (magnitudes)
		clusters = new_clusters 
		count += 1




f = open('sports_rankings.csv')
csv_reader = csv.reader(f, delimiter='\t')

data = {}
first_line = True
sports = []
attributes = []
dimensions = [9,10]

for line in csv_reader:
	if first_line:
		attributes = line[1:]
		first_line = False
		continue
	sport_name = line[0]
	sports.append(sport_name)
	data[sport_name] = map(lambda x: float(x), [line[d] for d in dimensions])

initial_means = random_initial_means(sports, data, dimensions, 6)
clusters, means = lloyds_algorithm(initial_means, data, sports, dimensions, max_iterations=1000)
print (clusters)
print(means)

dimension_string = ""
for dim in dimensions:
	dimension_string += attributes[dim-1] + " "

for i in range(len(clusters)):
	print "Cluster # " + str(i)
	print(dimension_string)
	print means[i]
	for sport in clusters[i]:
		print "\t" +  sports[sport]

