# CopySpeechProperty(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Gets the value associated with the specified property of a speech channel.

**Availability**:
- macOS 10.5+ - Deprecated in 13.0

## Declaration

```swift
func CopySpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: UnsafeMutablePointer<CFTypeRef?>) -> OSErr
```

```c
OSErr CopySpeechProperty(SpeechChannel chan, CFStringRef property, CFTypeRef  _Nullable *object);
```

#### Return Value

A result code. See [Result Codes](./speech_synthesis_manager.md#1659745).

#### Discussion

The `CopySpeechProperty` function is the Core Foundation-based equivalent of the [`GetSpeechInfo`](./api-1552220-getspeechinfo.md) function.

## Parameters

- `chan`: The speech channel with which the specified property is associated.
- `property`: A speech-channel property about which information is being requested. See [Speech-Channel Properties](./speech_synthesis_manager/speech-channel_properties.md) for information on the properties you can specify.
- `object`: On return, a pointer to a Core Foundation object that holds the value of the specified property. The type of the object depends on the specific property passed in. For some properties, the value of `object` can be `NULL`. When the returned object is a `CFDictionary` object, you can use `CFDictionary` functions, such as [`CFDictionaryGetValue(_:_:)`](../CoreFoundation/cfdictionarygetvalue%28_,_%29.md), to retrieve the values associated with the keys that are associated with the specified property.

## See Also

### Obtaining Information About Speech and Speech Channels
- [func GetSpeechPitch(SpeechChannel, UnsafeMutablePointer<Fixed>) -> OSErr](./api-1464774-getspeechpitch.md)
  Gets a speech channel’s current speech pitch.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459075-copyspeechproperty)*