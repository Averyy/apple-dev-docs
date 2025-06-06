# SetSpeechPitch(_:_:)

**Framework**: Application Services  
**Kind**: func

Sets the speech pitch on a designated speech channel.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func SetSpeechPitch(_ chan: SpeechChannel, _ pitch: Fixed) -> OSErr
```

#### Return_value

A resultcode. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `SetSpeechPitch` functionchanges the current speech pitch on the speech channel specifiedby the `chan` parameterto the pitch specified by the `pitch` parameter.Typical voice frequencies range from around 90 hertz for a low-pitchedmale voice to perhaps 300 hertz for a high-pitched child’s voice.These frequencies correspond to approximate pitch values in theranges of 30.000 to 40.000 and 55.000 to 65.000, respectively. Althoughfixed-point values allow you to specify a wide range of pitches,not all synthesizers will support the full range of pitches. Ifyour application specifies a pitch that a synthesizer cannot handle, itmay adjust the pitch to fit within an acceptable range. 

## Parameters

- `chan`: The speech channel whose pitch you wish to set.
- `pitch`: The new pitch for the speech channel, expressed as a fixed-point frequency value.

## See Also

- [func SetSpeechProperty(SpeechChannel, CFString, CFTypeRef?) -> OSErr](1459256-setspeechproperty.md)
  Sets the value of the specified speech-channel property.
- [func SetSpeechRate(SpeechChannel, Fixed) -> OSErr](1459896-setspeechrate.md)
  Sets the speech rate of a designated speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462674-setspeechpitch)*