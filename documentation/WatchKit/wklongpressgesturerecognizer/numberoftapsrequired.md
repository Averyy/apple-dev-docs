# numberOfTapsRequired

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The number of taps on the interface object that are required for the gesture to be recognized.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var numberOfTapsRequired: Int { get set }
```

```objc
@property (nonatomic) NSUInteger numberOfTapsRequired;
```

## Discussion

The default value of this property is `1`, but you can change this value when configuring the gesture recognizer in Interface Builder.

## See Also

### Configuring the Gesture Recognizer
- [var minimumPressDuration: CFTimeInterval](./minimumpressduration.md)
  The minimum amount of time (in seconds) that the user’s fingers must be touching the interface object.
- [var allowableMovement: CGFloat](./allowablemovement.md)
  The maximum movement of the finger on the interface object that allows the gesture to be recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/numberoftapsrequired)*