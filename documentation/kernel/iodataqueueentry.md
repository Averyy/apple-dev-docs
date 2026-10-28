# IODataQueueEntry

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

Represents an entry within the data queue

**Availability**:
- macOS 10.12+

## Declaration

```c
typedef struct _IODataQueueEntry IODataQueueEntry;
```

## Discussion

This is a variable sized struct. The data field simply represents the start of the data region. The size of the data region is stored in the size field. The whole size of the specific entry is the size of a UInt32 plus the size of the data region.

## Topics

### Instance Properties
- [data](./iodataqueueentry/api-1419868-data.md)
- [size](./iodataqueueentry/api-1419876-size.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueueentry)*