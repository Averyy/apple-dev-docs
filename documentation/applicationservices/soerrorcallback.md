# soErrorCallBack

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var soErrorCallBack: OSType { get }
```

#### Discussion

Set the callback function to be called whenan error is encountered during the processing of an embedded command.The callback function might also be called if other conditions (suchas insufficient memory) arise during the speech conversion process.When a Speech Synthesis Manager function returns an error directly,the error callback function is not called. The callback functionis passed information about the most recent error; it can determineinformation about the oldest pending error by using the speech informationselector `soErrors`. The `speechInfo` parameteris a pointer to an application-defined error callback function.Passing `NULL` in `speechInfo` disablesthe error callback function, [`SpeechErrorProcPtr`](speecherrorprocptr.md).

This selector works with the [`SetSpeechInfo`](1552223-setspeechinfo.md) function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/soerrorcallback)*