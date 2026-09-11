# IOUserVideoDriver

**Framework**: VideoDriverKit  
**Kind**: class

A video driver.

**Availability**:
- DriverKit 27.0+

## Declaration

```swift
class IOUserVideoDriver;
```

#### Overview

For the CoreVideo host to match against this `IOService`, keys must be added to the driver’s plist `IOKitOPersonalities`.

```None
<key>IOUserVideoDriverUserClientProperties</key>
<dict>
	<key>IOClass</key>
	<string>IOUserUserClient</string>
	<key>IOUserClass</key>
	<string>IOUserVideoDriverUserClient</string>
</dict>
```

See constants in `VideoDriverKitTypes.h`.

The VideoDriverKit framework will create the `IOVideoDriverUserClient` when `NewUserClient` is called in the `IOService`. The driver extension must have the `com.apple.developer.driverkit.allow-any-userclient-access` entitlement.

When the state of an `IOUserVideoObject` implemented by the driver changes, it notifies the host to update its state. For changes to an [`IOUserVideoDevice`](iouservideodevice.md) or [`IOUserVideoClockDevice`](iouservideoclockdevice.md) state that will affect IO or its structure, the client should  trigger a request to the host using `RequestDeviceConfigurationChange()`, so the host it has an oppurtunity to stop any outstanding  IO and otherwise return the device to its ground state. The host will inform the driver that it is safe to make the change by calling `PerformDeviceConfigurationChange()` on the object. It is only at this point that the device can make the state change. When `PerformDeviceConfigurationChange()` returns, the host will figure out what changed and restart any outstanding IO.

The host is in control of IO. It tells the drivers’s [`IOUserVideoDevice`](iouservideodevice.md) when to start and when to stop the hardware. The host drives its timing using the timestamps provided by the [`IOUserVideoClockDevice`](iouservideoclockdevice.md) implementation of `UpdateCurrentZeroTimestamp()` and `GetCurrentZeroTimestamp()`. The series of timestamps provides a mapping between the device's sample time and `mach_absolute_time()``.

## Topics

### Running the driver service
- [init](iouservideodriver/init.md)
- [Start](iouservideodriver/start.md)
- [Stop](iouservideodriver/stop.md)
- [free](iouservideodriver/free.md)
### Getting information about the class
- [GetClassID](iouservideodriver/getclassid.md)
  Gets the class identifier of the object.
- [GetBaseClassID](iouservideodriver/getbaseclassid.md)
  Gets the class identifier of the base class object.
- [IOUserVideoClassID](videodriverkit/iouservideoclassid.md)
  Video class identifiers of an video object.
- [GetWorkQueue](iouservideodriver/getworkqueue.md)
  Gets the work queue created by the video object.
- [GetName](iouservideodriver/getname.md)
  Gets the name of the driver.
- [SetName](iouservideodriver/setname.md)
  Sets the name of the video driver.
### Getting the driver’s video object identifier
- [kIOUserVideoObjectIDDriver](videodriverkit/kiouservideoobjectiddriver.md)
  The video object identifier of the driver.
### Starting and stopping the driver
- [StartDevice](iouservideodriver/startdevice.md)
  Tells the driver to start IO on an video device.
- [StopDevice](iouservideodriver/stopdevice.md)
  Tells the driver to stop IO on an video device.
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
  A handle for a a specific video object.
- [IOUserVideoStartStopFlags](videodriverkit/iouservideostartstopflags.md)
  Flags used to indicate how I/O is starting or stopping.
### Creating a new client
- [NewUserClient](iouservideodriver/newuserclient.md)
### Working with transport types
- [GetTransportType](iouservideodriver/gettransporttype.md)
  Gets the transport type of the driver.
- [SetTransportType](iouservideodriver/settransporttype.md)
  Sets the transport type of the video driver.
- [IOUserVideoTransportType](videodriverkit/iouservideotransporttype.md)
  The transport type of a video stream.
### Working with video objects
- [AddObject](iouservideodriver/addobject.md)
  Adds a video object to the driver.
- [RemoveObject](iouservideodriver/removeobject.md)
  Removes a video object from the driver.
- [IOUserVideoObject](iouservideoobject.md)
  The base class for all video objects.
- [GetVideoObjectForObjectID](iouservideodriver/getvideoobjectforobjectid.md)
  Gets the video object that corresponds to a video object identifier.
### Communicating with the host
- [PropertiesChanged](iouservideodriver/propertieschanged.md)
  This method informs the host when the state of an driver’s object changes.
- [IOUserVideoObjectID](videodriverkit/iouservideoobjectid.md)
  A handle for a a specific video object.
- [IOUserVideoObjectPropertySelector](videodriverkit/iouservideoobjectpropertyselector.md)
  A four character code which, along with the scope and element, specifies a specific piece of information about a video object.
### Working with custom properties
- [AddCustomProperty](iouservideodriver/addcustomproperty.md)
  Adds a custom property object to the video driver.
- [RemoveCustomProperty](iouservideodriver/removecustomproperty.md)
  Removes a custom property object from the video driver.
- [IOUserVideoCustomProperty](iouservideocustomproperty.md)
  A custom property object that can be added to or associated with video objects.
### Working with buffers
- [OutputBufferNotification](iouservideodriver/outputbuffernotification.md)
- [BufferQueueChange](iouservideodriver/bufferqueuechange.md)

## Relationships

### Inherits From
- [IOService](../driverkit/ioservice.md)

## See Also

- [IOUserVideoObject](iouservideoobject.md)
  The base class for all video objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/iouservideodriver)*