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


## Instructions

IMDb.py script requires python 2.7+

#### 1. The following libraries must be installed in the local system:

* pandas
* TfidfVectorizer from sklearn.feature_extraction.text
* LogisticRegression from sklearn.linear_model
* classification_report from sklearn.metrics

#### 2. Use cd command to move to the directory where the script is located.

#### 3. Before running the script from terminal, make sure that all the data frames are saved in the same directory as the script file.

#### 4. Type the correct python version followed by the name of the script, including the extension .py (i.e. python3 IMDb.py).

#### 5. Wait until the results are printed.
