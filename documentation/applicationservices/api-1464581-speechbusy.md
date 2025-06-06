# SpeechBusy()

**Framework**: Application Services  
**Kind**: func

Determines whether any channels of speech are currentlysynthesizing speech.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func SpeechBusy() -> Int16
```

#### Return_value

The number of speechchannels that are currently synthesizing speech in the application.This is useful when you want to ensure that an earlier speech requesthas been completed before having the system speak again. Pausedspeech channels are counted among those that are synthesizing speech.

   The speech channel that the Speech Synthesis Manager allocatesinternally in response to calls to the `SpeakString` functionis counted in the number returned by `SpeechBusy`. Thus,if you use just `SpeakString` toinitiate speech, `SpeechBusy` alwaysreturns `1` as long as speech is being produced. When `SpeechBusy` returns`0`, all speech has finished.

## See Also

- [func CopySpeechProperty(SpeechChannel, CFString, UnsafeMutablePointer<CFTypeRef?>) -> OSErr](1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [func GetSpeechRate(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1460797-getspeechrate.md)
  Gets a speech channel’s current speech rate.
- [func SpeechBusySystemWide() -> Int16](1460113-speechbusysystemwide.md)
  Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.
- [func SpeechManagerVersion() -> NumVersion](1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464581-speechbusy)*