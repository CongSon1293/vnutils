# Vietnamese Sentence Spliter
This python package is used to split a Vietnamese document into a list of sentences.
## Usage
```
from vnspliter.sentence_spliter import SentenceSpliter
sentence_spliter = SentenceSpliter()
doc = u"A paragraph or a document here"
sens = sentence_spliter.split(doc)
```