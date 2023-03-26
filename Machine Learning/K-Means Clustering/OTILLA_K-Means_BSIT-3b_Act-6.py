from random import randint
import statistics

def process(randInt, centroids, clusters):
    count = 0
    iteCount = 0
    iteration = 0

    while True:

        for i in clusters:
            i.clear()

        iteCount = 0

        for int in range(len(randInt)):

            index = 0
            cluster = 0

            for cen in range(len(centroids)):
                if cen == 0:
                    cluster = abs(randInt[int] - centroids[cen])
                    index = cen

                temp = abs(randInt[int] - centroids[cen])

                if cluster < temp:
                    continue
                else:
                    cluster = temp
                    index = cen

            clusters[index].append(cluster)

        cen = 0
        if count == 0:
            for cluster in clusters:
                centroids[cen] = statistics.mean(cluster)
                cen += 1
            count += 1
        else:
            temp = 0
            for i in range(len(clusters)):
                if len(clusters[i]) == 0:
                    temp = centroids[i]
                else:
                    temp = statistics.mean(clusters[i])
                if temp == centroids[i]:
                    iteCount += 1
                else:
                    iteCount = 0
                    centroids[i] = temp
        
        iteration += 1
        
        if iteration != 40:
            
            prev = 0
            if iteCount == 5:
                if prev == 0:
                    prev = iteCount
                else:
                    iteCount = prev + iteCount
                
                if iteCount == 10:
                    break
            else:
                prev = 0
        else:
            break
    
    return randInt, centroids, clusters

if __name__ == '__main__':

    randInt = [randint(1, 100000) for _ in range(300)]
    centroids = [randint(1, 100000) for _ in range(5)]
    clusters = [[], [], [], [], []]

    randInt, centroids, clusters = process(randInt, centroids, clusters)
    
    print("======================================================================================================================")
    
    for i in range(len(clusters)):
        print("Centroid ", i + 1, " :", centroids[i])
        print("Cluster ", i + 1, " Lenght: ", len(clusters[i]))
        
    print("======================================================================================================================")