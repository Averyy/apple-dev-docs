# init(url:)

**Framework**: XCUIAutomation  
**Kind**: init  
**Role**: Initializer

Creates a proxy for the application at the specified file system URL.

**Availability**:
- macOS
- Xcode 16.3+

## Declaration

```swift
init(url: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) url;
```

#### Discussion

This initializer is only available on macOS.

## See Also

### Creating an application proxy
- [init()](./init%28%29.md)
  Creates a proxy for the application that’s configured as the Target Application in Xcode’s target settings.
- [init(bundleIdentifier: String)](./init%28bundleidentifier%29.md)
  Creates a proxy for an application for the specified bundle identifier.
- [+ new](./new.md)
  Creates a proxy for the application specified as the Target Application in Xcode’s target settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/init(url:)-90e7z)*