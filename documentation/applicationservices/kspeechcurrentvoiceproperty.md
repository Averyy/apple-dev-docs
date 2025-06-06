# kSpeechCurrentVoiceProperty

**Framework**: Application Services  
**Kind**: data

Set the current voice on the current speech channel to the specified voice.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechCurrentVoiceProperty: CFString
```

#### Discussion

The value associated with this property is a `CFDictionary` object that contains the phoneme symbols and example words defined for the current synthesizer. Your application might use this information to show the user what symbols to use when entering phonemic text directly. See [`Phoneme Symbols Keys`](speech_synthesis_manager/phoneme_symbols_keys.md) for the keys you can use to specify values in this dictionary.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechcurrentvoiceproperty)*