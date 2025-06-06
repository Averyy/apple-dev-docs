# StopSpeech(_:)

**Framework**: Application Services  
**Kind**: func

Terminates speech immediately on the specified channel.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func StopSpeech(_ chan: SpeechChannel) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `StopSpeech` functionimmediately terminates speech on the channel specified by the `chan` parameter.After returning from `StopSpeech`,your application can safely release any text buffer that the speechsynthesizer has been using. You can call `StopSpeech` foran already idle channel without ill effect.

You can also stop speech by passing a zero-length string (or,in C, a `null` pointer)to one of the `SpeakString`, `SpeakText`,or `SpeakBuffer` functions.Doing this stops speech only in the specified speech channel (or,in the case of `SpeakString`,in the speech channel managed internally by the Speech SynthesisManager).

Before calling the `StopSpeech` function,you can use the `SpeechBusy` function,which is described in [`SpeechBusy()`](1464581-speechbusy.md),to determine if a synthesizer is still speaking. If you are working withmultiple speech channels, you can use the status selector with thefunction `GetSpeechInfo` whichis described in [`GetSpeechInfo`](1552220-getspeechinfo.md),to determine if a specific channel is still speaking. 

## Parameters

- `chan`: The speech channel on which speech is to be stopped.

## See Also

- [func ContinueSpeech(SpeechChannel) -> OSErr](1462728-continuespeech.md)
  Resumes speech paused by the `PauseSpeechAt` function.
- [func PauseSpeechAt(SpeechChannel, Int32) -> OSErr](1461174-pausespeechat.md)
  Pauses speech on a speech channel.
- [func SpeakCFString(SpeechChannel, CFString, CFDictionary?) -> OSErr](1461621-speakcfstring.md)
  Begins speaking a string represented as a `CFString` object.
- [func StopSpeechAt(SpeechChannel, Int32) -> OSErr](1459780-stopspeechat.md)
  Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462745-stopspeech)*