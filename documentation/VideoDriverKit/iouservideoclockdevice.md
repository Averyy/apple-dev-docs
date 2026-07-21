# IOUserVideoClockDevice

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoClockDevice;
```

#### Overview

The IOUserVideoClockDevice class is a subclass of the IOUserVideoObject class. IOUserVideoClockDevice handles the necessary configurations to be able to run IO.

## Topics

### Creating a clock device
- [Create](iouservideoclockdevice/create.md)
- [init](iouservideoclockdevice/init.md)
- [IOUserVideoDriver](iouservideodriver.md)
### Freeing a clock device
- [free](iouservideoclockdevice/free.md)
### Getting information about the class
- [GetClassID](iouservideoclockdevice/getclassid.md)
- [GetBaseClassID](iouservideoclockdevice/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
### Performing I/O
- [StartIO](iouservideoclockdevice/startio.md)
- [StopIO](iouservideoclockdevice/stopio.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
### Supporting device configuration changes
- [PerformDeviceConfigurationChange](iouservideoclockdevice/performdeviceconfigurationchange.md)
- [AbortDeviceConfigurationChange](iouservideoclockdevice/abortdeviceconfigurationchange.md)
### Supporting sample rate changes
- [HandleChangeSampleRate](iouservideoclockdevice/handlechangesamplerate.md)
### Identifying the clock device
- [GetUID](iouservideoclockdevice/getuid.md)
### Working with the clock domain
- [SetClockDomain](iouservideoclockdevice/setclockdomain.md)
- [GetClockDomain](iouservideoclockdevice/getclockdomain.md)
### Working with sample rates
- [SetSampleRate](iouservideoclockdevice/setsamplerate.md)
- [GetSampleRate](iouservideoclockdevice/getsamplerate.md)
- [SetAvailableSampleRates](iouservideoclockdevice/setavailablesamplerates.md)
- [GetAvailableSampleRates](iouservideoclockdevice/getavailablesamplerates.md)
- [GetNumberAvailableSampleRates](iouservideoclockdevice/getnumberavailablesamplerates.md)
### Working with timing and latency
- [SetOutputLatency](iouservideoclockdevice/setoutputlatency.md)
- [GetOutputLatency](iouservideoclockdevice/getoutputlatency.md)
- [SetInputLatency](iouservideoclockdevice/setinputlatency.md)
- [GetInputLatency](iouservideoclockdevice/getinputlatency.md)
### Working with clock device state
- [GetDeviceIsRunning](iouservideoclockdevice/getdeviceisrunning.md)
- [SetDeviceIsAlive](iouservideoclockdevice/setdeviceisalive.md)
- [GetDeviceIsAlive](iouservideoclockdevice/getdeviceisalive.md)
- [SetIsHidden](iouservideoclockdevice/setishidden.md)
- [GetIsHidden](iouservideoclockdevice/getishidden.md)
### Working with clock device behavior
- [SetClockAlgorithm](iouservideoclockdevice/setclockalgorithm.md)
- [GetClockAlgorithm](iouservideoclockdevice/getclockalgorithm.md)
- [IOUserVideoClockAlgorithm](videodriverkit/iouservideoclockalgorithm.md)
- [SetClockIsStable](iouservideoclockdevice/setclockisstable.md)
- [GetClockIsStable](iouservideoclockdevice/getclockisstable.md)
### Working with transport type
- [SetTransportType](iouservideoclockdevice/settransporttype.md)
- [GetTransportType](iouservideoclockdevice/gettransporttype.md)
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)
### Communicating with the host
- [RequestDeviceConfigurationChange](iouservideoclockdevice/requestdeviceconfigurationchange.md)
### Managing video controls
- [AddControl](iouservideoclockdevice/addcontrol.md)
- [RemoveControl](iouservideoclockdevice/removecontrol.md)
- [IOUserVideoControl](iouservideocontrol.md)
### Accessing timestamps
- [UpdateCurrentZeroTimestamp](iouservideoclockdevice/updatecurrentzerotimestamp.md)
- [GetCurrentZeroTimestamp](iouservideoclockdevice/getcurrentzerotimestamp.md)
### Accessing client status information
- [GetCurrentClientSampleTime](iouservideoclockdevice/getcurrentclientsampletime.md)
### Working with transport states
- [GetDeviceTransportState](iouservideoclockdevice/getdevicetransportstate.md)
- [IOUserVideoDeviceTransportState](videodriverkit/iouservideodevicetransportstate.md)
### Handling stream format changes
- [StreamFormatChanged](iouservideoclockdevice/streamformatchanged.md)

## Relationships

### Inherits From
- [IOUserVideoObject](iouservideoobject.md)
### Inherited By
- [IOUserVideoDevice](iouservideodevice.md)

## See Also

- [IOUserVideoDevice](iouservideodevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideoclockdevice)*