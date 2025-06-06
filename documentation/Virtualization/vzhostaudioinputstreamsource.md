# VZHostAudioInputStreamSource

**Framework**: Virtualization  
**Kind**: class

The host audio input stream source that provides audio from the host system’s default input device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZHostAudioInputStreamSource
```

#### Overview

The host input data comes from the same device that [`AudioQueueNewInput(_:_:_:_:_:_:_:)`](https://developer.apple.com/documentation/AudioToolbox/AudioQueueNewInput(_:_:_:_:_:_:_:)) uses.

## Topics

### Creating the audio input stream source
- [init()](vzhostaudioinputstreamsource/init.md)
  Creates a new audio input stream source.

## Relationships

### Inherits From
- [VZAudioInputStreamSource](vzaudioinputstreamsource.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZHostAudioOutputStreamSink](vzhostaudiooutputstreamsink.md)
  Host audio output stream sink plays audio to the host system’s default output device.
- [class VZAudioOutputStreamSink](vzaudiooutputstreamsink.md)
  The base class for an audio output stream sink.
- [class VZAudioInputStreamSource](vzaudioinputstreamsource.md)
  The base class for an audio input stream source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzhostaudioinputstreamsource)*