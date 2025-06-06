# kSpeechWordCFCallBack

**Framework**: Application Services  
**Kind**: data

Set the callback function to be called every time the Speech Synthesis Manager is about to generate a word on the speech channel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechWordCFCallBack: CFString
```

#### Discussion

 The value associated with this property is `CFNumber` object whose value is a pointer to an application-defined word callback function, whose syntax is described in [`SpeechWordCFProcPtr`](speechwordcfprocptr.md). Passing a `CFNumber` object that contains the value `NULL` for the value of this property disables the word callback function.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechwordcfcallback)*