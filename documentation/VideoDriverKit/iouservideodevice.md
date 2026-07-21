# IOUserVideoDevice

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoDevice;
```

#### Overview

The IOUserVideoDevice class is a subclass of the IOUserVideoClockDevice class. The device has IOUserVideoDeviceStreams.

## Topics

### Creating a video device
- [Create](iouservideodevice/create.md)
- [init](iouservideodevice/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
### Freeing a video device
- [free](iouservideodevice/free.md)
### Getting information about the class
- [GetClassID](iouservideodevice/getclassid.md)
- [GetBaseClassID](iouservideodevice/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Performing I/O
- [StartIO](iouservideodevice/startio.md)
- [StopIO](iouservideodevice/stopio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
### Supporting device configuration changes
- [PerformDeviceConfigurationChange](iouservideodevice/performdeviceconfigurationchange.md)
- [AbortDeviceConfigurationChange](iouservideodevice/abortdeviceconfigurationchange.md)
### Supporting sample rate changes
- [HandleChangeSampleRate](iouservideodevice/handlechangesamplerate.md)
### Supporting stream format changes
- [StreamFormatChanged](iouservideodevice/streamformatchanged.md)
### Working with video streams
- [AddStream](iouservideodevice/addstream.md)
- [RemoveStream](iouservideodevice/removestream.md)
- [IOUserVideoStream](iouservideostream.md)
### Working with default device behavior
- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
- [CanBeDefaultInputDevice](iouservideodevice/canbedefaultinputdevice.md)
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
- [CanBeDefaultOutputDevice](iouservideodevice/canbedefaultoutputdevice.md)
- [SetCanBeDefaultSystemOutputDevice](iouservideodevice/setcanbedefaultsystemoutputdevice.md)
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)
### Working with safety offset behavior
- [SetInputSafetyOffset](iouservideodevice/setinputsafetyoffset.md)
- [GetInputSafetyOffset](iouservideodevice/getinputsafetyoffset.md)
- [SetOutputSafetyOffset](iouservideodevice/setoutputsafetyoffset.md)
- [GetOutputSafetyOffset](iouservideodevice/getoutputsafetyoffset.md)
### Working with channel layouts
- [SetPreferredChannelsForStereo](iouservideodevice/setpreferredchannelsforstereo.md)
- [GetPreferredChannelsForStereo](iouservideodevice/getpreferredchannelsforstereo.md)
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
- [SetPreferredOutputChannelLayout](iouservideodevice/setpreferredoutputchannellayout.md)
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)
### Working with controls
- [SetControlValue](iouservideodevice/setcontrolvalue.md)

## Relationships

### Inherits From
- [IOUserVideoClockDevice](iouservideoclockdevice.md)

## See Also

- [IOUserVideoClockDevice](iouservideoclockdevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice)*