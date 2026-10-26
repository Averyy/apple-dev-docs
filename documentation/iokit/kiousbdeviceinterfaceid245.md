# kIOUSBDeviceInterfaceID245

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
#define kIOUSBDeviceInterfaceID245
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBDevice user client in the kernel. The type of this device interface is IOUSBDeviceInterface245. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBDeviceInterface245 is returned only by version 2.4.5 or above of the IOUSBFamily. This version of IOUSBFamily shipped with OS X version 10.4.5 (for Intel). This version does not add any more functions to the interface. It is used to allow us to fix an overrelease in our termination without affecting any current drivers: In previous versions, we would end up releasing our IOService, even though we had not retained it. For IOUSBDeviceInterfaceID245 clients we will retain the IOService.

Example:

```occ
 
 
 IOCFPluginInterface		**iodev; 	// obtained earlier
 
 IOUSBDeviceInterface245	**dev;		// fetching this now
 IOReturn                    err;
 
 err = (*iodev)->QueryInterface(iodev,
                                CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID245),
                                (LPVoid)&dev);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbdeviceinterfaceid245)*