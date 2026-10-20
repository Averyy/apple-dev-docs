# init(detectedObjectObservation:)

**Framework**: Vision  
**Kind**: init  
**Role**: Initializer

Creates a new object tracking request with a detected object observation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(detectedObjectObservation observation: VNDetectedObjectObservation)
```

```objc
- (instancetype) initWithDetectedObjectObservation:(VNDetectedObjectObservation *) observation;
```

## Parameters

- `observation`: A detected object observation with bounding box information.

## See Also

### Initializing an Object Tracking Request
- [init(detectedObjectObservation: VNDetectedObjectObservation, completionHandler: VNRequestCompletionHandler?)](./init%28detectedobjectobservation,completionhandler%29.md)
  Creates a new object tracking request with a detected object observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackobjectrequest/init(detectedobjectobservation:))*