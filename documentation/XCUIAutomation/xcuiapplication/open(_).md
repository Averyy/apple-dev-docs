# open(_:)

**Framework**: XCUIAutomation  
**Kind**: method  
**Role**: Instance Method

Launches the application by URL.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+
- Xcode 16.3+

## Declaration

```swift
func open(_ url: URL)
```

```objc
- (void) openURL:(NSURL *) url;
```

## Parameters

- `url`: The URL of the item to open the application to.

## See Also

### Launching the application
- [func launch()](./launch%28%29.md)
  Launches the application.
- [var launchArguments: [String]](./launcharguments.md)
  The arguments that pass to the application on launch.
- [var launchEnvironment: [String : String]](./launchenvironment.md)
  The environment variables that pass to the application on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/open(_:))*