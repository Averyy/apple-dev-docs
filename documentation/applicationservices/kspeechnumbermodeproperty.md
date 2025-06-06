# kSpeechNumberModeProperty

**Framework**: Application Services  
**Kind**: data

Get or set the speech channel’s current number-processing mode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechNumberModeProperty: CFString
```

#### Discussion

The value associated with this property is a `CFString` object that specifies whether the speech channel is currently in normal or literal number-processing mode. The constants `kSpeechModeNormal` and `kSpeechModeLiteral` (defined in [`Speech-Channel Modes for Core Foundation-based Functions`](speech_synthesis_manager/speech-channel_modes_for_core_foundation-based_functions.md)) are the possible values of this string.

When the number-processing mode is `kSpeechModeNormal`, the synthesizer assembles digits into numbers (so that “12” is spoken as “twelve”). When the mode is `kSpeechModeLiteral`, each digit is spoken literally (so that “12” is spoken as “one, two”).

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) and [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechnumbermodeproperty)*