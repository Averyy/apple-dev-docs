# kSpeechSyncCallBack

**Framework**: Application Services  
**Kind**: data

Set the callback function to be called when the Speech Synthesis Manager encounters a synchronization command within an embedded speech command in text being processed on the speech channel. 

**Availability**:
- macOS 10.5+

## Declaration

```swift
let kSpeechSyncCallBack: CFString
```

#### Discussion

The value associated with this property is `CFNumber` object whose value is a pointer to an application-defined synchronization callback function, whose syntax is described in [`SpeechSyncProcPtr`](speechsyncprocptr.md). Passing a `CFNumber` object that contains the value `NULL` for the value of this property disables the synchronization callback function.

This property works with the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kspeechsynccallback)*