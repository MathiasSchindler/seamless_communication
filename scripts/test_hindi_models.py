import sentencepiece as spm
import torch

model_file = "/large_experiments/seamless/workstream/ggml/wa/checkpoints/502193129/machine_translation__hi_IN_en_XX_model_ptl_717309797021985"

extra_files = {
    "source_vocab_dict": None,
    "target_vocab_dict": None,
    "source_vocab_model": None,
    "target_vocab_model": None,
    "source_vocab_json": None,
    "target_vocab_json": None,
}

generator = torch.jit.load(model_file, _extra_files=extra_files)
print(generator)
source_spm = spm.SentencePieceProcessor()
source_spm.LoadFromSerializedProto(extra_files["source_vocab_model"])
target_spm = spm.SentencePieceProcessor()
target_spm.LoadFromSerializedProto(extra_files["target_vocab_model"])

def generate_translations(input_texts):
    for input_str in input_texts:
        input_tokens = source_spm.encode(input_str)
        input_tokens.append(source_spm.eos_id())
        output_tokens = generator(torch.LongTensor(input_tokens)).tolist()
        output_str = target_spm.decode(output_tokens)
        print(f"{input_str}\n{output_str}\n\n")

def eval_model():
    texts = [
        "नमस्ते यह हिंदी में एक परीक्षण वाक्य है 😀👍",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
        "इस वीडियो को हमारी बहिन ,बेटी और बहुओं को जरूर सुनवाये। मुझे बहुत अच्छा लगा। प्लीज शेयर गुर्प विडियो।",
    ]
    generate_translations(texts)


if __name__ == "__main__":
    eval_model()
