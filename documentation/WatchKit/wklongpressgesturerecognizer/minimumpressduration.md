# minimumPressDuration

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The minimum amount of time (in seconds) that the user’s fingers must be touching the interface object.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var minimumPressDuration: CFTimeInterval { get set }
```

```objc
@property (nonatomic) CFTimeInterval minimumPressDuration;
```

## Discussion

The default value of this property is `0.5` seconds, but you can change this value when configuring the gesture recognizer in Interface Builder.

## See Also

### Configuring the Gesture Recognizer
- [var numberOfTapsRequired: Int](./numberoftapsrequired.md)
  The number of taps on the interface object that are required for the gesture to be recognized.
- [var allowableMovement: CGFloat](./allowablemovement.md)
  The maximum movement of the finger on the interface object that allows the gesture to be recognized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/minimumpressduration)*