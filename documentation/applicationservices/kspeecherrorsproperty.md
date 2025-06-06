# kSpeechErrorsProperty

**Framework**: Application Services  
**Kind**: data

Get speech-error information for the speech channel. 

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechErrorsProperty: CFString
```

#### Discussion

The value associated with this property is a `CFDictionary` object that contains speech-error information. See [`Speech Error Keys`](speech_synthesis_manager/speech_error_keys.md) for a description of the keys present in the dictionary.

This property lets you get information about various run-time errors that occur during speaking, such as the detection of badly formed embedded commands. Errors returned directly by the Speech Synthesis Manager are not reported here. If your application defines an error callback function, the function can use this property to get error information.

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeecherrorsproperty)*