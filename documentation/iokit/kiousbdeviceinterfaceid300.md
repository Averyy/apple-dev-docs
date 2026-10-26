# kIOUSBDeviceInterfaceID300

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOUSBDeviceInterfaceID300
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBDevice user client in the kernel. The type of this device interface is IOUSBDeviceInterface300. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBDeviceInterface300 is returned only by version 3.0.0 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.5. If your software is running on an earlier version of macOS you will need to use UUID kIOUSBDeviceInterfaceID, kIOUSBDeviceInterfaceID182, kIOUSBDeviceInterfaceID187, kIOUSBDeviceInterfaceID197, or kIOUSBDeviceInterfaceID245 and you will not have access to some functions.

Example:

```occ
 
 
 IOCFPluginInterface		**iodev; 	// obtained earlier
 
 IOUSBDeviceInterface300	**dev;		// fetching this now
 IOReturn                    err;
 
 err = (*iodev)->QueryInterface(iodev,
 CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID300),
 (LPVoid)&dev);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbdeviceinterfaceid300)*