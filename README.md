# Fake-News-Detection-NLP

## Reproduction Process

The folder TextFooler-master is copied directly from https://github.com/jind11/TextFooler. We try to reproduce the results with small modifications.

* Run the comp_cos_sim_mat.py.

```
python comp_cos_sim_mat.py [path to counter-fitted-vectors.txt]
```
This will generate a file of .npy of around 17GB.

* Run the attack_classification.py:

Sample terminal instructions on dataset YELP using BERT model are provided following. It will download a pretrained BERT model on YELP and USE model automatically:

```
python attack_classification.py --dataset_path data/yelp --target_model bert 
--target_model_path bert-pretrained-models/yelp --max_seq_length 256 --batch_size 32 
--counter_fitting_embeddings_path [path to counter-fitted-vectors.txt] 
--counter_fitting_cos_sim_path [path to cos_sim_counter_fitting.npy] --USE_cache_path ./
```

The above code will generate a file named vulnerable_words.txt to output the vulnerable(important) words after being sorted by the importance scores.
