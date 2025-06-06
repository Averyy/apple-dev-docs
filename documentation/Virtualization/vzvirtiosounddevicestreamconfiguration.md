# VZVirtioSoundDeviceStreamConfiguration

**Framework**: Virtualization  
**Kind**: class

An object that defines a Virtio sound device stream configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZVirtioSoundDeviceStreamConfiguration
```

#### Overview

A `VZVirtioSoundDeviceStreamConfiguration` object represents a PCM stream of audio data. Don’t instantiate this class directly. Instead, instantiate one of its subclasses such as [`VZVirtioSoundDeviceInputStreamConfiguration`](vzvirtiosounddeviceinputstreamconfiguration.md) or [`VZVirtioSoundDeviceOutputStreamConfiguration`](vzvirtiosounddeviceoutputstreamconfiguration.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [VZVirtioSoundDeviceInputStreamConfiguration](vzvirtiosounddeviceinputstreamconfiguration.md)
- [VZVirtioSoundDeviceOutputStreamConfiguration](vzvirtiosounddeviceoutputstreamconfiguration.md)
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
- [class VZVirtioSoundDeviceInputStreamConfiguration](vzvirtiosounddeviceinputstreamconfiguration.md)
  A PCM stream of input audio data, such as from a microphone.
- [class VZAudioDeviceConfiguration](vzaudiodeviceconfiguration.md)
  The base class for an audio device configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosounddevicestreamconfiguration)*