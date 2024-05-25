import hgtk

def word_to_jamo(token):
    def to_special_token(jamo):
        if not jamo:
            return '-'
        else:
            return jamo

    decomposed_token = ''
    for char in token:
        try:
            # char(음절)을 초성, 중성, 종성으로 분리
            cho, jung, jong = hgtk.letter.decompose(char)

            # 자모가 빈 문자일 경우 특수문자 -로 대체
            cho = to_special_token(cho)
            jung = to_special_token(jung)
            jong = to_special_token(jong)
            decomposed_token = decomposed_token + cho + jung + jong

        # 만약 char(음절)이 한글이 아닐 경우 자모를 나누지 않고 추가
        except Exception as exception:
            if type(exception).__name__ == 'NotHangulException':
                decomposed_token += char

    # 단어 토큰의 자모 단위 분리 결과를 추가
    return decomposed_token

print(word_to_jamo('남동생'))