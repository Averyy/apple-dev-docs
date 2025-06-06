# hasSmile

**Framework**: Core Image  
**Kind**: instp

A Boolean value that indicates whether a smile is detected in the face.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var hasSmile: Bool { get }
```

#### Discussion

For smiles to be detected, the key [`CIDetectorSmile`](cidetectorsmile.md) must be present with a value of [`true`](https://developer.apple.com/documentation/swift/true) in the dictionary passed to a detector’s [`features(in:options:)`](cidetector/1438189-features.md) method.

## See Also

- [var hasLeftEyePosition: Bool](cifacefeature/1437900-haslefteyeposition.md)
  A Boolean value that indicates whether the detector found the face’s left eye.
- [var hasRightEyePosition: Bool](cifacefeature/1438076-hasrighteyeposition.md)
  A Boolean value that indicates whether the detector found the face’s right eye.
- [var hasMouthPosition: Bool](cifacefeature/1437976-hasmouthposition.md)
  A Boolean value that indicates whether the detector found the face’s mouth.
- [var leftEyePosition: CGPoint](cifacefeature/1437923-lefteyeposition.md)
  The coordinates of the left eye, in image coordinates.
- [var rightEyePosition: CGPoint](cifacefeature/1438213-righteyeposition.md)
  The coordinates of the right eye, in image coordinates
- [var mouthPosition: CGPoint](cifacefeature/1438020-mouthposition.md)
  The coordinates of the mouth, in image coordinates
- [var leftEyeClosed: Bool](cifacefeature/1437630-lefteyeclosed.md)
  A Boolean value that indicates whether a closed left eye is detected in the face.
- [var rightEyeClosed: Bool](cifacefeature/1437615-righteyeclosed.md)
  A Boolean value that indicates whether a closed right eye is detected in the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifacefeature/1437882-hassmile)*