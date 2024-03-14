# VisualQuestionAnswering
## Hướng tiếp cận
Đào tạo một mô hình đa phương thức với các hướng dẫn bằng hình ảnh và ngôn ngữ!
Mô hình được đào tạo dựa trên kiến trúc của mô hình đa phương thức nguồn mở [OpenFlamingo](https://github.com/mlfoundations/open_flamingo) và chỉ tinh chỉnh ở mô đun ngôn ngữ lớn và sử dụng dữ liệu instruction, mô hình được tinh chỉnh và huấn luyện trên bộ dataset tiếng Việt được cung cấp bởi [VLSP_Challenge - Track 6](https://vlsp.org.vn/vlsp2023/eval/vrc?fbclid=IwAR0390aeSL3InaTsq7aq_-8TWH-9C01HXsUUt4YF1IXDhfqmK55asXTXFxg).

## Models
* LLM model   : [vietcuna-3b-v2](https://huggingface.co/vilm/vietcuna-3b-v2)
* Visual model: [CLIP](https://github.com/openai/CLIP/tree/main)
* Pretrain OpenFlamingo: [openflamingo/OpenFlamingo-9B](https://huggingface.co/openflamingo/OpenFlamingo-9B-deprecated)

## Demo
![alt text](https://github.com/mdnanh/VisualQuestionAnswering/blob/main/images/1%20(1).png)
![alt text](https://github.com/mdnanh/VisualQuestionAnswering/blob/main/images/1%20(3).png)
![alt text](https://github.com/mdnanh/VisualQuestionAnswering/blob/main/images/1%20(2).png)

## Huấn luyện mô hình
* Mô hình được huấn luyện trên [google colab](https://colab.research.google.com/) với GPU A100

```python
!python Fim1/finetune.py --vision_encoder_path "ViT-L-14" \
                   --vision_encoder_pretrained "openai" \
                   --lm_path 'vilm/vietcuna-3b-v2' \
                   --tokenizer_path 'vilm/vietcuna-3b-v2' \
                   --run_name {YOUR_RUN_NAME} \
                   --num_epochs 1 \
                   --batch_size 1 \
                   --delete_previous_checkpoint \
                   --dataset_config {YOUR_DATACONFIG_PATH} \
                   --tuning_config {YOUR_LORACONFIG_PATH} \
                   --report_to_wandb \
                   --wandb_project wandb_project\
                   --pretrained_path {YOUR_PRETRAINOPENFLAMINGO_PATH}
```
