# init(detectedObjectObservation:completionHandler:)

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
init(detectedObjectObservation observation: VNDetectedObjectObservation, completionHandler: VNRequestCompletionHandler? = nil)
```

```objc
- (instancetype) initWithDetectedObjectObservation:(VNDetectedObjectObservation *) observation completionHandler:(VNRequestCompletionHandler) completionHandler;
```

## Parameters

- `observation`: A detected object observation with bounding box information.
- `completionHandler`: The callback to invoke after performing the request.

## See Also

### Initializing an Object Tracking Request
- [init(detectedObjectObservation: VNDetectedObjectObservation)](./init%28detectedobjectobservation%29.md)
  Creates a new object tracking request with a detected object observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vntrackobjectrequest/init(detectedobjectobservation:completionhandler:))*