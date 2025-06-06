# kSpeechSpeechDoneCallBack

**Framework**: Application Services  
**Kind**: data

Set the callback function to be called when the Speech Synthesis Manager has finished generating speech on the speech channel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechSpeechDoneCallBack: CFString
```

#### Discussion

The value associated with this property is `CFNumber` object whose value is a pointer to an application-defined speech-done callback function, whose syntax is described in [`SpeechDoneProcPtr`](speechdoneprocptr.md). Passing `NULL` for the value of this property disables the speech-done callback function.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechspeechdonecallback)*