# indeterminate

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean set to true when a request can’t determine its progress in fractions completed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var indeterminate: Bool { get }
```

```objc
@property (readonly) BOOL indeterminate;
```

#### Discussion

A value of [`true`](../../Swift/true.md) doesn’t mean that the request will run forever. Rather, it means that the nature of the request can’t be broken down into identifiable fractions to report. The [`progressHandler`](./progresshandler.md) will still be called at suitable intervals.

## See Also

### Tracking Progress
- [var progressHandler: VNRequestProgressHandler](./progresshandler.md)
  A block of code executed periodically during a Vision request to report progress on long-running tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequestprogressproviding/indeterminate)*