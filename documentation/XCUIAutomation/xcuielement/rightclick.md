# rightClick()

**Framework**: XCUIAutomation  
**Kind**: method

Sends a Control-click event to a hittable point the system computes for the element.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
func rightClick()
```

#### Discussion

If the element exists within a scrollable view but is offscreen, XCTest attempts to scroll the element onscreen before performing the Control-click.

## See Also

- [func click()](xcuielement/click.md)
  Sends a click event to a hittable point computed for the element.
- [func click(forDuration: TimeInterval, thenDragTo: XCUIElement)](xcuielement/click(forduration:thendragto:).md)
  Clicks and holds an element for a duration you specify, and then drags it to another element.
- [func click(forDuration: TimeInterval, thenDragTo: XCUIElement, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](xcuielement/click(forduration:thendragto:withvelocity:thenholdforduration:).md)
  Clicks and holds an element for a duration, drags it at a velocity, and holds it over another element for a duration, all of which you specify.
- [func doubleClick()](xcuielement/doubleclick.md)
  Sends a double-click event to a hittable point the system computes for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/rightclick())*