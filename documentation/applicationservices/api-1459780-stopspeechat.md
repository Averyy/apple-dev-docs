# StopSpeechAt(_:_:)

**Framework**: Application Services  
**Kind**: func

Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func StopSpeechAt(_ chan: SpeechChannel, _ whereToStop: Int32) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `StopSpeechAt` functionhalts the production of speech on the channel specified by `chan` ata specified point in the text. This function returns immediately,although speech output continues until the specified point has beenreached.

If you call the `StopSpeechAt` functionbefore the Speech Synthesis Manager finishes processing input text,then the function might return before some input text has yet tobe spoken. Thus, before disposing of the text buffer, your applicationshould wait until its text-done callback function has been called(if one has been defined), or until it can determine (by, for exampleobtaining a speech status information structure) that the SpeechSynthesis Manager is no longer processing input text.

If the end of the input text buffer is reached before thespecified stopping point, the speech synthesizer stops at the endof the buffer without generating an error. 

## Parameters

- `chan`: The speech channel on which speech is to be stopped.
- `whereToStop`: A constant indicating when speech processing should stop. Pass the constant   to stop immediately, even in the middle of a word. Pass   or   to stop speech at the end of the current word or sentence, respectively. 

## See Also

- [func ContinueSpeech(SpeechChannel) -> OSErr](1462728-continuespeech.md)
  Resumes speech paused by the `PauseSpeechAt` function.
- [func PauseSpeechAt(SpeechChannel, Int32) -> OSErr](1461174-pausespeechat.md)
  Pauses speech on a speech channel.
- [func SpeakCFString(SpeechChannel, CFString, CFDictionary?) -> OSErr](1461621-speakcfstring.md)
  Begins speaking a string represented as a `CFString` object.
- [func StopSpeech(SpeechChannel) -> OSErr](1462745-stopspeech.md)
  Terminates speech immediately on the specified channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459780-stopspeechat)*