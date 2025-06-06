# soTextDoneCallBack

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soTextDoneCallBack: OSType { get }
```

#### Discussion

Set the callback function to be called whenthe Speech Synthesis Manager has finished processing speech beinggenerated on the speech channel. The `speechInfo` parameteris a pointer to an application-defined text-done callback function,whose syntax is described in [`SpeechTextDoneProcPtr`](speechtextdoneprocptr.md). Passing `NULL` in `speechInfo` disablesthe text-done callback function.

This selector works with the `SetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/sotextdonecallback)*