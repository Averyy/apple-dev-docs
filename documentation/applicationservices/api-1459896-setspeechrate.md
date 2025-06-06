# SetSpeechRate(_:_:)

**Framework**: Application Services  
**Kind**: func

Sets the speech rate of a designated speech channel.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func SetSpeechRate(_ chan: SpeechChannel, _ rate: Fixed) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `SetSpeechRate` functionadjusts the speech rate on the speech channel specified by the `chan` parameterto the rate specified by the `rate` parameter.As a general rule, speaking rates range from around 150 words perminute to around 220 words per minute. It is important to keep inmind, however, that users will differ greatly in their ability to understandsynthesized speech at a particular rate based upon their level ofexperience listening to the voice and their ability to anticipatethe types of utterances they will encounter. 

Note: the new speech rate should be expressed as an integer (nota fixed point decimal number as the data type implies).

## Parameters

- `chan`: The speech channel whose rate you wish to set.
- `rate`: The new speech rate in words per minute, expressed as an integer value.

## See Also

- [func SetSpeechProperty(SpeechChannel, CFString, CFTypeRef?) -> OSErr](1459256-setspeechproperty.md)
  Sets the value of the specified speech-channel property.
- [func SetSpeechPitch(SpeechChannel, Fixed) -> OSErr](1462674-setspeechpitch.md)
  Sets the speech pitch on a designated speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459896-setspeechrate)*