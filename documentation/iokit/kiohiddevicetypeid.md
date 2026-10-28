# kIOHIDDeviceTypeID

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOHIDDeviceTypeID
```

## Discussion

This UUID constant is used to obtain a device interface corresponding to an io_service_t corresponding to an IOHIDDevice in the kernel. Once you have obtained the IOCFPlugInInterface for the service, you must use the QueryInterface function to obtain the device interface for the user client itself.

Example:

```occ
 
 
    io_service_t            hidDeviceRef;   // obtained earlier
 
    IOCFPlugInInterface     **iodev;        // fetching this now
 
    SInt32                  score;          // not used
    IOReturn                err;
 
    err = IOCreatePlugInInterfaceForService(hidDeviceRef,
                                    kIOHIDDeviceTypeID,
                                    kIOCFPlugInInterfaceID,
                                    &iodev,
                                    &score);
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiohiddevicetypeid)*