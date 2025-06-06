# kSpeechSynthesizerInfoProperty

**Framework**: Application Services  
**Kind**: data

Get information about the speech synthesizer being used on the specified speech channel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechSynthesizerInfoProperty: CFString
```

#### Discussion

The value associated with this property is a `CFDictionary` object that contains information about the speech synthesizer being used on the specified speech channel. See [`Speech Synthesizer Information Keys`](speech_synthesis_manager/speech_synthesizer_information_keys.md) for a description of the keys present in the dictionary.

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechsynthesizerinfoproperty)*