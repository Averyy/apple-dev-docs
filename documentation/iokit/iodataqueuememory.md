# IODataQueueMemory

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

A struct mapping to the header region of a data queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias IODataQueueMemory = _IODataQueueMemory
```

```c
typedef struct _IODataQueueMemory {
    ...
} IODataQueueMemory;
```

#### Discussion

This struct is variable sized. The struct represents the data queue header information plus a pointer to the actual data queue itself. The size of the struct is the combined size of the header fields (3 * sizeof(UInt32)) plus the actual size of the queue region. This size is stored in the queueSize field.

## Topics

### Instance Properties
- [head](./iodataqueuememory/api-1456736-head.md)
- [queue](./iodataqueuememory/api-1456749-queue.md)
- [queueSize](./iodataqueuememory/api-1456744-queuesize.md)
- [tail](./iodataqueuememory/api-1456737-tail.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iodataqueuememory)*