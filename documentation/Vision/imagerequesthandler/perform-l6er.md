# perform(_:)

**Framework**: Vision  
**Kind**: method

Performs one or more framework requests on the handler’s image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final func perform<each T>(_ request: repeat each T) async throws -> (repeat (each T).Result) where repeat each T : VisionRequest
```

#### Discussion

The function returns after all requests complete.

## See Also

- [func perform<T>(T) async throws -> T.Result](imagerequesthandler/perform(_:)-7b6g5.md)
  Performs a framework request on the handler’s image.
- [func performAll(some Collection<any VisionRequest>) -> some AsyncSequence<VisionResult, Never>
](imagerequesthandler/performall(_:).md)
  Schedules a collection of framework requests to perform on the handler’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler/perform(_:)-l6er)*