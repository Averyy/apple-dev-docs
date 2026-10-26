# kIOUSBInterfaceInterfaceID245

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
#define kIOUSBInterfaceInterfaceID245
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBInterface user client in the kernel. The type of this device interface is IOUSBInterfaceInterface245. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBInterfaceInterface245 is returned only by version 2.4.5 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.4.5. This version does not add any new functions. It is used to allow us to fix a leak in our termination without affecting any current drivers: In previous versions, we would not release a reference to the IOUSBDevice. For IOUSBInterfaceInterfaceID245 clients we will now release that reference.

Example:

```occ
 
 
 IOCFPluginInterface             **iodev; 	// obtained earlier
 
 IOUSBInterfaceInterface245      **intf;     // fetching this now
 IOReturn                        err;
 
 err = (*iodev)->QueryInterface(iodev,
                                CFUUIDGetUUIDBytes(kIOUSBInterfaceInterfaceID245),
                                (LPVoid)&intf);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbinterfaceinterfaceid245)*