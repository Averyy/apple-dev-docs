# main

**Framework**: Xcuiautomation  
**Kind**: property

The current device’s main screen.

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
class var main: XCUIScreen { get }
```

#### Discussion

On macOS, [`main`](xcuiscreen/main.md) represents the screen that owns the menu bar. On iOS and tvOS, [`main`](xcuiscreen/main.md) represents the primary screen of the device.

## See Also

- [class var screens: [XCUIScreen]](xcuiscreen/screens.md)
  The current device’s active screens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiscreen/main)*