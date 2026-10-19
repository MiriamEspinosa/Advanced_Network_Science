# Advanced Network Science

Source code for Advanced Network Science, Autumn 2026

---

#### Table of Contents

* [Week 1. Introduction](#week-1-introduction)
    * [Exercises](#11-exercises)
* [Week 2. Simplicial Complexes](#week-2-simplicial-complexes)
    * [Exercises](#21-exercises)
* [Week 3. Processes with Memory](#week-3-processes-with-memory)
    * [Exercises](#31-exercises)
* [Week 4. Graph Mining](#week-4-graph-mining)
* [Week 5. Node Roles](#week-5-node-roles)
* [Week 6. Shallow Graph Learning](#week-6-shallow-graph-learning)
* [Week 7. Random Walk Embeddings](#week-7-random-walk-embeddings)
* [Week 8. Node Attribute Embeddings](#week-8-node-attribute-embeddings)
* [Week 9. Message-Passing Graph Neural Networks](#week-9-message-passing-graph-neural-networks)
* [Week 10. Graph Convolutional Networks](#week-10-graph-convolutional-networks)
* [Week 11. Deep Learning on Graphs](#week-11-deep-learning-on-graphs)
* [Week 12. Summarization and Similarity](#week-12-summarization-and-similarity)
* [Week 13. Network Uncertainty](#week-13-network-uncertainty)
* [Week 14. Course Recap](#week-14-course-recap)
* [Personal Notes](#personal-notes)
* [References](#references)

## Week 1. Introduction
### 1.1 Exercises
This week the exercises cover the set up of the environment.

## Week 2. Simplicial Complexes
### 2.1 Exercises
Exercise 2:
- To solve this exercise, you can use any networkx function you need without restrctions.
- Assume that the network provided in this exercise package is a simplicial complex, where all cliques are simplices.
- Detect all of its facets.
- Is this simplicial complex pure?
- Calculate the k_{1,0}, k_{2,0}, and k_{2,1} distributions.
- Classify all edges into 2-saturated and 2-unsaturated.
- Detect the 1-connected components.


TODO: Tengo que terminar el ejercicio con lo de detected 1-connected components. Peguntar a Emil porque no lo entiendo.


## Week 3. Processes with Memory
### 3.1 Exercises
Exercise 3:
- Paper titles are high order random walks happening on a network.
- Reconstruct the single order network based on the random walks in the data.txt file.
   - The nodes in this network are the words.
   - Two words w1 and w2 are connected by a directed w1 -> w2 edge if w2 follows w1 in any title.
   - The edge's weight is the probability that the next word from w1 is w2.
- Reconstruct the high order network of order two based on the random walks. This means you should build the network based on trigrams.
   - Each node is now a pair of oriented words. So node "w1,w2" means that w2 follows w1.
   - Each edge connects pairs of pairs of nodes. For instance, trigram "w1 w2 w3" connects node "w1,w2" to "w2,w3".
   - The edge's weight is still proportional to the probability of transition, but now it is, using the previous example, the probability of ending in w3 via w2 given that we arrived in w2 from w1.
- Print out some examples of random walks on both structures.
   - For the single order network, start from node "^" and end in node "$".
   - For the 2-order network, start from a random node containing "^" and stop when the node contains "$".
   - Compare the random walks you obtain from the two structures and reflect on their differences.
   - NOTE: since you embedded the high order into the structure, the random walk function can be written to work on both network structures (although you don't have to do it).


## Week 4. Graph Mining

## Week 5. Node Roles

## Week 6. Shallow Graph Learning

## Week 7. Random Walk Embeddings

## Week 8. Node Attribute Embeddings

## Week 9. Message-Passing Graph Neural Networks

## Week 10. Graph Convolutional Networks

## Week 11. Deep Learning on Graphs

## Week 12. Summarization and Similarity

## Week 13. Network Uncertainty

## Week 14. Course Recap

## Personal Notes
I would like to do a visualization tool for the networks and graphs. 