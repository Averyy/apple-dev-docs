# press(forDuration:thenDragTo:)

**Framework**: XCUIAutomation  
**Kind**: method

Initiates a press-and-hold gesture, then drags to another element.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func press(forDuration duration: TimeInterval, thenDragTo otherElement: XCUIElement)
```

#### Discussion

This interaction is suitable for table-cell reordering and similar operations.

## Parameters

- `duration`: The duration of the initial press-and-hold gesture.
- `otherElement`: The element over which to finish the drag. For example, when reordering table cells, this element is the reorder icon of the destination row.

## See Also

- [func tap()](xcuielement/tap.md)
  Sends a tap event to a hittable point the system computes for the element.
- [func doubleTap()](xcuielement/doubletap.md)
  Sends a double-tap event to a hittable point the system computes for the element.
- [func press(forDuration: TimeInterval)](xcuielement/press(forduration:).md)
  Sends a press-and-hold gesture to a hittable point the system computes for the element, holding for the duration you specify.
- [func press(forDuration: TimeInterval, thenDragTo: XCUIElement, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](xcuielement/press(forduration:thendragto:withvelocity:thenholdforduration:).md)
  Initiates a press-and-hold gesture, drags to another element at a velocity, and holds for a duration, all of which you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/press(forduration:thendragto:))*