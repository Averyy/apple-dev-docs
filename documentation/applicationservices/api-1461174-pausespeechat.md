# PauseSpeechAt(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Pauses speech on a speech channel.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func PauseSpeechAt(_ chan: SpeechChannel, _ whereToPause: Int32) -> OSErr
```

```c
OSErr PauseSpeechAt(SpeechChannel chan, SInt32 whereToPause);
```

#### Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

#### Discussion

The `PauseSpeechAt` functionmakes speech production pause at a specified point in the text. `PauseSpeechAt` returnsimmediately, although speech output will continue until the specifiedpoint.

You can determine whether your application has paused speechoutput on a speech channel by obtaining a speech status informationstructure through the `GetSpeechInfo` function.While a speech channel is paused, the speech status informationstructure indicates that `outputBusy` and `outputPaused` areboth `TRUE`.

If the end of the input text buffer is reached before thespecified pause point, speech output pauses at the end of the buffer.

The `PauseSpeechAt` functiondiffers from the `StopSpeech` and `StopSpeechAt` functionsin that a subsequent call to `ContinueSpeech`,described next, causes the contents of the current text buffer tocontinue being spoken.

If you plan to continue speech synthesis from a paused speechchannel, the text buffer being processed must remain available atall times and must not move while the channel is in a paused state. 

## Parameters

- `chan`: The speech channel on which speech is to be paused.
- `whereToPause`: A constant indicating when speech processing should be paused. Pass the constant `kImmediate` to pause immediately, even in the middle of a word. Pass `kEndOfWord` or `kEndOfSentence` to pause speech at the end of the current word or sentence, respectively. 

## See Also

### Starting, Stopping, and Pausing Speech
- [func ContinueSpeech(SpeechChannel) -> OSErr](./api-1462728-continuespeech.md)
  Resumes speech paused by the `PauseSpeechAt` function.
- [func SpeakCFString(SpeechChannel, CFString, CFDictionary?) -> OSErr](./api-1461621-speakcfstring.md)
  Begins speaking a string represented as a `CFString` object.
- [func StopSpeech(SpeechChannel) -> OSErr](./api-1462745-stopspeech.md)
  Terminates speech immediately on the specified channel.
- [func StopSpeechAt(SpeechChannel, Int32) -> OSErr](./api-1459780-stopspeechat.md)
  Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.
- [SpeakBuffer](./api-1552252-speakbuffer.md)
  Speaks a buffer of text, using certain flags to controlspeech behavior.
- [SpeakString](./api-1552250-speakstring.md)
  Begins speaking a text string.
- [SpeakText](./api-1552236-speaktext.md)
  Begins speaking a buffer of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461174-pausespeechat)*