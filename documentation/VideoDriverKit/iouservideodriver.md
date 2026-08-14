# IOUserVideoDriver

**Framework**: VideoDriverKit  
**Kind**: class

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
class IOUserVideoDriver;
```

#### Overview

An IOUserVideoDriver is a subclass of IOService.

For the CoreVideo host to match against this IOService, keys must be added to the driver’s plist IOKitOPersonalities.

IOUserVideoDriverUserClientProperties  IOClass IOUserUserClient IOUserClass IOUserVideoDriverUserClient 

See constants in VideoDriverKitTypes.h

VideoDriverKit framework will create the IOVideoDriverUserClient when NewUserClient is called in the IOService. The driver extension must have the following entitlements: com.apple.developer.driverkit.allow-any-userclient-access

When the state of an IOUserVideoObject implemented by the driver changes, it notifies the host to update its state. For changes to an IOUserVideoDevice’s or IOUserVideoClockDevice’s state that will affect IO or its structure, the client should  trigger a request to the host using RequestDeviceConfigurationChange(), so the host it has an oppurtunity to stop any outstanding  IO and otherwise return the device to its ground state. The host will inform the driver that it is safe to make the change by calling PerformDeviceConfigurationChange() on the object. It is only at this point that the device can make the state change. When PerformDeviceConfigurationChange() returns, the host will figure out what changed and restart any outstanding IO.

The host is in control of IO. It tells the drivers’s IOUserVideoDevice when to start and when to stop the hardware. The host drives its timing using the timestamps provided by the IOUserVideoClockDevice’s implementation of UpdateCurrentZeroTimestamp() and GetCurrentZeroTimestamp(). The series of timestamps provides a mapping between the device’s sample time and mach_absolute_time().

## Topics

### Running the driver service
- [init](iouservideodriver/init.md)
- [Start](iouservideodriver/start.md)
- [Stop](iouservideodriver/stop.md)
- [free](iouservideodriver/free.md)
### Getting information about the class
- [GetClassID](iouservideodriver/getclassid.md)
- [GetBaseClassID](iouservideodriver/getbaseclassid.md)
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
- [GetWorkQueue](iouservideodriver/getworkqueue.md)
- [GetName](iouservideodriver/getname.md)
- [SetName](iouservideodriver/setname.md)
### Getting the driver’s video object identifier
- [kIOUserVideoObjectIDDriver](videodriverkit/kiouservideoobjectiddriver.md)
### Starting and stopping the driver
- [StartDevice](iouservideodriver/startdevice.md)
- [StopDevice](iouservideodriver/stopdevice.md)
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
### Creating a new client
- [NewUserClient](iouservideodriver/newuserclient.md)
### Working with transport types
- [GetTransportType](iouservideodriver/gettransporttype.md)
- [SetTransportType](iouservideodriver/settransporttype.md)
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)
### Working with video objects
- [AddObject](iouservideodriver/addobject.md)
- [RemoveObject](iouservideodriver/removeobject.md)
- [IOUserVideoObject](iouservideoobject.md)
- [GetVideoObjectForObjectID](iouservideodriver/getvideoobjectforobjectid.md)
### Communicating with the host
- [PropertiesChanged](iouservideodriver/propertieschanged.md)
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
- [IOUserVideoObjectPropertySelector](videodriverkit/iouservideoobjectpropertyselector.md)
### Working with custom properties
- [AddCustomProperty](iouservideodriver/addcustomproperty.md)
- [RemoveCustomProperty](iouservideodriver/removecustomproperty.md)
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
### Working with buffers
- [OutputBufferNotification](iouservideodriver/outputbuffernotification.md)
- [BufferQueueChange](iouservideodriver/bufferqueuechange.md)

## Relationships

### Inherits From
- [IOService](../driverkit/ioservice.md)

## See Also

- [IOUserVideoObject](iouservideoobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver)*