# XCUIScreenshotProviding

**Framework**: Xcuiautomation  
**Kind**: protocol

A type that can provide a screenshot of its current UI state.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
protocol XCUIScreenshotProviding : NSObjectProtocol
```

#### Overview

Call this protocol’s [`screenshot()`](xcuiscreenshotproviding/screenshot().md) method on an [`XCUIScreen`](xcuiscreen.md) or [`XCUIElement`](xcuielement.md) to capture a screenshot of its current UI state.

## Topics

### Taking a Screenshot
- [func screenshot() -> XCUIScreenshot](xcuiscreenshotproviding/screenshot.md)
  Takes a screenshot of a screen or UI element’s current visual state.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [XCUIApplication](xcuiapplication.md)
- [XCUIElement](xcuielement.md)
- [XCUIScreen](xcuiscreen.md)

## See Also

- [class XCUIScreen](xcuiscreen.md)
  A physical screen attached to a device.
- [class XCUIScreenshot](xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiscreenshotproviding)*