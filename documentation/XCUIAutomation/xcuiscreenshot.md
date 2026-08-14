# XCUIScreenshot

**Framework**: XCUIAutomation  
**Kind**: class

A captured image of a screen, app, or UI element state.

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
class XCUIScreenshot
```

#### Overview

Screenshots capture the current UI state of classes that conform to the [`XCUIScreenshotProviding`](xcuiscreenshotproviding.md) protocol, such as [`XCUIScreen`](xcuiscreen.md) and [`XCUIElement`](xcuielement.md). Each screenshot contains an image representation of the captured UI at the point the screenshot was taken.

The following code demonstrates taking screenshots of a screen and a UI element:

```swift
func testTakeScreenshots() {

    // Take a screenshot of the current device's main screen.
    let mainScreenScreenshot = XCUIScreen.main.screenshot()
    
    // Take a screenshot of an app's first window.
    let app = XCUIApplication()
    app.launch()
    let windowScreenshot = app.windows.firstMatch.screenshot()

}
```

If you use [`XCTest`](https://developer.apple.com/documentation/xctest) for your UI automation tests, you can attach a screenshot of your app’s UI to a test or activity to store it for later analysis. Create an attachment for a screenshot by calling the [`XCTAttachment`](https://developer.apple.com/documentation/xctest/xctattachment) initializer [`init(screenshot:)`](https://developer.apple.com/documentation/xctest/xctattachment/init(screenshot:)) or [`init(screenshot:quality:)`](https://developer.apple.com/documentation/xctest/xctattachment/init(screenshot:quality:)). Add the attachment to a test or activity by calling the [`XCTActivity`](https://developer.apple.com/documentation/xctest/xctactivity) method [`add(_:)`](https://developer.apple.com/documentation/xctest/xctactivity/add(_:)). For more information, see [`Adding Attachments to Tests, Activities, and Issues`](https://developer.apple.com/documentation/xctest/adding-attachments-to-tests-activities-and-issues).

## Topics

### Screenshot representations
- [var image: UIImage](xcuiscreenshot/image.md)
  A representation of the screenshot as a platform-native image object.
- [var pngRepresentation: Data](xcuiscreenshot/pngrepresentation.md)
  A representation of the screenshot as PNG image data.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class XCUIScreen](xcuiscreen.md)
  A physical screen attached to a device.
- [protocol XCUIScreenshotProviding](xcuiscreenshotproviding.md)
  A type that can provide a screenshot of its current UI state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiscreenshot)*