import torch
from torch_geometric.data import Data

edge_index = torch.tensor([[0, 1, 1, 2],
                           [1, 0, 2, 1]], dtype=torch.long)
x = torch.tensor([[-1], [0], [1]], dtype=torch.float)

data = Data(x=x, edge_index=edge_index)
data.validate(raise_on_error=True)

print(data.keys())
# >>> ['x', 'edge_index']

print(data['x'])
# >>> tensor([[-1.0],
#            [0.0],
#            [1.0]])

for key, item in data:
    print(f'{key} found in data')
# >>> x found in data
#>>> edge_index found in data

print('edge_attr' in data)
# >>> False

print(data.num_nodes)
# >>> 3

print(data.num_edges)
# >>> 4

print(data.num_node_features)
# >>> 1

print(data.has_isolated_nodes())
# >>> False

print(data.has_self_loops())
# >>> False

print(data.is_directed())
# >>> False

### COMMON BENCHMARK DATASETS
from torch_geometric.datasets import TUDataset

dataset = TUDataset(root='/tmp/ENZYMES', name='ENZYMES')
#>>> ENZYMES(600)

len(dataset)
#>>> 600

dataset.num_classes
#>>> 6

dataset.num_node_features
#>>> 3

data = dataset[0]
#>>> Data(edge_index=[2, 168], x=[37, 3], y=[1])

data.is_undirected()
#>>> True

train_dataset = dataset[:540]
# >>> ENZYMES(540)

test_dataset = dataset[540:]
# >>> ENZYMES(60)

perm = torch.randperm(len(dataset))
dataset = dataset[perm]
# >> ENZYMES(600)

from torch_geometric.datasets import Planetoid

dataset = Planetoid(root='/tmp/Cora', name='Cora')
# >>> Cora()

len(dataset)
# >>> 1

dataset.num_classes
#>>> 7

dataset.num_node_features
# >>> 1433
