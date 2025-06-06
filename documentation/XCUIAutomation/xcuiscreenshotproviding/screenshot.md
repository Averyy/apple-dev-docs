# screenshot()

**Framework**: Xcuiautomation  
**Kind**: method  
**Required**: Yes

Takes a screenshot of a screen or UI element’s current visual state.

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
func screenshot() -> XCUIScreenshot
```

#### Discussion

The output of this method is equivalent to capturing a screenshot manually on a device. For example, if you take a screenshot of a window on macOS that is covered by another window, the covering window is visible in the screenshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiscreenshotproviding/screenshot())*