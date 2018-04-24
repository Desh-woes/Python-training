from math import sqrt
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

metadata = pd.read_csv('Test.csv', low_memory=False, header=0)

# vectorizer = TfidfVectorizer()
# metadata = vectorizer.fit_transform(vector)
# print(metadata)
def similarity_score(person1,person2):
    both_viewed = {}
    for metadata['item'] in metadata[person1]:
        if metadata['item'] in metadata[person2]:
            both_viewed[metadata['item']]= 1

        if len(both_viewed) == 0:
            return 0

        sum_of_euclidean_distance = []

        for metadata['item'] in metadata[person1]:
            if metadata['item'] in metadata[person2]:
                sum_of_euclidean_distance.append(pow(metadata[person1][metadata['item']]- metadata[person1][metadata['item']],2))
        sum_of_euclidean_distance = sum(sum_of_euclidean_distance)
        return 1/(1+sqrt(sum_of_euclidean_distance))
similarity_score(metadata['user'][0],metadata['user'][1])
#print (metadata)