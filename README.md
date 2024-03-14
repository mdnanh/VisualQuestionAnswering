# VisualQuestionAnswering
## Hướng tiếp cận
Đào tạo một mô hình đa phương thức với các hướng dẫn bằng hình ảnh và ngôn ngữ!
Mô hình được đào tạo dựa trên kiến trúc của mô hình đa phương thức nguồn mở [OpenFlamingo](https://github.com/mlfoundations/open_flamingo) và chỉ tinh chỉnh ở mô đun ngôn ngữ lớn và sử dụng dữ liệu instruction, mô hình được tinh chỉnh và huấn luyện trên bộ dataset tiếng Việt được cung cấp bởi [VLSP_Challenge - Track 6](https://vlsp.org.vn/vlsp2023/eval/vrc?fbclid=IwAR0390aeSL3InaTsq7aq_-8TWH-9C01HXsUUt4YF1IXDhfqmK55asXTXFxg).

## Models
* LLM model   : [vietcuna-3b-v2](https://huggingface.co/vilm/vietcuna-3b-v2)
* Visual model: [CLIP](https://github.com/openai/CLIP/tree/main)
* Pretrain OpenFlamingo: [openflamingo/OpenFlamingo-9B](https://huggingface.co/openflamingo/OpenFlamingo-9B-deprecated)

