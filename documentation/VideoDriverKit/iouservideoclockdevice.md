# IOUserVideoClockDevice

**Framework**: VideoDriverKit  
**Kind**: class

A clock device.

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoClockDevice;
```

#### Overview

[`IOUserVideoClockDevice`](iouservideoclockdevice.md) handles the necessary configurations to be able to run IO.

## Topics

### Creating a clock device
- [Create](iouservideoclockdevice/create.md)
  A static factory method that allocates and initializes a video clock device.
- [init](iouservideoclockdevice/init.md)
  Initializes a video clock device.
- [IOUserVideoDriver](iouservideodriver.md)
  A video driver.
### Freeing a clock device
- [free](iouservideoclockdevice/free.md)
  Frees the video clock device.
### Getting information about the class
- [GetClassID](iouservideoclockdevice/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideoclockdevice/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
### Performing I/O
- [StartIO](iouservideoclockdevice/startio.md)
  Tells the clock device to start IO.
- [StopIO](iouservideoclockdevice/stopio.md)
  Tells the clock device to stop IO.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
### Supporting device configuration changes
- [PerformDeviceConfigurationChange](iouservideoclockdevice/performdeviceconfigurationchange.md)
  The host calls this method to allow the clock device to perform a configuration change that had been previously requested via a call to the host via RequestDeviceConfigChange or a change to an IO state that requires a configuration change
- [AbortDeviceConfigurationChange](iouservideoclockdevice/abortdeviceconfigurationchange.md)
  The host calls this method to tell the driver not to perform a configuration change that had been requested via a call to the Host method, RequestDeviceConfigurationChange().
### Supporting sample rate changes
- [HandleChangeSampleRate](iouservideoclockdevice/handlechangesamplerate.md)
  The system calls this virtual method when the clock device’s sample rate changes.
### Identifying the clock device
- [GetUID](iouservideoclockdevice/getuid.md)
  Gets the unique identifier of the clock device.
### Working with the clock domain
- [SetClockDomain](iouservideoclockdevice/setclockdomain.md)
  Sets the clock domain value of the clock device.
- [GetClockDomain](iouservideoclockdevice/getclockdomain.md)
  Gets the clock domain value of the clock device.
### Working with sample rates
- [SetSampleRate](iouservideoclockdevice/setsamplerate.md)
  Sets the current sample rate for the clock device.
- [GetSampleRate](iouservideoclockdevice/getsamplerate.md)
  Gets sample rate of the clock device.
- [SetAvailableSampleRates](iouservideoclockdevice/setavailablesamplerates.md)
  Sets the available sample rates for the clock device.
- [GetAvailableSampleRates](iouservideoclockdevice/getavailablesamplerates.md)
  Gets available sample rates of the clock device.
- [GetNumberAvailableSampleRates](iouservideoclockdevice/getnumberavailablesamplerates.md)
  Gets number of available sample rates of the clock device.
### Working with timing and latency
- [SetOutputLatency](iouservideoclockdevice/setoutputlatency.md)
  Sets the output latency of the clock device.
- [GetOutputLatency](iouservideoclockdevice/getoutputlatency.md)
  Gets the output latency of the clock device.
- [SetInputLatency](iouservideoclockdevice/setinputlatency.md)
  Sets the input latency of the clock device.
- [GetInputLatency](iouservideoclockdevice/getinputlatency.md)
  Gets the input latency of the clock device.
### Working with clock device state
- [GetDeviceIsRunning](iouservideoclockdevice/getdeviceisrunning.md)
  Gets bool value indicating if device is running.
- [SetDeviceIsAlive](iouservideoclockdevice/setdeviceisalive.md)
  Sets a Boolean value to indicate the device is alive.
- [GetDeviceIsAlive](iouservideoclockdevice/getdeviceisalive.md)
  Gets a Boolean value indicating if the device is alive.
- [SetIsHidden](iouservideoclockdevice/setishidden.md)
  Sets a Boolean value indicating if the device is hidden.
- [GetIsHidden](iouservideoclockdevice/getishidden.md)
  Gets a Boolean value indicating if the device is hidden.
### Working with clock device behavior
- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
  Sets the algorithm for the video clock device.
- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
  Gets the clock algorithm of the clock device.
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
  Clock smoothing algorithm selectors.
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
  Sets the clock stability of the clock device.
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)
  Gets a Boolean value for clock stability of the clock device.
### Working with transport type
- [SetTransportType](iouservideoclockdevice/settransporttype.md)
  Sets the transport type of the clock device.
- [GetTransportType](iouservideoclockdevice/gettransporttype.md)
  Gets the transport type of the IOUserVideoClockDevice.
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)
  The transport type of a video stream.
### Communicating with the host
- [RequestDeviceConfigurationChange](iouservideoclockdevice/requestdeviceconfigurationchange.md)
  Tells the host to initiate a configuration change operation.
### Managing video controls
- [AddControl](iouservideoclockdevice/addcontrol.md)
  Adds a video control to the video clock device.
- [RemoveControl](iouservideoclockdevice/removecontrol.md)
  Removes a user video control from the video clock device.
- [IOUserVideoControl](iouservideocontrol.md)
  A base class for control objects.
### Accessing timestamps
- [UpdateCurrentZeroTimestamp](iouservideoclockdevice/updatecurrentzerotimestamp.md)
  Update the current timestamp value.
- [GetCurrentZeroTimestamp](iouservideoclockdevice/getcurrentzerotimestamp.md)
  Gets the current zero timestamp value.
### Accessing client status information
- [GetCurrentClientSampleTime](iouservideoclockdevice/getcurrentclientsampletime.md)
  Gets the current sample time in the ring buffer that the client reads from and writes to.
### Working with transport states
- [GetDeviceTransportState](iouservideoclockdevice/getdevicetransportstate.md)
  Gets the transport state of the device.
- [IOUserVideoDeviceTransportState](videodriverkit/iouservideodevicetransportstate.md)
  The current transport state of the device.
### Handling stream format changes
- [StreamFormatChanged](iouservideoclockdevice/streamformatchanged.md)

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)
### Inherited By
- [IOUserVideoDevice](iouservideodevice.md)

## See Also

- [IOUserVideoDevice](iouservideodevice.md)
  A video device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice)*