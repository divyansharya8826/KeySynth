class keywords:
    
    def key(self, txt):
        from rake_nltk import Rake #type:ignore
        rake_nltk_var = Rake()
        rake_nltk_var.extract_keywords_from_text(txt)
        keyword_extracted = rake_nltk_var.get_ranked_phrases()
        return keyword_extracted