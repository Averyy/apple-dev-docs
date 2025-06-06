# Audio

**Framework**: Kernel

Implement a driver that interacts with audio hardware. 

## Topics

### Interfaces
- [IOAudioLevelControl](ioaudiolevelcontrol.md)
- [IOAudioSelectorControl](ioaudioselectorcontrol.md)
- [IOAudioToggleControl](ioaudiotogglecontrol.md)
- [IOAudioControl](ioaudiocontrol.md)
  Represents any controllable attribute of an IOAudioDevice.
- [IOAudioEngine](ioaudioengine.md)
  Abstract base class for a single audio audio / I/O engine.
- [IOAudioStream](ioaudiostream.md)
  This class wraps a single sample buffer in an audio driver.
- [IOAudioPort](ioaudioport.md)
  Represents a logical or physical port or functional unit in an audio device.
### Devices
- [IOAudioDevice](ioaudiodevice.md)
  Abstract base class for a single piece of audio hardware. The IOAudioDevice provides the central coordination point for an audio driver.
### User-Space Access
- [IOAudioControlUserClient](ioaudiocontroluserclient.md)
- [IOAudioEngineUserClient](ioaudioengineuserclient.md)
### Descriptors
- [IOAudioBufferDataDescriptor](ioaudiobufferdatadescriptor.md)
- [IOAudioSampleIntervalDescriptor](ioaudiosampleintervaldescriptor.md)
- [IOAudioStreamDataDescriptor](ioaudiostreamdatadescriptor.md)
### Audio Data
- [IOAudioEngineNotifications](ioaudioenginenotifications.md)
- [IOAudioEngineTraps](ioaudioenginetraps.md)
- [IOAudioSampleRate](ioaudiosamplerate.md)
- [IOAudioStreamFormat](ioaudiostreamformat.md)
- [IOAudioStreamFormatExtension](ioaudiostreamformatextension.md)
- [IOAudioTimeStamp](ioaudiotimestamp.md)
- [IOAudioClientBuffer](ioaudioclientbuffer.md)
- [IOAudioClientBuffer64](ioaudioclientbuffer64.md)
- [IOAudioClientBufferExtendedInfo](ioaudioclientbufferextendedinfo.md)
- [IOAudioClientBufferExtendedInfo64](ioaudioclientbufferextendedinfo64.md)
- [IOAudioEnginePosition](ioaudioengineposition.md)
  Represents a position in an audio audio engine.
- [IOAF_bcopy_WriteCombine](1416189-ioaf_bcopy_writecombine.md)
  An efficient bcopy from "write combine" memory to regular memory. It is safe to assume that all memory has been copied when the function has completed
- [UInt64mult](1402722-uint64mult.md)
### Conversions
- [IOAF_Float32ToInt8](3242800-ioaf_float32toint8.md)
- [IOAF_Float32ToNativeInt16](1416160-ioaf_float32tonativeint16.md)
  Converts 32-bit floating point to native 16-bit integer
- [IOAF_Float32ToNativeInt24](1416158-ioaf_float32tonativeint24.md)
  Converts 32-bit floating point to native 24-bit integer
- [IOAF_Float32ToNativeInt32](1416171-ioaf_float32tonativeint32.md)
  Converts 32-bit floating point to native 32-bit integer
- [IOAF_Float32ToSwapInt16](1416149-ioaf_float32toswapint16.md)
  Converts 32-bit floating point to non-native 16-bit integer
- [IOAF_Float32ToSwapInt24](1416187-ioaf_float32toswapint24.md)
  Converts 32-bit floating point to non-native 24-bit integer
- [IOAF_Float32ToSwapInt32](1416170-ioaf_float32toswapint32.md)
  Converts 32-bit floating point to non-native 32-bit integer
- [IOAF_Int8ToFloat32](3242801-ioaf_int8tofloat32.md)
- [IOAF_NativeInt16ToFloat32](1416175-ioaf_nativeint16tofloat32.md)
  Converts native 16-bit integer float to 32-bit float
- [IOAF_NativeInt24ToFloat32](1416169-ioaf_nativeint24tofloat32.md)
  Converts native 24-bit integer float to 32-bit float
- [IOAF_NativeInt32ToFloat32](1416152-ioaf_nativeint32tofloat32.md)
  Converts native 32-bit integer float to 32-bit float
- [IOAF_SwapInt16ToFloat32](1416179-ioaf_swapint16tofloat32.md)
  Converts non-native 16-bit integer float to 32-bit float
- [IOAF_SwapInt24ToFloat32](1416164-ioaf_swapint24tofloat32.md)
  Converts non-native 24-bit integer float to 32-bit float
- [IOAF_SwapInt32ToFloat32](1416183-ioaf_swapint32tofloat32.md)
  Converts non-native 32-bit integer float to 32-bit float

## See Also

- [Graphics and Displays](hardware_families/graphics_and_displays.md)
  Implement a driver that interacts with graphics and video hardware. 
- [HID](hardware_families/hid.md)
  Implement a driver that interacts with human interface devices, such as mice and keyboards.
- [Network](hardware_families/network.md)
  Implement a driver that interacts with network interfaces such as Ethernet adaptors. 
- [SCSI](hardware_families/scsi.md)
  Implement a driver that supports Small Computer System Interface (SCSI) protocols.
- [Mass Storage](hardware_families/mass_storage.md)
  Implement a driver that communicates with CD, DVD, or other mass storage devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/hardware_families/audio)*