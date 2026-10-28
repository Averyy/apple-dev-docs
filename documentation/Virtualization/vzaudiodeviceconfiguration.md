# VZAudioDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class  
**Role**: Class

The base class for an audio device configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZAudioDeviceConfiguration
```

```objc
@interface VZAudioDeviceConfiguration : NSObject
```

## Overview

Don’t instantiate this abstract class directly. Instead, instantiate one of its subclasses such as [`VZVirtioSoundDeviceConfiguration`](./vzvirtiosounddeviceconfiguration.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [VZVirtioSoundDeviceConfiguration](./vzvirtiosounddeviceconfiguration.md)
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
- [class VZVirtioSoundDeviceOutputStreamConfiguration](./vzvirtiosounddeviceoutputstreamconfiguration.md)
  An object that defines a Virtio sound device output stream configuration.
- [class VZVirtioSoundDeviceInputStreamConfiguration](./vzvirtiosounddeviceinputstreamconfiguration.md)
  A PCM stream of input audio data, such as from a microphone.
- [class VZVirtioSoundDeviceStreamConfiguration](./vzvirtiosounddevicestreamconfiguration.md)
  An object that defines a Virtio sound device stream configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzaudiodeviceconfiguration)*