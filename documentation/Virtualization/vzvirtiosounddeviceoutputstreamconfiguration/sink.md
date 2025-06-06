# sink

**Framework**: Virtualization  
**Kind**: property

An audio stream sink that defines how the host handles audio data produced by the guest.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var sink: VZAudioOutputStreamSink? { get set }
```

#### Discussion

Not specifying a sink results in a default handler that suppresses the audio. The default is `nil`.

## See Also

- [class VZAudioOutputStreamSink](vzaudiooutputstreamsink.md)
  The base class for an audio output stream sink.
- [class VZHostAudioOutputStreamSink](vzhostaudiooutputstreamsink.md)
  Host audio output stream sink plays audio to the host system’s default output device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosounddeviceoutputstreamconfiguration/sink)*