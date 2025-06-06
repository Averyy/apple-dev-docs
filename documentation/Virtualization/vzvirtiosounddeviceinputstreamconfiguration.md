# VZVirtioSoundDeviceInputStreamConfiguration

**Framework**: Virtualization  
**Kind**: class

A PCM stream of input audio data, such as from a microphone.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZVirtioSoundDeviceInputStreamConfiguration
```

#### Overview

This device represents a PCM stream of audio data. Don’t instantiate `VZVirtioSoundDeviceStreamConfiguration` directly. Instead, use one of its subclasses such as [`VZVirtioSoundDeviceInputStreamConfiguration`](vzvirtiosounddeviceinputstreamconfiguration.md) or [`VZVirtioSoundDeviceOutputStreamConfiguration`](vzvirtiosounddeviceoutputstreamconfiguration.md).

## Topics

### Creating an input stream configuration
- [init()](vzvirtiosounddeviceinputstreamconfiguration/init.md)
  Creates a new sound device input stream configuration.
### Accessing the sound source
- [var source: VZAudioInputStreamSource?](vzvirtiosounddeviceinputstreamconfiguration/source.md)
  An audio stream source that defines how the host supplies audio data for the guest.
### Input source
- [class VZHostAudioInputStreamSource](vzhostaudioinputstreamsource.md)
  The host audio input stream source that provides audio from the host system’s default input device.
- [class VZAudioInputStreamSource](vzaudioinputstreamsource.md)
  The base class for an audio input stream source.

## Relationships

### Inherits From
- [VZVirtioSoundDeviceStreamConfiguration](vzvirtiosounddevicestreamconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioSoundDeviceConfiguration](vzvirtiosounddeviceconfiguration.md)
  An object that defines a Virtio sound device configuration.
- [class VZVirtioSoundDeviceOutputStreamConfiguration](vzvirtiosounddeviceoutputstreamconfiguration.md)
  An object that defines a Virtio sound device output stream configuration.
- [class VZAudioDeviceConfiguration](vzaudiodeviceconfiguration.md)
  The base class for an audio device configuration.
- [class VZVirtioSoundDeviceStreamConfiguration](vzvirtiosounddevicestreamconfiguration.md)
  An object that defines a Virtio sound device stream configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosounddeviceinputstreamconfiguration)*