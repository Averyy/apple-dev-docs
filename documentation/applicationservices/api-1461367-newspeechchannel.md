# NewSpeechChannel(_:_:)

**Framework**: Application Services  
**Kind**: func

Creates a new speech channel.

**Availability**:
- macOS 10.0+ - Deprecated in 13.0

## Declaration

```swift
func NewSpeechChannel(_ voice: UnsafeMutablePointer<VoiceSpec>?, _ chan: UnsafeMutablePointer<SpeechChannel?>) -> OSErr
```

#### Return_value

A result code. See [`Result Codes`](speech_synthesis_manager#1659745.md).

#### Discussion

The `NewSpeechChannel` functionallocates memory for a speech channel structure and sets the speechchannel variable pointed to by the `chan` parameterto point to this speech channel structure. The Speech SynthesisManager automatically locates and opens a connection to the propersynthesizer for the voice specified by the `voice` parameter.

There is no predefined limit to the number of speech channelsan application can create. However, system constraints on availableRAM, processor loading, and number of available sound channels limitthe number of speech channels actually possible.

Your application should not attempt to manipulate the datapointed to by a variable of type `SpeechChannel`.The internal format that the Speech Synthesis Manager uses for speech channeldata is not documented and may change in future versions of systemsoftware. 

## Parameters

- `voice`: Specifying a voice means the initial speaking rate is determined by the synthesizer’s default speaking rate; passing   means the speaking rate is automatically set to the rate the user specifies in Speech preferences.
- `chan`: On return, a pointer to a valid speech channel.

## See Also

- [func DisposeSpeechChannel(SpeechChannel) -> OSErr](1462081-disposespeechchannel.md)
  Disposes of an existing speech channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461367-newspeechchannel)*