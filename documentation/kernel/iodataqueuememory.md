# IODataQueueMemory

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

A struct mapping to the header region of a data queue.

**Availability**:
- macOS 10.12+

## Declaration

```c
typedef struct _IODataQueueMemory IODataQueueMemory;
```

#### Discussion

This struct is variable sized. The struct represents the data queue header information plus a pointer to the actual data queue itself. The size of the struct is the combined size of the header fields (3 * sizeof(UInt32)) plus the actual size of the queue region. This size is stored in the queueSize field.

## Topics

### Instance Properties
- [head](./iodataqueuememory/api-1419872-head.md)
- [queue](./iodataqueuememory/api-1419856-queue.md)
- [queueSize](./iodataqueuememory/api-1419860-queuesize.md)
- [tail](./iodataqueuememory/api-1419866-tail.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuememory)*