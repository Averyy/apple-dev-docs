# kSpeechStatusOutputBusy

**Framework**: Application Services  
**Kind**: data

Indicates whether the speech channel is currently producing speech.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechStatusOutputBusy: CFString
```

#### Discussion

A speech channel is considered to be producing speech even at some times when no audio data is being produced through the computer’s speaker. This occurs, for example, when the Speech Synthesis Manager is processing input, but has not yet initiated speech or when speech output is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechstatusoutputbusy)*