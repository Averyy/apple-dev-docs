# GetSpeechRate(_:_:)

**Framework**: Application Services  
**Kind**: func

Gets a speech channel’s current speech rate.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func GetSpeechRate(_ chan: SpeechChannel, _ rate: UnsafeMutablePointer<Fixed>) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

## Parameters

- `chan`: The speech channel whose rate you wish to determine.
- `rate`: On return, a pointer to the speech channel’s speech rate in words per minute, expressed as an integer value.

## See Also

- [func CopySpeechProperty(SpeechChannel, CFString, UnsafeMutablePointer<CFTypeRef?>) -> OSErr](1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [func SpeechBusy() -> Int16](1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [func SpeechBusySystemWide() -> Int16](1460113-speechbusysystemwide.md)
  Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.
- [func SpeechManagerVersion() -> NumVersion](1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1460797-getspeechrate)*