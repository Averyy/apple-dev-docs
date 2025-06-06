# soPhonemeOptions

**Framework**: Application Services  
**Kind**: data

Get or set options for the generation of phonetic output. See [`Phoneme Generation Options`](speech_synthesis_manager/1552233-phoneme_generation_options.md) for a complete list of options.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var soPhonemeOptions: OSType { get }
```

#### Discussion

The `speechInfo` parameter is a pointer to a long value that represents the phoneme generation value.

This selector works with both the `GetSpeechInfo` and `SetSpeechInfo` functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sophonemeoptions)*