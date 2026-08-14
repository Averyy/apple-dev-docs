# VZAudioOutputStreamSink

**Framework**: Virtualization  
**Kind**: class

The base class for an audio output stream sink.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZAudioOutputStreamSink
```

#### Overview

An audio output stream sink defines how the host system consumes audio data from a guest.

Don’t instantiate `VZAudioOutputStreamSink` directly, use one of its subclasses, such as [`VZHostAudioOutputStreamSink`](vzhostaudiooutputstreamsink.md) instead.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZHostAudioOutputStreamSink](vzhostaudiooutputstreamsink.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZHostAudioOutputStreamSink](vzhostaudiooutputstreamsink.md)
  Host audio output stream sink plays audio to the host system’s default output device.
- [class VZHostAudioInputStreamSource](vzhostaudioinputstreamsource.md)
  The host audio input stream source that provides audio from the host system’s default input device.
- [class VZAudioInputStreamSource](vzaudioinputstreamsource.md)
  The base class for an audio input stream source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzaudiooutputstreamsink)*