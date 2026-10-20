# press(forDuration:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Sends a press-and-hold gesture to a hittable point the system computes for the element, holding for the duration you specify.

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
func press(forDuration duration: TimeInterval)
```

```objc
- (void) pressForDuration:(NSTimeInterval) duration;
```

#### Discussion

If the element exists within a scrollable view but is offscreen, XCTest attempts to scroll the element onscreen before performing the press.

## Parameters

- `duration`: The duration of the press, in seconds.

## See Also

### Tapping and pressing
- [func tap()](./tap%28%29.md)
  Sends a tap event to a hittable point the system computes for the element.
- [func doubleTap()](./doubletap%28%29.md)
  Sends a double-tap event to a hittable point the system computes for the element.
- [func press(forDuration: TimeInterval, thenDragTo: XCUIElement)](./press%28forduration,thendragto%29.md)
  Initiates a press-and-hold gesture, then drags to another element.
- [func press(forDuration: TimeInterval, thenDragTo: XCUIElement, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](./press%28forduration,thendragto,withvelocity,thenholdforduration%29.md)
  Initiates a press-and-hold gesture, drags to another element at a velocity, and holds for a duration, all of which you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/press(forduration:))*