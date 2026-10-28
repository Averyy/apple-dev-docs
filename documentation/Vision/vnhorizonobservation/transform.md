# transform

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

The transform to apply to the detected horizon.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var transform: CGAffineTransform { get }
```

```objc
@property (nonatomic, assign, readonly) CGAffineTransform transform;
```

## Discussion

Apply the transform’s inverse to orient the image in an upright position and make the detected horizon level.

## See Also

### Evaluating the Horizon
- [var angle: CGFloat](./angle.md)
  The angle of the observed horizon.
- [func transform(forImageWidth: Int, height: Int) -> CGAffineTransform](./transform%28forimagewidth,height%29.md)
  Creates an affine transform for the specified image width and height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnhorizonobservation/transform)*