# perform(_:)

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Performs a framework request on the handler’s image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 27.0+

## Declaration

```swift
final func perform<T>(_ request: T) async throws -> T.Result where T : VisionRequest
```

## Mentions

- [Isolating an object from a tap, box, or scribble](../segmenting-objects-with-iterative-refinement.md)

## See Also

### Performing the request
- [func perform<each T>(repeat each T) async throws -> (repeat (each T).Result)](./perform%28_%29-l6er.md)
  Performs one or more framework requests on the handler’s image.
- [func performAll(some Collection<any VisionRequest>) -> some AsyncSequence<VisionResult, Never>
](./performall%28_%29.md)
  Schedules a collection of framework requests to perform on the handler’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/imagerequesthandler/perform(_:)-7b6g5)*