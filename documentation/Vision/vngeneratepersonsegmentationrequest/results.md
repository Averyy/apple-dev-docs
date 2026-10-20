# results

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The results of the segmentation request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var results: [VNPixelBufferObservation]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<VNPixelBufferObservation *> * results;
```

## See Also

### Accessing the Results
- [class VNPixelBufferObservation](../vnpixelbufferobservation.md)
  An object that represents an image that an image-analysis request produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vngeneratepersonsegmentationrequest/results)*