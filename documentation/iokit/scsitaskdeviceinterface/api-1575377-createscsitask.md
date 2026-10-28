# CreateSCSITask

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to create SCSITasks.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
SCSITaskInterface **(*CreateSCSITask)(void *self);
```

## Return Value

Returns a handle to an instance of a SCSITaskInterface or NULL if one could not be allocated.

## Discussion

Once a SCSITaskDeviceInterface is opened, the client may request exclusive access to the device. Once the client has successfully gained exclusive access, it becomes the Logical Unit Driver. It then can use this method to allocate SCSITasks to be sent to the device.

## Parameters

- `self`: Pointer to a SCSITaskDeviceInterface instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskdeviceinterface/1575377-createscsitask)*