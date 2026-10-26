# GetSCSITaskDeviceInterface

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Gets a handle to the SCSITaskDeviceInterface without closing the user client connection which was initiated by IOCreateCFPlugInForService.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
SCSITaskDeviceInterface **(*GetSCSITaskDeviceInterface)(void *self);
```

#### Return Value

Returns a handle to a SCSITaskDeviceInterface if successful, otherwise NULL.

#### Discussion

Once an MMCDeviceInterface is opened the client may use this function to get a handle to the interface used to create and send SCSITasks directly to the device.

## Parameters

- `self`: Pointer to an MMCDeviceInterface for one IOService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/mmcdeviceinterface/1575395-getscsitaskdeviceinterface)*