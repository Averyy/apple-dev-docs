# kIOUSBInterfaceInterfaceID192

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOUSBInterfaceInterfaceID192
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBInterface user client in the kernel. The type of this device interface is IOUSBInterfaceInterface192. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBInterfaceInterface192 is returned only by version 1.9.2 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.2.3. If your software is running on a version of macOS prior to 10.2.3 you will need to use the UUID kIOUSBInterfaceInterfaceID, kIOUSBInterfaceInterfaceID182, kIOUSBInterfaceInterfaceID183, or kIOUSBInterfaceInterfaceID190 and you will not have access to some functions.

Example:

```occ
 
 
    IOCFPluginInterface             **iodev; 	// obtained earlier
 
    IOUSBInterfaceInterface192      **intf;     // fetching this now
    IOReturn                        err;
 
    err = (*iodev)->QueryInterface(iodev,
                                CFUUIDGetUUIDBytes(kIOUSBInterfaceInterfaceID192),
                                (LPVoid)&intf);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbinterfaceinterfaceid192)*