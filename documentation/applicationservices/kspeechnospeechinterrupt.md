# kSpeechNoSpeechInterrupt

**Framework**: Application Services  
**Kind**: data

Do not interrupt current speech.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechNoSpeechInterrupt: CFString
```

#### Discussion

The `kSpeechNoSpeechInterrupt` key is used to control the behavior of [`SpeakCFString(_:_:_:)`](1461621-speakcfstring.md) when it is called on a speech channel that is busy. When `kSpeechNoSpeechInterrupt` is not specified in the `options` dictionary (or if it is specified with the value `kCFBooleanFalse`), `SpeakCFString` immediately interrupts the speech currently being produced on the specified speech channel and the new `aString` text is spoken. When `kSpeechNoSpeechInterrupt` is specified with the value `kCFBooleanTrue`, the request to speak on a speech channel that is already busy causes the new `aString` text to be ignored and the `synthNotReady` error to be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechnospeechinterrupt)*