# kIOMediaPartitionIDKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A property of IOMedia objects.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
#define kIOMediaPartitionIDKey
```

#### Discussion

The kIOMediaPartitionIDKey property has an OSNumber value and is placed into an IOMedia instance created via the partition scheme. It is an ID that differentiates one partition from the other (within a given scheme). It is typically an index into the on-disk partition table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiomediapartitionidkey)*