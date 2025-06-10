# screenPoint

**Framework**: XCUIAutomation  
**Kind**: property

The dynamically computed value of the coordinate’s location on screen.

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
var screenPoint: CGPoint { get }
```

#### Discussion

Note that this value is dependent on the current frame of the referenced element. If the element’s frame changes, so does the value returned by this property. If the referenced element doesn’t exist when you call this property, the system fails the current test. Check the referenced element’s [`exists`](xcuielement/exists.md) property to veryify whether the element is present.

## See Also

- [var referencedElement: XCUIElement](xcuicoordinate/referencedelement.md)
  The element that the coordinate is based on, either directly or through the coordinate from which it was derived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuicoordinate/screenpoint)*