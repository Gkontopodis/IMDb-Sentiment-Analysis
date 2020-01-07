# IMDb-Sentiment-Analysis

Large Movie Review Dataset v1.0

## Overview

This dataset contains movie reviews along with their associated binary
sentiment polarity labels. It is intended to serve as a benchmark for
sentiment classification. This document outlines how the dataset was
gathered, and how to use the files provided. 

## Dataset 

The core dataset contains 25,000 reviews split into train, development
and test sets. The overall distribution of labels is roughly balanced.

## Files

Each folder contains files with negative (neg) and positive (reviews).
One review per line.

## Reference paper

@InProceedings{maas-EtAl:2011:ACL-HLT2011,
  author    = {Maas, Andrew L.  and  Daly, Raymond E.  and  Pham, Peter T.  and  Huang, Dan  and  Ng, Andrew Y.  and  Potts, Christopher},
  title     = {Learning Word Vectors for Sentiment Analysis},
  booktitle = {Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies},
  month     = {June},
  year      = {2011},
  address   = {Portland, Oregon, USA},
  publisher = {Association for Computational Linguistics},
  pages     = {142--150},
  url       = { http://www.aclweb.org/anthology/P11-1015 }


## Linux Terminal Instructions

IMDb.py script requires python 2.7+. After printing the results of its performance on the test set, the model will ask the user to provide a new movie review. It will detect if this new review is positive or negative by returning 1 or 0 respectively.

#### 1. The following libraries must be installed locally:

* pandas
* TfidfVectorizer from sklearn.feature_extraction.text
* LogisticRegression from sklearn.linear_model
* classification_report from sklearn.metrics

#### 2. Use cd command to move to the directory where the script is located.

#### 3. Before running the script from terminal, make sure that all the data frames are saved in the same directory as the file.

#### 4. Type the python version installed in your system followed by the name of the script, including the extension .py (i.e. python3 IMDb.py).

#### 5. Wait until the performance results are printed.

#### 6. Write a new movie review and hit Enter.

#### 7. The model will ouput 1 for a positive review or 0 for a negative one.
