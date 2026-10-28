# kIOUSBDeviceInterfaceID182

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
#define kIOUSBDeviceInterfaceID182
```

## Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBDevice user client in the kernel. The type of this device interface is IOUSBDeviceInterface182. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBDeviceInterface182 is returned only by version 1.8.2 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.0.4. If your software is running on an earlier version of macOS, you will need to use the UUID kIOUSBDeviceInterfaceID and you will not have access to some functions.

Example:

```occ
 
 
    IOCFPluginInterface		**iodev; 	// obtained earlier
 
    IOUSBDeviceInterface182	**dev;		// fetching this now
    IOReturn                    err;
 
    err = (*iodev)->QueryInterface(iodev,
                                CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID182),
                                (LPVoid)&dev);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbdeviceinterfaceid182)*