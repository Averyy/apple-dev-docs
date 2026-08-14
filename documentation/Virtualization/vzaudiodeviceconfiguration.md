# VZAudioDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

The base class for an audio device configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZAudioDeviceConfiguration
```

#### Overview

Don’t instantiate this abstract class directly. Instead, instantiate one of its subclasses such as [`VZVirtioSoundDeviceConfiguration`](vzvirtiosounddeviceconfiguration.md).

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [VZVirtioSoundDeviceConfiguration](vzvirtiosounddeviceconfiguration.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class VZVirtioSoundDeviceConfiguration](vzvirtiosounddeviceconfiguration.md)
  An object that defines a Virtio sound device configuration.
- [class VZVirtioSoundDeviceOutputStreamConfiguration](vzvirtiosounddeviceoutputstreamconfiguration.md)
  An object that defines a Virtio sound device output stream configuration.
- [class VZVirtioSoundDeviceInputStreamConfiguration](vzvirtiosounddeviceinputstreamconfiguration.md)
  A PCM stream of input audio data, such as from a microphone.
- [class VZVirtioSoundDeviceStreamConfiguration](vzvirtiosounddevicestreamconfiguration.md)
  An object that defines a Virtio sound device stream configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzaudiodeviceconfiguration)*