# kSpeechCharacterModeProperty

**Framework**: Application Services  
**Kind**: data

Get or set the speech channel’s current character-processing mode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechCharacterModeProperty: CFString
```

#### Discussion

The value associated with this property is a `CFString` object that specifies whether the speech channel is currently in normal or literal character-processing mode. The constants `kSpeechModeNormal` and `kSpeechModeLiteral` (defined in [`Speech-Channel Modes for Core Foundation-based Functions`](speech_synthesis_manager/speech-channel_modes_for_core_foundation-based_functions.md)) are the possible values of this string.

When the character-processing mode is `kSpeechModeNormal`, input characters are spoken as you would expect to hear them. When the mode is `kSpeechModeLiteral`, each character is spoken literally, so that the word “cat” is spoken “C–A–T”.

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) and [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechcharactermodeproperty)*