# indeterminate

**Framework**: Vision  
**Kind**: property  
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

#### Discussion

A value of [`true`](https://developer.apple.com/documentation/swift/true) doesn’t mean that the request will run forever. Rather, it means that the nature of the request can’t be broken down into identifiable fractions to report. The [`progressHandler`](vnrequestprogressproviding/progresshandler.md) will still be called at suitable intervals.

## See Also

- [var progressHandler: VNRequestProgressHandler](vnrequestprogressproviding/progresshandler.md)
  A block of code executed periodically during a Vision request to report progress on long-running tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnrequestprogressproviding/indeterminate)*