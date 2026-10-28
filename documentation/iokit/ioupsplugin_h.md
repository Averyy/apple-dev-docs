# IOUPSPlugIn.h

**Framework**: IOKit  
**Role**: API Collection

## Overview

IOUPSPlugIn.h is the header that defines the software used by ioupsd in user-space to communicate with UPS devices.

 **NOTE:** Kernel extensions should have the following key/value pair in their personality in order to be recognized by ioupsd:

```occ
 
        <key>UPSDevice<key>
        <true/>
 
```

To communicate with a UPS device, an instance of IOUPSPlugInInterface (a struct which is defined below) is created. The methods of IOUPSPlugInInterface allow ioupsd to communicate with the device.

To obtain an IOUPSPlugInInterface for a UPS device, use the function IOCreatePlugInInterfaceForService() defined in IOKit/IOCFPlugIn.h. (Note the "i" in "PlugIn" is always upper-case.) Quick usage reference:

- 'service' is a reference to the IOKit registry entry of the kernel object (usually of type IOHIDDevice) representing the device of interest. This reference can be obtained using the functions defined in IOKit/IOKitLib.h.
- 'plugInType' should be CFUUIDGetUUIDBytes(kIOCFPlugInInterfaceID)
- 'interfaceType' should be CFUUIDGetUUIDBytes(kIOUPSPlugInTypeID) when using IOUPSPlugIn

The interface returned by IOCreatePlugInInterfaceForService() should be deallocated using IODestroyPlugInInterface(). Do not call Release() on it.

### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <IOKit/IOCFPlugIn.h>

## Topics

### Callbacks
- [IOUPSEventCallbackFunction](./ioupseventcallbackfunction.md)
### Constants
- [Defines](./ioupsplugin_h/defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioupsplugin_h)*