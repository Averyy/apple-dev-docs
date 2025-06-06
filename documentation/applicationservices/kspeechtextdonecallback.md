# kSpeechTextDoneCallBack

**Framework**: Application Services  
**Kind**: data

Set the callback function to be called when the Speech Synthesis Manager has finished processing speech being generated on the speech channel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechTextDoneCallBack: CFString
```

#### Discussion

The value associated with this property is a `CFNumber` object whose value is a pointer to an application-defined text-done callback function, whose syntax is described in [`SpeechTextDoneProcPtr`](speechtextdoneprocptr.md). Passing a `CFNumber` object that contains the value `NULL` disables the text-done callback function.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechtextdonecallback)*