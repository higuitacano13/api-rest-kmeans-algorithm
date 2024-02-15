from sklearn.cluster import KMeans

def k_means_algorithm(data):
    try:
        k = 3
        kmeans = KMeans(n_clusters=k, n_init=10)
        kmeans.fit(data)
        labels = kmeans.labels_
        data['Cluster'] = labels
        return data, kmeans
    except Exception as error:
        raise Exception(f'Se ha generado un error en el método k_means_algorithm -> {error}')