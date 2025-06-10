# kSCSITaskStatus_DeliveryFailure

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.3+

## Declaration

```swift
kSCSITaskStatus_DeliveryFailure = 0x05
```

#### Discussion

If the task is unable to be delivered to the device due to a failure in the SCSI Protocol Layer, such as a bus reset or communications error, but the device is is known to be functioning properly, the task status shall be set to kSCSITaskStatus_DeliveryFailure. This can also be reported if the task could not be delivered due to a protocol error that has since been corrected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsitaskstatus/kscsitaskstatus_deliveryfailure)*