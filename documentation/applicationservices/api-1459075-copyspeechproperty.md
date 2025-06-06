# CopySpeechProperty(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Gets the value associated with the specified property of a speech channel.

**Availability**:
- macOS 10.5+ - Deprecated in 13.0

## Declaration

```swift
func CopySpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: UnsafeMutablePointer<CFTypeRef?>) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `CopySpeechProperty` function is the Core Foundation-based equivalent of the [`GetSpeechInfo`](1552220-getspeechinfo.md) function.

## Parameters

- `chan`: The speech channel with which the specified property is associated.
- `property`: A speech-channel property about which information is being requested. See   for information on the properties you can specify.
- `object`: On return, a pointer to a Core Foundation object that holds the value of the specified property. The type of the object depends on the specific property passed in. For some properties, the value of   can be  . When the returned object is a   object, you can use   functions, such as  , to retrieve the values associated with the keys that are associated with the specified property.

## See Also

- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
- [func GetSpeechRate(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](1460797-getspeechrate.md)
  Gets a speech channel’s current speech rate.
- [func SpeechBusy() -> Int16](1464581-speechbusy.md)
  Determines whether any channels of speech are currentlysynthesizing speech.
- [func SpeechBusySystemWide() -> Int16](1460113-speechbusysystemwide.md)
  Determines if any speech is currently being synthesizedin your application or elsewhere on the computer.
- [func SpeechManagerVersion() -> NumVersion](1462334-speechmanagerversion.md)
  Determines the current version of the Speech SynthesisManager installed in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459075-copyspeechproperty)*