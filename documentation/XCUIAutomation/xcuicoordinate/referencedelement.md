# referencedElement

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

The element that the coordinate is based on, either directly or through the coordinate from which it was derived.

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
var referencedElement: XCUIElement { get }
```

```objc
@property (readonly) XCUIElement * referencedElement;
```

## See Also

### Getting coordinate properties
- [var screenPoint: CGPoint](./screenpoint.md)
  The dynamically computed value of the coordinate’s location on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/referencedelement)*