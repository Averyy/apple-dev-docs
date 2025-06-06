# DisposeSpeechChannel(_:)

**Framework**: Application Services  
**Kind**: func

Disposes of an existing speech channel.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func DisposeSpeechChannel(_ chan: SpeechChannel) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `DisposeSpeechChannel` functiondisposes of the speech channel specified in the `chan` parameterand releases all memory the channel occupies. If the speech channelspecified is producing speech, then the `DisposeSpeechChannel` functionimmediately stops speech before disposing of the channel. If youhave defined a text-done callback function or a speech-done callbackfunction, the function will not be called before the channel is disposedof.

The Speech Synthesis Manager releases any speech channelsthat have not been explicitly disposed of by an application whenthe application quits. In general, however, your application shoulddispose of any speech channels it has created whenever it receivesa suspend event. This ensures that other applications can take fulladvantage of Speech Synthesis Manager and Sound Manager capabilities. 

## Parameters

- `chan`: The speech channel to dispose of.

## See Also

- [func NewSpeechChannel(UnsafeMutablePointer<VoiceSpec>?, UnsafeMutablePointer<SpeechChannel?>) -> OSErr](1461367-newspeechchannel.md)
  Creates a new speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462081-disposespeechchannel)*