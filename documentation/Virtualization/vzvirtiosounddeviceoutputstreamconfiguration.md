# VZVirtioSoundDeviceOutputStreamConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

An object that defines a Virtio sound device output stream configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZVirtioSoundDeviceOutputStreamConfiguration
```

```objc
@interface VZVirtioSoundDeviceOutputStreamConfiguration : VZVirtioSoundDeviceStreamConfiguration
```

## Mentions

- [Creating and Running a Linux Virtual Machine](./creating-and-running-a-linux-virtual-machine.md)

#### Overview

A PCM stream of output audio data, such as to a speaker.

## Topics

### Creating an output stream configuration
- [init()](./vzvirtiosounddeviceoutputstreamconfiguration/init%28%29.md)
  Creates a new sounds device output stream configuration.
### Accessing the sound sink
- [var sink: VZAudioOutputStreamSink?](./vzvirtiosounddeviceoutputstreamconfiguration/sink.md)
  An audio stream sink that defines how the host handles audio data produced by the guest.
### Output sink
- [class VZHostAudioOutputStreamSink](./vzhostaudiooutputstreamsink.md)
  Host audio output stream sink plays audio to the host system’s default output device.
- [class VZAudioOutputStreamSink](./vzaudiooutputstreamsink.md)
  The base class for an audio output stream sink.

## Relationships

### Inherits From
- [VZVirtioSoundDeviceStreamConfiguration](./vzvirtiosounddevicestreamconfiguration.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configurations
- [class VZVirtioSoundDeviceConfiguration](./vzvirtiosounddeviceconfiguration.md)
  An object that defines a Virtio sound device configuration.
- [class VZVirtioSoundDeviceInputStreamConfiguration](./vzvirtiosounddeviceinputstreamconfiguration.md)
  A PCM stream of input audio data, such as from a microphone.
- [class VZAudioDeviceConfiguration](./vzaudiodeviceconfiguration.md)
  The base class for an audio device configuration.
- [class VZVirtioSoundDeviceStreamConfiguration](./vzvirtiosounddevicestreamconfiguration.md)
  An object that defines a Virtio sound device stream configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosounddeviceoutputstreamconfiguration)*