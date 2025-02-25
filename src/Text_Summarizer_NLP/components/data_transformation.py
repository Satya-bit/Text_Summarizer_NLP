import os
from src.Text_Summarizer_NLP.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
from src.Text_Summarizer_NLP.entity import DataTransformationConfig
class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer=AutoTokenizer.from_pretrained(config.tokenizer_name) #Initializing tokenizer from config file
    
    
    def convert_examples_to_features(self,example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

        with self.tokenizer.as_target_tokenizer():#By using with tokenizer.as_target_tokenizer(), we signal that
        # we are working with the target sequence, which may have special handling for tokenization, like adding special tokens (e.g., [BOS], [EOS] for beginning and end of the sequence) or truncating the sequence in a particular way.
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'], #This depicts whether the token is padded or not. 1 means it is not padded
            'labels': target_encodings['input_ids']
        }
        
    def convert(self): #Applying tokenizer to whole dataset
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features,batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir,"samsum_dataset"))
        
