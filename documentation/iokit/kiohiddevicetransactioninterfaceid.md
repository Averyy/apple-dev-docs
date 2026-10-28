# kIOHIDDeviceTransactionInterfaceID

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOHIDDeviceTransactionInterfaceID
```

## Discussion

This UUID constant is used to obtain a transaction interface corresponding to an IOHIDDevice service in the kernel. The type of this queue interface is IOHIDDeviceTransactionInterface. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** Please note that subsequent calls to QueryInterface with the UUID kIOHIDDeviceTransactionInterfaceID, will return a retained instance of a new IOHIDDeviceTransactionInterface.

Example:

```occ
 
 
    IOCFPluginInterface **              iodev;  // obtained earlier
 
    IOHIDDeviceTransactionInterface	**  intf;   // fetching this now
    IOReturn                            err;
 
    err = (*iodev)->QueryInterface(iodev,
                                CFUUIDGetUUIDBytes(kIOHIDDeviceTransactionInterfaceID),
                                (LPVoid)&intf);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiohiddevicetransactioninterfaceid)*