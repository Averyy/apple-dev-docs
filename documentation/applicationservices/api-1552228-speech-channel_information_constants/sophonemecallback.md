# soPhonemeCallBack

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
soPhonemeCallBack = 'phcb'
```

## Discussion

Set the callback function to be called everytime the Speech Synthesis Manager is about to generate a phonemeon the speech channel. The `speechInfo` parameteris a pointer to an application-defined phoneme callback function,whose syntax is described in [`SpeechPhonemeProcPtr`](../speechphonemeprocptr.md). Passing `NULL` in `speechInfo` disablesthe phoneme callback function.

This selector works with the `SetSpeechInfo` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552228-speech-channel_information_constants/sophonemecallback)*