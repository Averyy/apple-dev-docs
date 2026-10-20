# VZAudioOutputStreamSink

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for an audio output stream sink.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZAudioOutputStreamSink
```

```objc
@interface VZAudioOutputStreamSink : NSObject
```

#### Overview

An audio output stream sink defines how the host system consumes audio data from a guest.

Don’t instantiate `VZAudioOutputStreamSink` directly, use one of its subclasses, such as [`VZHostAudioOutputStreamSink`](./vzhostaudiooutputstreamsink.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZHostAudioOutputStreamSink](./vzhostaudiooutputstreamsink.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Audio streams
- [class VZHostAudioOutputStreamSink](./vzhostaudiooutputstreamsink.md)
  Host audio output stream sink plays audio to the host system’s default output device.
- [class VZHostAudioInputStreamSource](./vzhostaudioinputstreamsource.md)
  The host audio input stream source that provides audio from the host system’s default input device.
- [class VZAudioInputStreamSource](./vzaudioinputstreamsource.md)
  The base class for an audio input stream source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzaudiooutputstreamsink)*