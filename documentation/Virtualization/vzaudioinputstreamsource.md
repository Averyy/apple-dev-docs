# VZAudioInputStreamSource

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for an audio input stream source.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZAudioInputStreamSource
```

```objc
@interface VZAudioInputStreamSource : NSObject
```

## Overview

An audio input stream source defines how th guest produces audio input data on the host system.

Don’t instantiate `VZAudioInputStreamSource` directly, use one of its subclasses such as [`VZHostAudioInputStreamSource`](./vzhostaudioinputstreamsource.md) instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZHostAudioInputStreamSource](./vzhostaudioinputstreamsource.md)
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
- [class VZAudioOutputStreamSink](./vzaudiooutputstreamsink.md)
  The base class for an audio output stream sink.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzaudioinputstreamsource)*