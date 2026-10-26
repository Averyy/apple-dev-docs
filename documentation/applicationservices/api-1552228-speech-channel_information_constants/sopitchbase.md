# soPitchBase

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
soPitchBase = 'pbas'
```

#### Discussion

Get or set the speech channel’s baselinespeech pitch. This selector is intended for use by the Speech SynthesisManager; ordinarily, an application uses the [`GetSpeechPitch`](../api-1464774-getspeechpitch.md) and [`SetSpeechPitch`](../api-1462674-setspeechpitch.md) functions.The `speechInfo` parameteris a pointer to a variable of type `Fixed`.

This selector works with both the `GetSpeechInfo` and `SetSpeechInfo` functions.

> **Note**: The change in speech pitch may not be noticeable until the next sentence or paragraph is spoken.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552228-speech-channel_information_constants/sopitchbase)*