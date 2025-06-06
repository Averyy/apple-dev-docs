# kNoSpeechInterrupt

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var kNoSpeechInterrupt: Int32 { get }
```

#### Discussion

Does not interrupt current speech. The `kNoSpeechInterrupt` flagbit is used to control the behavior of `SpeakBuffer` whencalled on a speech channel that is still busy. When the flag bitis not set, `SpeakBuffer` behavessimilarly to `SpeakString` and `SpeakText`.Any speech currently being produced on the specified speech channelis immediately interrupted, and then the new text buffer is spoken.When the `kNoSpeechInterrupt` flagbit is set, however, a request to speak on a channel that is stillbusy processing a prior text buffer will result in an error. Thenew buffer is ignored and the error `synthNotReady` isreturned. If the prior text buffer has been fully processed, thenew buffer is spoken normally. One way of achieving continuous speech without using callback functions is to continually call `SpeakBuffer` with the `kNoSpeechInterrupt` flagbit set until the function returns `noErr`.The function will then execute as soon as the first text bufferhas been processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/knospeechinterrupt)*