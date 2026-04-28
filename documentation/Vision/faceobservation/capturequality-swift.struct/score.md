# score

**Framework**: Vision  
**Kind**: property

A value that indicates the quality of the face capture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let score: Float
```

#### Discussion

The score allows you to compare the quality of the face in terms of its capture attributes: lighting, blur, and prime positioning. Use this value to compare the capture quality of a face against other captures of the same face in a specified set. The value of this property value ranges from `0.0` to `1.0`. Faces with quality closer to `1.0` are better lit, sharper, and more centrally positioned than faces with quality closer to `0.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/faceobservation/capturequality-swift.struct/score)*