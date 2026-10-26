# IODataQueueEntry

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

Represents an entry within the data queue

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
typealias IODataQueueEntry = _IODataQueueEntry
```

```c
typedef struct _IODataQueueEntry {
    ...
} IODataQueueEntry;
```

#### Discussion

This is a variable sized struct. The data field simply represents the start of the data region. The size of the data region is stored in the size field. The whole size of the specific entry is the size of a UInt32 plus the size of the data region.

## Topics

### Instance Properties
- [data](./iodataqueueentry/api-1456748-data.md)
- [size](./iodataqueueentry/api-1456739-size.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iodataqueueentry)*