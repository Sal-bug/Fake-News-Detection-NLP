# Fake-News-Detection-NLP

First run the comp_cos_sim_mat.py.

Run the attack_classification.py:

python attack_classification.py --dataset_path data/yelp --target_model bert --target_model_path bert-pretrained-models/yelp --max_seq_length 256 --batch_size 32 --counter_fitting_embeddings_path [path to counter-fitted-vectors.txt] --counter_fitting_cos_sim_path [path to cos_sim_counter_fitting.npy] --USE_cache_path ./
