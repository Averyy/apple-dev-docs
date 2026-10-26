# kIOUSBDeviceInterfaceID

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define kIOUSBDeviceInterfaceID
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOUSBDevice user client in the kernel. The type of this device interface is IOUSBDeviceInterface. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** The IOUSBDeviceInterface is returned by all versions of the IOUSBFamily currently shipping. However, there are some functions that are available only in IOUSBFamily version 1.8.2 and above. Access to these functions, in addition to the functions contained in IOUSBDeviceInterface, can be obtained by using one of the other UUIDs listed in this header.

Example:

```occ
 
 
    IOCFPluginInterface		**iodev; 	// obtained earlier
 
    IOUSBDeviceInterface	**dev;		// fetching this now
    IOReturn                    err;
 
    err = (*iodev)->QueryInterface(iodev,
                                    CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID),
                                    (LPVoid)&dev);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiousbdeviceinterfaceid)*