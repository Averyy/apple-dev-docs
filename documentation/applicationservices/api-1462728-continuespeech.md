# ContinueSpeech(_:)

**Framework**: Application Services  
**Kind**: func

Resumes speech paused by the `PauseSpeechAt` function.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func ContinueSpeech(_ chan: SpeechChannel) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

At any time after the `PauseSpeechAt` functionis called, the `ContinueSpeech` functioncan be called to continue speaking from the beginning of the wordin which speech paused. Calling `ContinueSpeech` ona channel that is not currently in a paused state has no effecton the speech channel or on future calls to the `PauseSpeechAt` function.If you call `ContinueSpeech` ona channel before a pause is effective, `ContinueSpeech` cancelsthe pause.

If the `PauseSpeechAt` functionstopped speech in the middle of a word, the Speech Synthesis Managerwill start speaking that word from the beginning when you call `ContinueSpeech`. 

## Parameters

- `chan`: The paused speech channel on which speech is to be resumed.

## See Also

- [func PauseSpeechAt(SpeechChannel, Int32) -> OSErr](1461174-pausespeechat.md)
  Pauses speech on a speech channel.
- [func SpeakCFString(SpeechChannel, CFString, CFDictionary?) -> OSErr](1461621-speakcfstring.md)
  Begins speaking a string represented as a `CFString` object.
- [func StopSpeech(SpeechChannel) -> OSErr](1462745-stopspeech.md)
  Terminates speech immediately on the specified channel.
- [func StopSpeechAt(SpeechChannel, Int32) -> OSErr](1459780-stopspeechat.md)
  Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462728-continuespeech)*