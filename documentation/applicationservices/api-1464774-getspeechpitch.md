# GetSpeechPitch(_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Gets a speech channel’s current speech pitch.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func GetSpeechPitch(_ chan: SpeechChannel, _ pitch: UnsafeMutablePointer<Fixed>) -> OSErr
```

```c
OSErr GetSpeechPitch(SpeechChannel chan, Fixed *pitch);
```

## Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

## Discussion

Typical voice frequencies range from around 90 hertz for alow-pitched male voice to perhaps 300 hertz for a high-pitched child’svoice. These frequencies correspond to approximate pitch valuesin the ranges of 30.000 to 40.000 and 55.000 to 65.000, respectively.

## Parameters

- `chan`: The speech channel whose pitch you wish to determine.
- `pitch`: On return, a pointer to the current pitch of the voice in the speech channel, expressed as a fixed-point frequency value.

## See Also

### Obtaining Information About Speech and Speech Channels
- [func CopySpeechProperty(SpeechChannel, CFString, UnsafeMutablePointer<CFTypeRef?>) -> OSErr](./api-1459075-copyspeechproperty.md)
  Gets the value associated with the specified property of a speech channel.
- [func GetSpeechRate(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](./api-1460797-getspeechrate.md)
  Gets a speech channel’s current speech rate.
- [func SpeechBusy() -> Int16](./api-1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [func SpeechBusySystemWide() -> Int16](./api-1460113-speechbusysystemwide.md)
  Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.
- [func SpeechManagerVersion() -> NumVersion](./api-1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.
- [GetSpeechInfo](./api-1552220-getspeechinfo.md)
  Gets information about a designated speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464774-getspeechpitch)*