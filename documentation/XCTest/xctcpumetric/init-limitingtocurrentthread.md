# init(limitingToCurrentThread:)

**Framework**: XCTest  
**Kind**: init

Creates a CPU metric that optionally records data only for the current thread.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(limitingToCurrentThread limitToCurrentThread: Bool)
```

#### Discussion

If `limitToCurrentThread` is `true`, the returned metric only records data related to CPU use on the current thread. In a single-threaded context, a thread-limited metric provides lower variance and greater precision than a whole-process metric.

## Parameters

- `limitToCurrentThread`: A Boolean value that specifies whether to limit the recording of data for this metric to the current thread only.

## See Also

- [init()](xctcpumetric/init.md)
  Creates a CPU metric that records data for the current process.
- [init(application: XCUIApplication)](xctcpumetric/init(application:).md)
  Creates a CPU metric that records data for the requested app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctcpumetric/init(limitingtocurrentthread:))*