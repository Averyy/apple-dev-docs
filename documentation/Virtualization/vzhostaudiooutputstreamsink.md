# VZHostAudioOutputStreamSink

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

Host audio output stream sink plays audio to the host system’s default output device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZHostAudioOutputStreamSink
```

```objc
@interface VZHostAudioOutputStreamSink : VZAudioOutputStreamSink
```

#### Overview

Host output data goes to the same device that [`AudioQueueNewOutput(_:_:_:_:_:_:_:)`](../AudioToolbox/audioqueuenewoutput%28_,_,_,_,_,_,_%29.md) uses.

## Topics

### Creating the audio output stream sink
- [init()](./vzhostaudiooutputstreamsink/init%28%29.md)
  Creates a new host audio output stream sink instance.

## Relationships

### Inherits From
- [VZAudioOutputStreamSink](./vzaudiooutputstreamsink.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Related Documentation
- [class VZVirtioSoundDeviceInputStreamConfiguration](./vzvirtiosounddeviceinputstreamconfiguration.md)
  A PCM stream of input audio data, such as from a microphone.
### Audio streams
- [class VZHostAudioInputStreamSource](./vzhostaudioinputstreamsource.md)
  The host audio input stream source that provides audio from the host system’s default input device.
- [class VZAudioOutputStreamSink](./vzaudiooutputstreamsink.md)
  The base class for an audio output stream sink.
- [class VZAudioInputStreamSource](./vzaudioinputstreamsource.md)
  The base class for an audio input stream source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzhostaudiooutputstreamsink)*