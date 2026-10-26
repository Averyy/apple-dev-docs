# ObtainExclusiveAccess

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to obtain exclusive access to the device so that SCSITasks can be sent to it.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ObtainExclusiveAccess)(void *self);
```

#### Return Value

Returns kIOReturnSuccess if exclusive access was granted, else if media is still mounted it returns kIOReturnBusy. If another client already has exclusive access, kIOReturnExclusiveAccess is returned.

#### Discussion

Once a SCSITaskDeviceInterface is opened, the client may request exclusive access to the device. Once the client has successfully gained exclusive access, it becomes the Logical Unit Driver and all in-kernel Logical Unit Drivers are quiesced.

## Parameters

- `self`: Pointer to a SCSITaskDeviceInterface instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskdeviceinterface/1575374-obtainexclusiveaccess)*