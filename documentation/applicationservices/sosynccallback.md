# soSyncCallBack

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soSyncCallBack: OSType { get }
```

#### Discussion

Set the callback function to be called whenthe Speech Synthesis Manager encounters a synchronization commandwithin an embedded speech command in text being processed on thespeech channel. The `speechInfo` parameteris a pointer to an application-defined synchronization callback function,whose syntax is described in [`SpeechSyncProcPtr`](speechsyncprocptr.md).Passing `NULL` in `speechInfo` disablesthe synchronization callback function.

This selector works with the `SetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sosynccallback)*