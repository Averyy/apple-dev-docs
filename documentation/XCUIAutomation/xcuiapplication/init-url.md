# init(url:)

**Framework**: XCUIAutomation  
**Kind**: init

Creates a proxy for the application at the specified file system URL.

**Availability**:
- macOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
init(url: URL)
```

#### Discussion

This initializer is only available on macOS.

## See Also

- [init()](xcuiapplication/init.md)
  Creates a proxy for the application that’s configured as the Target Application in Xcode’s target settings.
- [init(bundleIdentifier: String)](xcuiapplication/init(bundleidentifier:).md)
  Creates a proxy for an application for the specified bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/init(url:))*