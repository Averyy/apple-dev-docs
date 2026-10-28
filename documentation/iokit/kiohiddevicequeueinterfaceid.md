# kIOHIDDeviceQueueInterfaceID

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOHIDDeviceQueueInterfaceID
```

## Discussion

This UUID constant is used to obtain a queue interface corresponding to an IOHIDDevice service in the kernel. The type of this queue interface is IOHIDDeviceQueueInterface. This device interface is obtained after the device interface for the service itself has been obtained.

**Note:** Please note that subsequent calls to QueryInterface with the UUID kIOHIDDeviceQueueInterfaceID, will return a retained instance of a new IOHIDDeviceQueueInterface.

Example:

```occ
 
 
    IOCFPluginInterface **          iodev; 	// obtained earlier
 
    IOHIDDeviceQueueInterface **    intf;   // fetching this now
    IOReturn                        err;
 
    err = (*iodev)->QueryInterface(iodev,
                                CFUUIDGetUUIDBytes(kIOHIDDeviceQueueInterfaceID),
                                (LPVoid)&intf);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiohiddevicequeueinterfaceid)*