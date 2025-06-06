# Text Analysis Keys

**Framework**: Core Services

Each of these constants is an optional key in a Search Kit index’s text analysis properties dictionary. The constant descriptions describe the corresponding values for each of these keys. These keys are declared in the `Analysis.h` header file.

## Topics

### Constants
- [let kSKMinTermLength: CFString!](kskmintermlength.md)
  The minimum term length to index. Specified as a CFNumber object. If this optional key is not present, Search Kit indexing defaults to a minimum term length of 1.
- [let kSKStopWords: CFString!](kskstopwords.md)
  A set of stopwords—words not to index. Specified as a CFSet object. There is no default stopword list. You must supply your own.
- [let kSKSubstitutions: CFString!](ksksubstitutions.md)
  A dictionary of term substitutions—terms that differ in their character strings but that match during a search. Specified as a CFDictionary object.
- [let kSKMaximumTerms: CFString!](kskmaximumterms.md)
- [let kSKProximityIndexing: CFString!](kskproximityindexing.md)
- [let kSKTermChars: CFString!](ksktermchars.md)
- [let kSKStartTermChars: CFString!](kskstarttermchars.md)
- [let kSKEndTermChars: CFString!](kskendtermchars.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/search_kit/text_analysis_keys)*