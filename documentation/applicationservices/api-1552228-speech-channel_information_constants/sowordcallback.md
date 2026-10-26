# soWordCallBack

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
soWordCallBack = 'wdcb'
```

#### Discussion

Set the callback function to be called everytime the Speech Synthesis Manager is about to generate a word onthe speech channel. The `speechInfo` parameteris a pointer to an application-defined word callback function, whose syntax is described in [`SpeechWordProcPtr`](../speechwordprocptr.md).Passing `NULL` in `speechInfo` disablesthe word callback function.

This selector works with the `SetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552228-speech-channel_information_constants/sowordcallback)*