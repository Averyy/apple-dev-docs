# ReleaseExclusiveAccess

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to release exclusive access to the device so that other clients can send commands to it.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ReleaseExclusiveAccess)(void *self);
```

## Return Value

Returns kIOReturnSuccess if exclusive access was released, else some appropriate error.

## Discussion

Once a SCSITaskDeviceInterface is opened, the client may request exclusive access to the device. Once the client has successfully gained exclusive access, it becomes the Logical Unit Driver and all in-kernel Logical Unit Drivers (if any are matched on the device) are quiesced. This method releases this access and unquiesces the in-kernel drivers (if any).

## Parameters

- `self`: Pointer to a SCSITaskDeviceInterface instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskdeviceinterface/1575344-releaseexclusiveaccess)*