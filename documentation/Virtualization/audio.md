# Audio

**Framework**: Virtualization

Configure audio devices that enable the guest operating system to perform audio playback and capture through the host’s audio devices.

#### Overview

If your app can configure an audio input device, you must set an [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) message in your app’s `Info.plist.` The system uses this description when asking the user’s permission to enable microphone access. If this message isn’t set or the key isn’t present, the system denies microphone access to your app.

> **Note**:  To enable VIRTIO sound support in Linux guests, configure sound support in the kernel using the `CONFIG_SND_VIRTIO` kernel parameter.

You can add audio support to your guest with just a few lines of code. The example below shows how to configure a VM to expose a VIRTIO sound device that consists of an audio input and output on the guest that the system bridges to the host machine’s speakers and microphone:

## Topics

### Configurations
- [class VZVirtioSoundDeviceConfiguration](vzvirtiosounddeviceconfiguration.md)
  An object that defines a Virtio sound device configuration.
- [class VZVirtioSoundDeviceOutputStreamConfiguration](vzvirtiosounddeviceoutputstreamconfiguration.md)
  An object that defines a Virtio sound device output stream configuration.
- [class VZVirtioSoundDeviceInputStreamConfiguration](vzvirtiosounddeviceinputstreamconfiguration.md)
  A PCM stream of input audio data, such as from a microphone.
- [class VZAudioDeviceConfiguration](vzaudiodeviceconfiguration.md)
  The base class for an audio device configuration.
- [class VZVirtioSoundDeviceStreamConfiguration](vzvirtiosounddevicestreamconfiguration.md)
  An object that defines a Virtio sound device stream configuration.
### Audio streams
- [class VZHostAudioOutputStreamSink](vzhostaudiooutputstreamsink.md)
  Host audio output stream sink plays audio to the host system’s default output device.
- [class VZHostAudioInputStreamSource](vzhostaudioinputstreamsource.md)
  The host audio input stream source that provides audio from the host system’s default input device.
- [class VZAudioOutputStreamSink](vzaudiooutputstreamsink.md)
  The base class for an audio output stream sink.
- [class VZAudioInputStreamSource](vzaudioinputstreamsource.md)
  The base class for an audio input stream source.

## See Also

- [Graphics](graphics.md)
  Configure a device for a guest to display its UI.
- [Keyboards and pointing devices](keyboards-and-pointing-devices.md)
  Configure devices that connect a mouse and keyboard to the guest system.
- [Memory](memory.md)
  Configure a memory balloon device to change the allocated memory for the guest system.
- [Network](network.md)
  Configure the devices that connect the guest system to the network.
- [Randomization](randomization.md)
  Configure a device for the guest system to use to generate random numbers.
- [Serial ports](serial-ports.md)
  Configure the serial devices that you use to communicate with the guest system.
- [Shared directories](shared-directories.md)
  Configure devices that share directories from the host into the guest system.
- [Sockets](sockets.md)
  Configure a device that manages port-based communication with the guest system.
- [Storage](storage.md)
  Configure the block-storage devices that represent the disks of the guest system.
- [Consoles](consoles.md)
  Configure a device that manages multiport console communication with the guest system.
- [Clipboard sharing](clipboard-sharing.md)
  Share the pasteboard between the host and guest system.
- [USB Devices](usb-devices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/audio)*