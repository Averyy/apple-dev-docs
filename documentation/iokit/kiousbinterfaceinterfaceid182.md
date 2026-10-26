# kIOUSBInterfaceInterfaceID182

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
#define kIOUSBInterfaceInterfaceID182
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBInterface user client in the kernel. The type of this device interface is IOUSBInterfaceInterface182. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBInterfaceInterface182 is returned only by version 1.8.2 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.0.4. If your software is running on an earlier version of macOS, you will need to use the UUID kIOUSBInterfaceInterfaceID and you will not have access to some functions.

Example:

```occ
 
 
    IOCFPluginInterface         **iodev; 	// obtained earlier
 
    IOUSBInterfaceInterface182	**intf;		// fetching this now
    IOReturn                    err;
 
    err = (*iodev)->QueryInterface(iodev,
                                CFUUIDGetUUIDBytes(kIOUSBInterfaceInterfaceID182),
                                (LPVoid)&intf);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbinterfaceinterfaceid182)*