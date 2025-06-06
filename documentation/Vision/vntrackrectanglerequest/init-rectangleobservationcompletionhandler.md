# init(rectangleObservation:completionHandler:)

**Framework**: Vision  
**Kind**: init

Creates a new rectangle tracking request with a rectangle observation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(rectangleObservation observation: VNRectangleObservation, completionHandler: VNRequestCompletionHandler? = nil)
```

## Parameters

- `observation`: A rectangle observation with bounding box and corner location information.
- `completionHandler`: The block to invoke after performing the request.

## See Also

- [convenience init(rectangleObservation: VNRectangleObservation)](vntrackrectanglerequest/init(rectangleobservation:).md)
  Creates a new rectangle tracking request with a rectangle observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackrectanglerequest/init(rectangleobservation:completionhandler:))*