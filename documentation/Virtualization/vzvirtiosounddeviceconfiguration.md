# VZVirtioSoundDeviceConfiguration

**Framework**: Virtualization  
**Kind**: class

An object that defines a Virtio sound device configuration.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class VZVirtioSoundDeviceConfiguration
```

#### Overview

Use a `VZVirtioSoundDeviceConfiguration` object to configure an audio device for your VM. After creating this object, assign appropriate values to the [`streams`](vzvirtiosounddeviceconfiguration/streams.md) array property which defines the behaviors of the underlying audio streams for this audio device.

After creating and configuring a `VZVirtioSoundDeviceConfiguration` object, assign it to the [`audioDevices`](vzvirtualmachineconfiguration/audiodevices.md) property of your VM’s configuration.

## Topics

### Creating a sound device configuration
- [init()](vzvirtiosounddeviceconfiguration/init.md)
  Creates a new sound device configuration.
### Accessing the sound streams
- [var streams: [VZVirtioSoundDeviceStreamConfiguration]](vzvirtiosounddeviceconfiguration/streams.md)
  List of audio streams exposed by this device.

## Relationships

### Inherits From
- [VZAudioDeviceConfiguration](vzaudiodeviceconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class VZVirtioSoundDeviceOutputStreamConfiguration](vzvirtiosounddeviceoutputstreamconfiguration.md)
  An object that defines a Virtio sound device output stream configuration.
- [class VZVirtioSoundDeviceInputStreamConfiguration](vzvirtiosounddeviceinputstreamconfiguration.md)
  A PCM stream of input audio data, such as from a microphone.
- [class VZAudioDeviceConfiguration](vzaudiodeviceconfiguration.md)
  The base class for an audio device configuration.
- [class VZVirtioSoundDeviceStreamConfiguration](vzvirtiosounddevicestreamconfiguration.md)
  An object that defines a Virtio sound device stream configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtiosounddeviceconfiguration)*