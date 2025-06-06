# Speech Dictionary Keys

**Framework**: Application Services

Keys used in a speech dictionary to override the synthesizer’s default pronunciation of a word.

#### Overview

The keys in a speech dictionary can determine how a synthesizer pronounces a word. After you’ve created a speech dictionary, you register it with a speech channel with the [`UseSpeechDictionary(_:_:)`](1463688-usespeechdictionary.md) function.

## Topics

### Constants
- [let kSpeechDictionaryLocaleIdentifier: CFString](kspeechdictionarylocaleidentifier.md)
  The locale associated with the pronunciation.
- [let kSpeechDictionaryModificationDate: CFString](kspeechdictionarymodificationdate.md)
  The date the dictionary was last modified.
- [let kSpeechDictionaryPronunciations: CFString](kspeechdictionarypronunciations.md)
  The set of custom pronunciations.
- [let kSpeechDictionaryAbbreviations: CFString](kspeechdictionaryabbreviations.md)
  The set of custom pronunciations for abbreviations.
- [let kSpeechDictionaryEntrySpelling: CFString](kspeechdictionaryentryspelling.md)
  The spelling of an entry.
- [let kSpeechDictionaryEntryPhonemes: CFString](kspeechdictionaryentryphonemes.md)
  The phonemic representation of an entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speech_synthesis_manager/speech_dictionary_keys)*