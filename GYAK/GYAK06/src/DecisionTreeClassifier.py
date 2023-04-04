import numpy as np

from src.Node import Node

class DecisionTreeClassifier():
    def __init__(self, min_sample_split = 2, max_depth = 2) -> None:
        #megallasi feltetel
        self.max_depth = max_depth
        self.min_sample_split = min_sample_split
        #gyoker
        self.root = None

    def build_tree(self, dataset, curr_depth = 0):
        x,y = dataset[:,:-1], dataset[:,-1]

        num_sample, num_features = np.shape(x)

        if num_sample >= self.min_sample_split and curr_depth <= self.max_depth:
            best_split = self.get_best_split(dataset, num_sample, num_features)

            if best_split['info_gain'] > 0:
                left_subtree = self.build_tree(best_split['dataset_left'], curr_depth + 1)
                right_subtree = self.build_tree(best_split['dataset_right'], curr_depth + 1)

                return Node(best_split['feature_index'], best_split['threshold'], left_subtree, right_subtree, best_split['info_gain'])

    def get_best_split(self, dataset, num_sample, num_feature):
        best_split = {}
        max_info_gain = -float('inf')

        for feature_index in range(num_feature):
            feature_value = dataset[:, feature_index]
            possible_thresholds = np.unique(feature_value)

            for threshold in possible_thresholds:
                dataset_left, dataset_right = self.split(dataset, feature_index, threshold)
                if len(dataset_left) > 0 and len(dataset_right) > 0:
                    y, left_y, right_y = dataset[:,-1], dataset_left[:,-1], dataset_right[:,-1]

                    curr_info_gain = self.information_gain(y, left_y, right_y, 'gini')

                    if curr_info_gain > max_info_gain:
                        best_split['feature_index'] = feature_index
                        best_split['threshold'] = threshold
                        best_split['dataset_left'] = dataset_left
                        best_split['dataset_right'] = dataset_right
                        best_split['curr_info_gain'] = curr_info_gain

                        max_info_gain = curr_info_gain
        return best_split
    
    def split(self, dataset, feature_index, threshold):
        dataset_left = np.array([row for row in dataset if row['feature_index'] <= threshold])
        dataset_right = np.array([row for row in dataset if row['feature_index'] > threshold])

        return dataset_left, dataset_right
    
    def information_gain(self, parent, l_child, r_child, mode = 'entropy'):
        weight_l = len(l_child) / len(parent)
        weight_r = len(r_child) / len(parent)

        gain = self.gini_index(parent) - (weight_l*self.gini_index(l_child) + weight_r*self.gini_index(r_child))

        return gain
    
    def gini_index(self, y):
        class_labels = np.unique(y)
        gini = 0
        for cls in class_labels:
            p_cls = len(y[y == cls]) / len(y)
            gini += p_cls**2
        return 1 - gini
    
    def calculate_leaf_node(self, y):
        Y = list(y)
        return max(Y, key=(Y.count))
    
    def print_tree(self, tree = None, indent = " "):
        if not tree:
            tree = self.root
        if tree.value is not None:
            print(tree.value)
        else:
            print("X_" + str(tree.feature_index), " <= ", tree.threshold, "?", tree.info_gain)
            print("%sleft: " %(indent), end = "")
            self.print_tree(tree.left, indent + indent)

            print("%right: " %(indent), end = "")
            self.print_tree(tree.left, indent + indent)
    
    def fit(self,X,Y):
        dataset = np.concatenate((X,Y), axis=1)
        self.root = self.build_tree(dataset)

    def predict(self,X):
        prediction = [self.make_prediction(X, self.root) for x in X]
        return prediction
    
    def make_prediction(self, x, tree):
        if tree.value != None:
            return tree.value
        feature_val = x[tree.feature_index]
        if feature_val < tree.threshold:
            return self.make_prediction(x, tree.left)
        else:
            return self.make_prediction(x, tree.right)