import numpy as np


def calculate_distance(point1, point2):

    return np.sqrt(np.sum((point1 - point2) ** 2))


def assign_clusters(X, centroids):
    labels = []

    for point in X:

        distances = []

        for centroid in centroids:
            distances.append(calculate_distance(point, centroid))

        labels.append(np.argmin(distances))

    return np.array(labels)


def update_centroids(X, labels, k):
    centroids = []

    for i in range(k):

        cluster_points = X[labels == i]

        if len(cluster_points) == 0:
            centroids.append(np.zeros(X.shape[1]))
        else:
            centroids.append(np.mean(cluster_points, axis=0))

    return np.array(centroids)


def kmeans(X, k=3, max_iterations=100):
    X = np.array(X)

    np.random.seed(42)

    random_indices = np.random.choice(len(X), k, replace=False)

    centroids = X[random_indices]

    for i in range(max_iterations):

        labels = assign_clusters(X, centroids)

        new_centroids = update_centroids(X, labels, k)

        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return labels, centroids