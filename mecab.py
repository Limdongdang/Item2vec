import MeCab

tagger = MeCab.Tagger()

def extract_morphs(text):
    parsed = tagger.parse(text)
    lines = parsed.split('\n')
    morphs = [line.split('\t')[0] for line in lines[:-2]]  # 마지막 두 줄은 'EOS'와 빈 줄이므로 제외
    return morphs

print(extract_morphs('강아지가 너무 귀여워요.'))