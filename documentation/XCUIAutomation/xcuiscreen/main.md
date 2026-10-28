# main

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Type Property

The current device’s main screen.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
class var main: XCUIScreen { get }
```

```objc
@property (class, strong, readonly) XCUIScreen * mainScreen;
```

## Discussion

On macOS, [`main`](./main.md) represents the screen that owns the menu bar. On iOS and tvOS, [`main`](./main.md) represents the primary screen of the device.

## See Also

### Device screens
- [class var screens: [XCUIScreen]](./screens.md)
  The current device’s active screens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiscreen/main)*