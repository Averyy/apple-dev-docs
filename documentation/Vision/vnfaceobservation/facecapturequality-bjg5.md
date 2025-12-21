# faceCaptureQuality

**Framework**: Vision  
**Kind**: property

A value that indicates the quality of the face capture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+

## Declaration

```swift
@nonobjc
var faceCaptureQuality: Float? { get }
```

#### Discussion

The capture quality of the face allows you to compare the quality of the face in terms of its capture attributes: lighting, blur, and prime positioning. Use this value to compare the capture quality of a face against other captures of the same face in a specified set.

The value of this property value ranges from `0.0` to `1.0`. Faces with quality closer to `1.0` are better lit, sharper, and more centrally positioned than faces with quality closer to `0.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnfaceobservation/facecapturequality-bjg5)*