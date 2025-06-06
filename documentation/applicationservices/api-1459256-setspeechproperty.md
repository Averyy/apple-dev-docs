# SetSpeechProperty(_:_:_:)

**Framework**: Application Services  
**Kind**: func

Sets the value of the specified speech-channel property.

**Availability**:
- macOS 10.5+ - Deprecated in 13.0

## Declaration

```swift
func SetSpeechProperty(_ chan: SpeechChannel, _ property: CFString, _ object: CFTypeRef?) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `SetSpeechProperty` function is the Core Foundation-based equivalent of the [`SetSpeechInfo`](1552223-setspeechinfo.md) function.

See [`Speech-Channel Properties`](speech_synthesis_manager/speech-channel_properties.md) for information on the properties you can specify.

## Parameters

- `chan`: The speech channel whose property to set.
- `property`: The speech-channel property to set to the specified value.
- `object`: The value to which the specified speech-channel property should be set. For some properties, this value can be  .

## See Also

- [func SetSpeechPitch(SpeechChannel, Fixed) -> OSErr](1462674-setspeechpitch.md)
  Sets the speech pitch on a designated speech channel.
- [func SetSpeechRate(SpeechChannel, Fixed) -> OSErr](1459896-setspeechrate.md)
  Sets the speech rate of a designated speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459256-setspeechproperty)*