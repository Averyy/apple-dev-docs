# queueSize

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

Size of this queue.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var queueSize: UInt16 { get }
```

```objc
@property (readonly) uint16_t queueSize;
```

## Discussion

The size of the queue indicates the maximum number of `VZVirtioQueueElement` that can be made available in the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtioqueue/queuesize)*