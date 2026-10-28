# kIOUSBInterfaceInterfaceID500

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```c
#define kIOUSBInterfaceInterfaceID500
```

## Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBInterface user client in the kernel. The type of this device interface is IOUSBInterfaceInterface500. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBInterfaceInterface500 is returned only by version 5.0.0 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.7.3. If your software is running on a version of macOS prior to 10.7.3 you will need to use the UUID kIOUSBInterfaceInterfaceID, kIOUSBInterfaceInterfaceID182, kIOUSBInterfaceInterfaceID183, kIOUSBInterfaceInterfaceID190, kIOUSBInterfaceInterfaceID192, kIOUSBInterfaceInterfaceID197, kIOUSBInterfaceInterfaceID220, kIOUSBInterfaceInterfaceID245, or kIOUSBInterfaceInterfaceID300 and you will not have access to some functions.

Example:

```occ
 
 
 IOCFPluginInterface             **iodev; 	// obtained earlier
 
 IOUSBInterfaceInterface500      **intf;     // fetching this now
 IOReturn                        err;
 
 err = (*iodev)->QueryInterface(iodev,
 CFUUIDGetUUIDBytes(kIOUSBInterfaceInterfaceID500),
 (LPVoid)&intf);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbinterfaceinterfaceid500)*