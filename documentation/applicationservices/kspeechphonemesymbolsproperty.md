# kSpeechPhonemeSymbolsProperty

**Framework**: Application Services  
**Kind**: data

Get a list of phoneme symbols and example words defined for the speech channel’s synthesizer.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechPhonemeSymbolsProperty: CFString
```

#### Discussion

The value associated with this property is a `CFDictionary` object that contains the phoneme symbols and example words defined for the current synthesizer. Your application might use this information to show the user what symbols to use when entering phonemic text directly. See [`Phoneme Symbols Keys`](speech_synthesis_manager/phoneme_symbols_keys.md) for a description of the keys present in the dictionary.

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechphonemesymbolsproperty)*