# launchEnvironment

**Framework**: Xcuiautomation  
**Kind**: property

The environment variables that pass to the application on launch.

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
var launchEnvironment: [String : String] { get set }
```

#### Discussion

If not modified, these are the environment variables that Xcode passes to the application on launch. You can change, add to, or remove the environment variables. Unlike with [`Process`](https://developer.apple.com/documentation/Foundation/Process), you can modify the environment variables after the application launches. Such changes don’t affect the current launch session, but do take effect the next time the application launches.

## See Also

- [func launch()](xcuiapplication/launch.md)
  Launches the application.
- [var launchArguments: [String]](xcuiapplication/launcharguments.md)
  The arguments that pass to the application on launch.
- [func open(URL)](xcuiapplication/open(_:).md)
  Launches the application by URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/launchenvironment)*