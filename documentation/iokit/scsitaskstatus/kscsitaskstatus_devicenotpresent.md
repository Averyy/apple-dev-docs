# kSCSITaskStatus_DeviceNotPresent

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
kSCSITaskStatus_DeviceNotPresent = 0x04
```

## Discussion

If the task is unable to be delivered because the device has been detached, the task status shall be set to kSCSITaskStatus_DeviceNotPresent. This will allow the SCSI Application Layer to halt the sending of tasks to the device and, if supported, perform any device failover or system cleanup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskstatus/kscsitaskstatus_devicenotpresent)*