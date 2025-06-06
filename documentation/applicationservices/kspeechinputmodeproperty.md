# kSpeechInputModeProperty

**Framework**: Application Services  
**Kind**: data

Get or set the speech channel’s current text-processing mode. 

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechInputModeProperty: CFString
```

#### Discussion

The value associated with this property is a `CFString` object that specifies whether the channel is currently in text input mode or phoneme input mode. The constants `kSpeechModeText` and `kSpeechModePhoneme` (defined in [`Speech-Channel Modes for Core Foundation-based Functions`](speech_synthesis_manager/speech-channel_modes_for_core_foundation-based_functions.md)) are the possible values of this string.

When in phoneme-processing mode, a text string is interpreted to be a series of characters representing various phonemes and prosodic controls. Some synthesizers might support additional input-processing modes and define constants for these modes.

When in text-processing mode, you can also specify how characters and numbers should be processed using the [`kSpeechCharacterModeProperty`](kspeechcharactermodeproperty.md) and [`kSpeechNumberModeProperty`](kspeechnumbermodeproperty.md).

This property works with the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) and [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechinputmodeproperty)*