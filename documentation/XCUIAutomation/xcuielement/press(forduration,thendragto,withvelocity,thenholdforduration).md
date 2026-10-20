# press(forDuration:thenDragTo:withVelocity:thenHoldForDuration:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Initiates a press-and-hold gesture, drags to another element at a velocity, and holds for a duration, all of which you specify.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
func press(forDuration duration: TimeInterval, thenDragTo otherElement: XCUIElement, withVelocity velocity: XCUIGestureVelocity, thenHoldForDuration holdDuration: TimeInterval)
```

```objc
- (void) pressForDuration:(NSTimeInterval) duration thenDragToElement:(XCUIElement *) otherElement withVelocity:(XCUIGestureVelocity) velocity thenHoldForDuration:(NSTimeInterval) holdDuration;
```

## Parameters

- `duration`: The duration of the initial press-and-hold gesture.
- `otherElement`: The element over which to finish the drag gesture.
- `velocity`: The speed at which to move from the initial press position to the other element, expressed in pixels per second.
- `holdDuration`: The duration for which to hold the dragged element over the other element.

## See Also

### Tapping and pressing
- [func tap()](./tap%28%29.md)
  Sends a tap event to a hittable point the system computes for the element.
- [func doubleTap()](./doubletap%28%29.md)
  Sends a double-tap event to a hittable point the system computes for the element.
- [func press(forDuration: TimeInterval)](./press%28forduration%29.md)
  Sends a press-and-hold gesture to a hittable point the system computes for the element, holding for the duration you specify.
- [func press(forDuration: TimeInterval, thenDragTo: XCUIElement)](./press%28forduration,thendragto%29.md)
  Initiates a press-and-hold gesture, then drags to another element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/press(forduration:thendragto:withvelocity:thenholdforduration:))*