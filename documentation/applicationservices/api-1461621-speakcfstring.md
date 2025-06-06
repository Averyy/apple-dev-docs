# SpeakCFString(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Begins speaking a string represented as a `CFString` object.

**Availability**:
- macOS 10.5+ - Deprecated in 13.0

## Declaration

```swift
func SpeakCFString(_ chan: SpeechChannel, _ aString: CFString, _ options: CFDictionary?) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `SpeakCFString` function is the Core Foundation-based equivalent of the [`SpeakBuffer`](1552252-speakbuffer.md) function.

The `SpeakCFString` function converts the text string specified in `aString` into speech, using the voice and control settings in effect for the speech channel specified in `chan`. (Before you use `SpeakCFString`, therefore, be sure you’ve created a speech channel with the [`NewSpeechChannel(_:_:)`](1461367-newspeechchannel.md) function.) The `SpeakCFString` function generates speech asynchronously, which means that control is returned to your application before speech has finished, perhaps even before the speech is first audible.

If `SpeakCFString` is called while the speech channel is currently speaking the contents of another text string, the speech stops immediately and the new text string is spoken as soon as possible.

## Parameters

- `chan`: The speech channel through which speech is to be spoken.
- `aString`: The string to be spoken, represented as a   object.
- `options`: An optional dictionary of key-value pairs used to customize speech behavior. See   for the available keys.

## See Also

- [func ContinueSpeech(SpeechChannel) -> OSErr](1462728-continuespeech.md)
  Resumes speech paused by the `PauseSpeechAt` function.
- [func PauseSpeechAt(SpeechChannel, Int32) -> OSErr](1461174-pausespeechat.md)
  Pauses speech on a speech channel.
- [func StopSpeech(SpeechChannel) -> OSErr](1462745-stopspeech.md)
  Terminates speech immediately on the specified channel.
- [func StopSpeechAt(SpeechChannel, Int32) -> OSErr](1459780-stopspeechat.md)
  Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461621-speakcfstring)*