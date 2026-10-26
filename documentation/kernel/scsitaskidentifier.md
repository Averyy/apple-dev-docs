# SCSITaskIdentifier

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.6+

## Declaration

```c
typedef OSObject *SCSITaskIdentifier;
```

#### Discussion

This is an opaque object that represents a task. This is used so that drivers for both the SCSI Protocol Layer and the SCSI Application Layer cannot modify the SCSITask object directly but must instead use the inherited methods to do so. This allows the implementation of SCSITask to change without directly impacting device and protocol layer drivers. In addition, it prevents changing of properties that are not allowed to be changed by a given layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scsitaskidentifier)*