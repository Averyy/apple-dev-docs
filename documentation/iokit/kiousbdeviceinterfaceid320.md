# kIOUSBDeviceInterfaceID320

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOUSBDeviceInterfaceID320
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBDevice user client in the kernel. The type of this device interface is IOUSBDeviceInterface320. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBDeviceInterface320 is returned only by version 3.2.0 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.5.4 If your software is running on an earlier version of macOS you will need to use UUID kIOUSBDeviceInterfaceID, kIOUSBDeviceInterfaceID182, kIOUSBDeviceInterfaceID187, kIOUSBDeviceInterfaceID197, kIOUSBDeviceInterfaceID245, or kIOUSBDeviceInterfaceID300 and you will not have access to some functions.

Example:

```occ
 
 
 IOCFPluginInterface		**iodev; 	// obtained earlier
 
 IOUSBDeviceInterface320	**dev;		// fetching this now
 IOReturn                    err;
 
 err = (*iodev)->QueryInterface(iodev,
 CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID320),
 (LPVoid)&dev);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbdeviceinterfaceid320)*