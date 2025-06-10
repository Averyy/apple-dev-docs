# leftEyeClosed

**Framework**: Core Image  
**Kind**: property

A Boolean value that indicates whether a closed left eye is detected in the face.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var leftEyeClosed: Bool { get }
```

#### Discussion

“Left” is relative to the original (non-mirrored) image orientation, not to the owner of the eye.

For closed eyes to be detected, the key [`CIDetectorEyeBlink`](cidetectoreyeblink.md) must be present with a value of [`true`](https://developer.apple.com/documentation/swift/true) in the dictionary passed to a detector’s [`features(in:options:)`](cidetector/features(in:options:).md) method.

## See Also

- [var hasLeftEyePosition: Bool](cifacefeature/haslefteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s left eye.
- [var hasRightEyePosition: Bool](cifacefeature/hasrighteyeposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s right eye.
- [var hasMouthPosition: Bool](cifacefeature/hasmouthposition-swift.property.md)
  A Boolean value that indicates whether the detector found the face’s mouth.
- [var leftEyePosition: CGPoint](cifacefeature/lefteyeposition-swift.property.md)
  The coordinates of the left eye, in image coordinates.
- [var rightEyePosition: CGPoint](cifacefeature/righteyeposition-swift.property.md)
  The coordinates of the right eye, in image coordinates
- [var mouthPosition: CGPoint](cifacefeature/mouthposition-swift.property.md)
  The coordinates of the mouth, in image coordinates
- [var hasSmile: Bool](cifacefeature/hassmile-swift.property.md)
  A Boolean value that indicates whether a smile is detected in the face.
- [var rightEyeClosed: Bool](cifacefeature/righteyeclosed-swift.property.md)
  A Boolean value that indicates whether a closed right eye is detected in the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifacefeature/lefteyeclosed-swift.property)*