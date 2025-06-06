# kSpeechStatusProperty

**Framework**: Application Services  
**Kind**: data

Get speech-status information for the speech channel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechStatusProperty: CFString
```

#### Discussion

The value associated with this property is a `CFDictionary` object that contains speech-status information for the speech channel. See [`Speech Status Keys`](speech_synthesis_manager/speech_status_keys.md) for a description of the keys present in the dictionary.

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechstatusproperty)*