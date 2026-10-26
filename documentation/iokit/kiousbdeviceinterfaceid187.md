# kIOUSBDeviceInterfaceID187

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
#define kIOUSBDeviceInterfaceID187
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBDevice user client in the kernel. The type of this device interface is IOUSBDeviceInterface187. This device interface is obtained after the device interface for the service itself has been obtained (see [`kIOUSBDeviceUserClientTypeID`](./kiousbdeviceuserclienttypeid.md) ).

**Note:** The IOUSBDeviceInterface187 is returned only by version 1.8.7 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.1.2. If your software is running on an earlier version of macOS you will need to use UUID kIOUSBDeviceInterfaceID or kIOUSBDeviceInterfaceID182 and you will not have access to some functions.

Example:

```occ
 
 
    IOCFPluginInterface		**iodev; 	// obtained earlier
 
    IOUSBDeviceInterface187	**dev;		// fetching this now
    IOReturn                    err;
 
    err = (*iodev)->QueryInterface(iodev,
                                CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID187),
                                (LPVoid)&dev);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbdeviceinterfaceid187)*