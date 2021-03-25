# Fake-News-Detection-NLP

The folder TextFooler-master is copied directly from https://github.com/jind11/TextFooler. We try to reproduce the results with small modification.

## Run the comp_cos_sim_mat.py.

This will generate a file of .npy of around 17GB.

## Run the attack_classification.py:

Sample terminal instructions on dataset yelp using bert model. It will download a pretrained bert model on yelp and USE model automatically:

```
python attack_classification.py --dataset_path data/yelp --target_model bert 
--target_model_path bert-pretrained-models/yelp --max_seq_length 256 --batch_size 32 
--counter_fitting_embeddings_path [path to counter-fitted-vectors.txt] 
--counter_fitting_cos_sim_path [path to cos_sim_counter_fitting.npy] --USE_cache_path ./
```
