class StringUtil:
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        # we allow only letters and numbers
        s = ''.join(c for c in s if c.isalnum()) # Study this!
        # For case insensitive comparison, we lower-case s
        if case_insensitive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c -1]:
                return False
        return True
    
    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())

s1 = StringUtil()
print(s1.is_palindrome("Radar",case_insensitive=False))
print(StringUtil.is_palindrome("Radar",case_insensitive=True))
print(StringUtil.get_unique_words(
    'I love palindromes. I really really love them!'))