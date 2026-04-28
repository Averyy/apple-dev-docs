# perform(_:)

**Framework**: Vision  
**Kind**: method

Performs a framework request on the handler’s image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final func perform<T>(_ request: T) async throws -> T.Result where T : TargetedRequest
```

## See Also

- [func perform<each T>(repeat each T) async throws -> (repeat (each T).Result)](targetedimagerequesthandler/perform(_:)-1i4di.md)
  Performs one or more framework requests on the handler’s image.
- [func performAll(some Collection<any TargetedRequest>) -> some AsyncSequence<VisionResult, Never>
](targetedimagerequesthandler/performall(_:).md)
  Schedules a collection of framework requests to perform on the handler’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/targetedimagerequesthandler/perform(_:)-2r0k8)*