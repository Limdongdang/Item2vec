import hgtk

# 한글인지 체크
print(hgtk.checker.is_hangul('ㄱ'))

print(hgtk.checker.is_hangul('28'))

# 음절을 초성, 중성, 종성으로 분해
print(hgtk.letter.decompose('남'))

# 초성, 중성을 결합
print(hgtk.letter.compose('ㄴ', 'ㅏ'))

# 한글이 아닌 입력에 대해서는 에러 발생.
print(hgtk.letter.decompose('1'))

# 결합할 수 없는 상황에서는 에러 발생
print(hgtk.letter.compose('ㄴ', 'ㅁ', 'ㅁ'))
