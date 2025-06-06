# kSpeechPhonemeOptionsProperty

**Framework**: Application Services  
**Kind**: data

Get or set the options for the generation of phonetic output.

**Availability**:
- macOS 10.6+

## Declaration

```swift
let kSpeechPhonemeOptionsProperty: CFString
```

#### Discussion

The value associated with this property is a pointer to an `CFNumber` object containing the flags (options) you would pass to [`soPhonemeOptions`](sophonemeoptions.md). (See [`Phoneme Generation Options`](speech_synthesis_manager/1552233-phoneme_generation_options.md) for a complete list of options.)

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) and the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechphonemeoptionsproperty)*