# IODataQueueAppendix

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

A struct mapping to the appendix region of a data queue.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- visionOS 1.0+

## Declaration

```swift
typealias IODataQueueAppendix = _IODataQueueAppendix
```

```c
typedef struct _IODataQueueAppendix {
    ...
} IODataQueueAppendix;
```

#### Discussion

This struct is variable sized dependent on the version. The struct represents the data queue appendix information.

## Topics

### Instance Properties
- [msgh](./iodataqueueappendix/api-1456751-msgh.md)
- [version](./iodataqueueappendix/api-1456755-version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iodataqueueappendix)*