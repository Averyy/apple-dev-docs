# performAll(_:)

**Framework**: Vision  
**Kind**: method

Schedules a collection of framework requests to perform on the handler’s image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
final func performAll(_ requests: some Collection<any VisionRequest>) -> some AsyncSequence<VisionResult, Never>
```

#### Return Value

A sequence of requests results.

#### Discussion

This function doesn’t wait for requests to complete before returning. You can receive request results from the `AsyncSequence` as they become available.

## Parameters

- `requests`: A collection of requests to perform.

## See Also

- [func perform<each T>(repeat each T) async throws -> (repeat (each T).Result)](imagerequesthandler/perform(_:)-l6er.md)
  Performs one or more framework requests on the handler’s image.
- [func perform<T>(T) async throws -> T.Result](imagerequesthandler/perform(_:)-7b6g5.md)
  Performs a framework request on the handler’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler/performall(_:))*