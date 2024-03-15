from .vqa_dataset import VQADataset, VQAPrompter
from transformers import AutoTokenizer
from collections import defaultdict
import random
import json
from PIL import Image
import os

class VlspDataset(VQADataset):
    def __init__(
        self,
        tokenizer,
        ann_paths,
        vis_processor=None,
        vis_root=None,
        add_eos=True,
        ignore_instruction=True,
        sample_image=False,
    ):
        self.tokenizer: AutoTokenizer = tokenizer
        self.vis_root = vis_root
        self.info = json.load(open(ann_paths, "r", encoding= 'utf8'))
        self.annotations= self.info['annotations']
        self.images= self.info['images']
        self.annotation=[self.annotations[key] for key in self.annotations.keys()]
        self.prompter= VQAPrompter()

        self.sample_image = sample_image
        if self.sample_image:
            print("randomly sample one annotation for each image")
            self.annotation = self.parse_annotation(self.annotation)

        self.vis_processor = vis_processor
    def parse_annotation(self, annotation):
        image_list = defaultdict(list)
        for ann in annotation:
            image = self.images[str(ann['image_id'])]
            image_list[image].append(ann)
        # image_name_list = list(image_list.keys())
        annotation = []
        for ann_list in image_list.values():
            annotation.append(random.choice(ann_list))
        return annotation
    
    def process_image(self, ann):
        image_path = os.path.join(self.vis_root, self.images[str(ann['image_id'])])
        image = Image.open(image_path).convert("RGB")

        image = self.vis_processor(image)
        return image

    def process_text(self, ann):
        question = ann["question"]

        true_answer = ann['answer']
        instruction = self.prompter(question)

        return dict(instruction=instruction, answer=true_answer)

