# click()

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Sends a click event to a hittable point computed for the element.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS
- Xcode 16.3+

## Declaration

```swift
func click()
```

```objc
- (void) click;
```

## Discussion

If the element exists within a scrollable view but is offscreen, the framework attempts to scroll the element onscreen before performing the click.

## See Also

### Clicking
- [func click(forDuration: TimeInterval, thenDragTo: XCUIElement)](./click%28forduration,thendragto%29.md)
  Clicks and holds an element for a duration you specify, and then drags it to another element.
- [func click(forDuration: TimeInterval, thenDragTo: XCUIElement, withVelocity: XCUIGestureVelocity, thenHoldForDuration: TimeInterval)](./click%28forduration,thendragto,withvelocity,thenholdforduration%29.md)
  Clicks and holds an element for a duration, drags it at a velocity, and holds it over another element for a duration, all of which you specify.
- [func doubleClick()](./doubleclick%28%29.md)
  Sends a double-click event to a hittable point the system computes for the element.
- [func rightClick()](./rightclick%28%29.md)
  Sends a Control-click event to a hittable point the system computes for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielement/click())*