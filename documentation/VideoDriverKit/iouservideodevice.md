# IOUserVideoDevice

**Framework**: VideoDriverKit  
**Kind**: class

A video device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoDevice;
```

#### Overview

The device has `IOUserVideoDeviceStream` objects.

## Topics

### Creating a video device
- [Create](iouservideodevice/create.md)
  A static factory method that allocates and initializes a video device.
- [init](iouservideodevice/init.md)
  Initializes a video device.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
### Freeing a video device
- [free](iouservideodevice/free.md)
  Frees the IOUserVideoDevice.
### Getting information about the class
- [GetClassID](iouservideodevice/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideodevice/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Performing I/O
- [StartIO](iouservideodevice/startio.md)
  Tells the device to start IO.
- [StopIO](iouservideodevice/stopio.md)
  Tells the device to stop IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
- [GetCurrentClientIOTime](iouservideodevice/getcurrentclientiotime.md)
  Gets the current sample/host time pair in the ring buffer written to or read from by the client
- [SetIOOperationHandler](iouservideodevice/setiooperationhandler.md)
  Sets the IOOperationHandler block on the device.
- [IOOperationHandler](videodriverkit/iooperationhandler.md)
  A block that tells the device to perform an IOUserVideoIOOperation.
### Supporting device configuration changes
- [PerformDeviceConfigurationChange](iouservideodevice/performdeviceconfigurationchange.md)
  The host calls this method to allow the device to perform a configuration change it previously requested by calling RequestDeviceConfigurationChange(), or a change to an IO state that requires a configuration change.
- [AbortDeviceConfigurationChange](iouservideodevice/abortdeviceconfigurationchange.md)
  The host calls this method to tell the driver not to perform a configuration change it requested by calling RequestDeviceConfigurationChange(). Subclass and override this method to handle any aborted custom configuration change requests. Then call the superclass implementation to update state.
### Supporting sample rate changes
- [HandleChangeSampleRate](iouservideodevice/handlechangesamplerate.md)
  The system calls this virtual method when the device’s sample rate changes.
### Supporting stream format changes
- [StreamFormatChanged](iouservideodevice/streamformatchanged.md)
### Working with video streams
- [AddStream](iouservideodevice/addstream.md)
  Adds an video stream to the device.
- [RemoveStream](iouservideodevice/removestream.md)
  Removes a video stream from the device.
- [IOUserVideoStream](iouservideostream.md)
  A video stream.
### Working with default device behavior
- [SetCanBeDefaultInputDevice](iouservideodevice/setcanbedefaultinputdevice.md)
  Specify if device can be used as default input device.
- [CanBeDefaultInputDevice](iouservideodevice/canbedefaultinputdevice.md)
  Returns a Boolean value indicating if device can be used for default input.
- [SetCanBeDefaultOutputDevice](iouservideodevice/setcanbedefaultoutputdevice.md)
  Specifies if device can be used as default output device.
- [CanBeDefaultOutputDevice](iouservideodevice/canbedefaultoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default output.
- [SetCanBeDefaultSystemOutputDevice](iouservideodevice/setcanbedefaultsystemoutputdevice.md)
  Specifies if device can be used as default system output device
- [CanBeDefaultSystemOutputDevice](iouservideodevice/canbedefaultsystemoutputdevice.md)
  Returns a Boolean value indicating if device can be used for default system output.
### Working with safety offset behavior
- [SetInputSafetyOffset](iouservideodevice/setinputsafetyoffset.md)
  Specifies the input safety offset of the device.
- [GetInputSafetyOffset](iouservideodevice/getinputsafetyoffset.md)
  Gets the input safety offset of the device.
- [SetOutputSafetyOffset](iouservideodevice/setoutputsafetyoffset.md)
  Specifies the output safety offset of the device.
- [GetOutputSafetyOffset](iouservideodevice/getoutputsafetyoffset.md)
  Gets the output safety offset of the device.
### Working with channel layouts
- [SetPreferredChannelsForStereo](iouservideodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the preferred stereo pair
- [GetPreferredChannelsForStereo](iouservideodevice/getpreferredchannelsforstereo.md)
  Gets the channel indices for the preferred stereo pair.
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout with IOUserVideoChannelLabel values
- [SetPreferredOutputChannelLayout](iouservideodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout.
- [IOUserVideoChannelLabel](videodriverkit/iouservideochannellabel.md)
  These constants are to set the preferred channel layout on video device.
### Working with controls
- [SetControlValue](iouservideodevice/setcontrolvalue.md)

## Relationships

### Inherits From
- [IOUserVideoClockDevice](iouservideoclockdevice.md)

## See Also

- [IOUserVideoClockDevice](iouservideoclockdevice.md)
  A clock device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodevice)*