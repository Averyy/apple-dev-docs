# allowableMovement

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The maximum movement of the finger on the interface object that allows the gesture to be recognized.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var allowableMovement: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat allowableMovement;
```

#### Discussion

The allowable movement is measured in points. The default value of this property is `10`, but you can change this value when configuring the gesture recognizer in Interface Builder.

## See Also

### Configuring the Gesture Recognizer
- [var minimumPressDuration: CFTimeInterval](./minimumpressduration.md)
  The minimum amount of time (in seconds) that the user’s fingers must be touching the interface object.
- [var numberOfTapsRequired: Int](./numberoftapsrequired.md)
  The number of taps on the interface object that are required for the gesture to be recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/allowablemovement)*