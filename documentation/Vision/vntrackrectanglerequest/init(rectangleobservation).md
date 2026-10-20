# init(rectangleObservation:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

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
convenience init(rectangleObservation observation: VNRectangleObservation)
```

```objc
- (instancetype) initWithRectangleObservation:(VNRectangleObservation *) observation;
```

## Parameters

- `observation`: A rectangle observation with bounding box and corner location information.

## See Also

### Initializing a Rectangle Tracking Request
- [init(rectangleObservation: VNRectangleObservation, completionHandler: VNRequestCompletionHandler?)](./init%28rectangleobservation,completionhandler%29.md)
  Creates a new rectangle tracking request with a rectangle observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackrectanglerequest/init(rectangleobservation:))*