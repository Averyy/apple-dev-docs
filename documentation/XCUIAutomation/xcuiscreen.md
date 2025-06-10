# XCUIScreen

**Framework**: XCUIAutomation  
**Kind**: class

A physical screen attached to a device.

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
class XCUIScreen
```

#### Overview

Call the [`screenshot()`](xcuiscreenshotproviding/screenshot().md) method on an [`XCUIScreen`](xcuiscreen.md) instance to capture a screenshot of its current UI state. The [`XCUIScreenshotProviding`](xcuiscreenshotproviding.md) protocol adds this method to [`XCUIScreen`](xcuiscreen.md).

You can take a screenshot of the current device’s main screen using the following code:

```swift
let screenshot = XCUIScreen.main.screenshot()
```

You can take a screenshot of every screen on the current device using the following code:

```swift
let allScreenshots = XCUIScreen.screens.map { screen in
    return screen.screenshot()
}
```

## Topics

### Device screens
- [class var main: XCUIScreen](xcuiscreen/main.md)
  The current device’s main screen.
- [class var screens: [XCUIScreen]](xcuiscreen/screens.md)
  The current device’s active screens.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [XCUIScreenshotProviding](xcuiscreenshotproviding.md)

## See Also

- [class XCUIScreenshot](xcuiscreenshot.md)
  A captured image of a screen, app, or UI element state.
- [protocol XCUIScreenshotProviding](xcuiscreenshotproviding.md)
  A type that can provide a screenshot of its current UI state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiscreen)*