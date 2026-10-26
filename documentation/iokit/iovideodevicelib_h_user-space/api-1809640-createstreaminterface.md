# CreateStreamInterface

**Framework**: IOKit  
**Kind**: func

## Declaration

```c
IOReturn ( *CreateStreamInterface)(
   IOVideoDeviceRef device,
   CFDictionaryRef streamDictionary,
   UInt32 streamIndex,
   bool isInput,
   IOStreamRef *streamRef);
```

#### Return Value

Returns kIOReturnSuccess if the stream was successfully stopped from the run loop.

## Parameters

- `device`: The IOVideoDeviceRef of the device to operate on.
- `streamDictionary`: 
- `streamIndex`: The index of the stream that you want to stop.
- `isInput`: 

## See Also

### Opening and closing VideoDevices
- [AddToRunLoop](../iostreamlib_h/api-1809610-addtorunloop.md)
  Add the CFRunLoopSource for the notification port to a run loop.
- [Close](../iostreamlib_h/api-1809625-close.md)
  Closes an IOStream.
- [GetNotificationPort](./api-1809655-getnotificationport.md)
  Get the notification port for device state changes sent to user space.
- [GetRunLoopSource](../iostreamlib_h/api-1809678-getrunloopsource.md)
  Gets a CFRunLoopSource for the CFMachPort used for notifications from the kernel that data is ready.
- [Open](../iostreamlib_h/api-1809697-open.md)
  Open an IOStream from user space.
- [ReleaseStreamInterface](./api-1809719-releasestreaminterface.md)
- [RemoveFromRunLoop](../iostreamlib_h/api-1809745-removefromrunloop.md)
  Remove the CFRunLoopSource for the notification port from a run loop.
- [SetNotificationCallback](./api-1809779-setnotificationcallback.md)
  Set the callback function to be called when certain device state changes happen.
- [SetStreamFormat](./api-1809797-setstreamformat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideodevicelib_h_user-space/1809640-createstreaminterface)*