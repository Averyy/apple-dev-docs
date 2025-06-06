# VZHostAudioOutputStreamSink

**Framework**: Virtualization  
**Kind**: class

Host audio output stream sink plays audio to the host system’s default output device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZHostAudioOutputStreamSink
```

#### Overview

Host output data goes to the same device that [`AudioQueueNewOutput(_:_:_:_:_:_:_:)`](https://developer.apple.com/documentation/AudioToolbox/AudioQueueNewOutput(_:_:_:_:_:_:_:)) uses.

## Topics

### Creating the audio output stream sink
- [init()](vzhostaudiooutputstreamsink/init.md)
  Creates a new host audio output stream sink instance.

## Relationships

### Inherits From
- [VZAudioOutputStreamSink](vzaudiooutputstreamsink.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioSoundDeviceInputStreamConfiguration](vzvirtiosounddeviceinputstreamconfiguration.md)
  A PCM stream of input audio data, such as from a microphone.
- [class VZHostAudioInputStreamSource](vzhostaudioinputstreamsource.md)
  The host audio input stream source that provides audio from the host system’s default input device.
- [class VZAudioOutputStreamSink](vzaudiooutputstreamsink.md)
  The base class for an audio output stream sink.
- [class VZAudioInputStreamSource](vzaudioinputstreamsource.md)
  The base class for an audio input stream source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzhostaudiooutputstreamsink)*