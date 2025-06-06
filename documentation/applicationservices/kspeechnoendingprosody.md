# kSpeechNoEndingProsody

**Framework**: Application Services  
**Kind**: data

Disable prosody at the end of sentences.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechNoEndingProsody: CFString
```

#### Discussion

The `kSpeechNoEndingProsody` key is used to indicate whether the speech synthesizer should automatically apply ending prosody, which is the speech tone and cadence that normally occur at the end of a sentence. When the key is not specified (or if it is specified with the value `kCFBooleanFalse`), ending prosody is applied to the speech at the end of `aString`. This behavior can be disabled by specifying the `kSpeechNoEndingProsody` key, with the value `kCFBooleanTrue`, in the `options` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechnoendingprosody)*