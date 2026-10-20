# velocityInObject()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

The velocity of the pan gesture in the current object.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
func velocityInObject() -> CGPoint
```

```objc
- (CGPoint) velocityInObject;
```

#### Return Value

The velocity of the gesture, which is expressed in points per second. The `x` field contains the horizontal velocity and the `y` field contains the vertical velocity.

## See Also

### Tracking the Location and Velocity of the Gesture
- [func translationInObject() -> CGPoint](./translationinobject%28%29.md)
  The amount of translation for the pan gesture in the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer/velocityinobject())*