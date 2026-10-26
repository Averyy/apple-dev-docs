# SCSITaggedTaskIdentifier

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

64-bit number to represent a unique task identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
typedef UInt64 SCSITaggedTaskIdentifier;
```

#### Discussion

The Tagged Task Identifier is used when a Task has a Task Attribute other than SIMPLE. The SCSI Application Layer client that controls the Logical Unit for which a Task is intended is required to guarantee that the Task Tag Identifier is unique. Zero cannot be used a a Tag value as this is used to when a Tagged Task Identifier value is needed for a Task with a SIMPLE attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaggedtaskidentifier)*