# VZHostAudioInputStreamSource

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The host audio input stream source that provides audio from the host system’s default input device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZHostAudioInputStreamSource
```

```objc
@interface VZHostAudioInputStreamSource : VZAudioInputStreamSource
```

#### Overview

The host input data comes from the same device that [`AudioQueueNewInput(_:_:_:_:_:_:_:)`](../AudioToolbox/audioqueuenewinput%28_,_,_,_,_,_,_%29.md) uses.

## Topics

### Creating the audio input stream source
- [init()](./vzhostaudioinputstreamsource/init%28%29.md)
  Creates a new audio input stream source.

## Relationships

### Inherits From
- [VZAudioInputStreamSource](./vzaudioinputstreamsource.md)
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
- [class VZAudioOutputStreamSink](./vzaudiooutputstreamsink.md)
  The base class for an audio output stream sink.
- [class VZAudioInputStreamSource](./vzaudioinputstreamsource.md)
  The base class for an audio input stream source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzhostaudioinputstreamsource)*