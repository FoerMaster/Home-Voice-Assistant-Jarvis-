import torch
from transformers import FSMTModel, FSMTTokenizer, FSMTForConditionalGeneration
tokenizer = FSMTTokenizer.from_pretrained("facebook/wmt19-en-ru")
model = FSMTForConditionalGeneration.from_pretrained("facebook/wmt19-en-ru")
inverse_tokenizer = FSMTTokenizer.from_pretrained("facebook/wmt19-ru-en")
inverse_model = FSMTForConditionalGeneration.from_pretrained("facebook/wmt19-ru-en")
model.cuda();
inverse_model.cuda();

def paraphrase(text, gram=4, num_beams=5, **kwargs):
    """ Generate a paraphrase using back translation.
    Parameter `gram` denotes size of token n-grams of the original sentence that cannot appear in the paraphrase.
    """
    input_ids = inverse_tokenizer.encode(text, return_tensors="pt")
    with torch.no_grad():
        outputs = inverse_model.generate(input_ids.to(inverse_model.device), num_beams=num_beams, **kwargs)
    other_lang = inverse_tokenizer.decode(outputs[0], skip_special_tokens=True)
    # print(other_lang)
    input_ids = input_ids[0, :-1].tolist()
    bad_word_ids = [input_ids[i:(i+gram)] for i in range(len(input_ids)-gram)]
    input_ids = tokenizer.encode(other_lang, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(input_ids.to(model.device), num_beams=num_beams, bad_words_ids=bad_word_ids, **kwargs)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded