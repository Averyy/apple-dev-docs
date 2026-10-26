# kIOHIDDeviceDeviceInterfaceID

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOHIDDeviceDeviceInterfaceID
```

#### Discussion

This UUID constant is used to obtain a device interface corresponding to an IOHIDDevice service in the kernel. The type of this device interface is IOHIDDeviceDeviceInterface. This device interface is obtained after the IOCFPlugInInterface for the service itself has been obtained.

**Note:** Please note that subsequent calls to QueryInterface with the UUID kIOHIDDeviceTransactionInterfaceID, will return a retained instance of an existing IOHIDDeviceTransactionInterface.

Example:

```occ
 
 
    IOCFPluginInterface **          iodev;  // obtained earlier
 
    IOHIDDeviceDeviceInterface **   dev;    // fetching this now
    IOReturn                        err;
 
    err = (*iodev)->QueryInterface(iodev,
                                    CFUUIDGetUUIDBytes(kIOHIDDeviceDeviceInterfaceID),
                                    (LPVoid)&dev);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiohiddevicedeviceinterfaceid)*