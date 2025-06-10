# kSCSITaskStatus_DeviceNotResponding

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.3+

## Declaration

```swift
kSCSITaskStatus_DeviceNotResponding = 0x03
```

#### Discussion

If a task is unable to be delivered due to a failure of the device not accepting the task or the device acknowledging the attempt to send it the device the task status shall be set to kSCSITaskStatus_DeviceNotResponding. This will allow the SCSI Application driver to perform the necessary steps to try to recover the device. This shall only be reported after the SCSI Protocol Layer driver has attempted all protocol specific attempts to recover the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsitaskstatus/kscsitaskstatus_devicenotresponding)*