# IOVideoDeviceLib.h User-Space

**Framework**: IOKit  
**Role**: API Collection

## Overview

### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <IOKit/IOKitLib.h>
- <IOKit/IOCFPlugIn.h>
- <IOKit/stream/IOStreamLib.h>
- <IOKit/stream/IOStreamShared.h>
- <IOKit/video/IOVideoDeviceShared.h>
- <IOKit/video/IOVideoTypes.h>

## Topics

### Opening and closing VideoDevices
- [AddToRunLoop](./iostreamlib_h/api-1809610-addtorunloop.md)
  Add the CFRunLoopSource for the notification port to a run loop.
- [Close](./iostreamlib_h/api-1809625-close.md)
  Closes an IOStream.
- [CreateStreamInterface](./iovideodevicelib_h_user-space/api-1809640-createstreaminterface.md)
- [GetNotificationPort](./iovideodevicelib_h_user-space/api-1809655-getnotificationport.md)
  Get the notification port for device state changes sent to user space.
- [GetRunLoopSource](./iostreamlib_h/api-1809678-getrunloopsource.md)
  Gets a CFRunLoopSource for the CFMachPort used for notifications from the kernel that data is ready.
- [Open](./iostreamlib_h/api-1809697-open.md)
  Open an IOStream from user space.
- [ReleaseStreamInterface](./iovideodevicelib_h_user-space/api-1809719-releasestreaminterface.md)
- [RemoveFromRunLoop](./iostreamlib_h/api-1809745-removefromrunloop.md)
  Remove the CFRunLoopSource for the notification port from a run loop.
- [SetNotificationCallback](./iovideodevicelib_h_user-space/api-1809779-setnotificationcallback.md)
  Set the callback function to be called when certain device state changes happen.
- [SetStreamFormat](./iovideodevicelib_h_user-space/api-1809797-setstreamformat.md)
### Callbacks
- [IOVideoDeviceNotificationCallback](./iovideodevicenotificationcallback.md)
- [IOVideoDeviceOutputCallback](./iovideodeviceoutputcallback.md)
### Data Types
- [IOVideoDeviceInterface_v1_t](./iovideodeviceinterface_v1_t.md)
  Forward declaration of IOVideoDeviceInterface_v1_t.
- [IOVideoDeviceRef](./iovideodeviceref.md)
### Constants
- [Defines](./iovideodevicelib_h_user-space/defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iovideodevicelib_h_user-space)*