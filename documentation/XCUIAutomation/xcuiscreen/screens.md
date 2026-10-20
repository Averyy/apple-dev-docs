# screens

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Type Property

The current device’s active screens.

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
class var screens: [XCUIScreen] { get }
```

```objc
@property (class, copy, readonly) NSArray<XCUIScreen *> * screens;
```

#### Discussion

The first screen in the array represents the main screen.

## See Also

### Device screens
- [class var main: XCUIScreen](./main.md)
  The current device’s main screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiscreen/screens)*