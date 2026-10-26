# GetSpeechRate(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Gets a speech channel’s current speech rate.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func GetSpeechRate(_ chan: SpeechChannel, _ rate: UnsafeMutablePointer<Fixed>) -> OSErr
```

```c
OSErr GetSpeechRate(SpeechChannel chan, Fixed *rate);
```

#### Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

## Parameters

- `chan`: The speech channel whose rate you wish to determine.
- `rate`: On return, a pointer to the speech channel’s speech rate in words per minute, expressed as an integer value.

## See Also

### Obtaining Information About Speech and Speech Channels
- [func CopySpeechProperty(SpeechChannel, CFString, UnsafeMutablePointer<CFTypeRef?>) -> OSErr](./api-1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](./api-1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [func SpeechBusy() -> Int16](./api-1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [func SpeechBusySystemWide() -> Int16](./api-1460113-speechbusysystemwide.md)
  Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.
- [func SpeechManagerVersion() -> NumVersion](./api-1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.
- [GetSpeechInfo](./api-1552220-getspeechinfo.md)
  Gets information about a designated speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460797-getspeechrate)*