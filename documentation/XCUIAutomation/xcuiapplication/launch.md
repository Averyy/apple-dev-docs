# launch()

**Framework**: Xcuiautomation  
**Kind**: method

Launches the application.

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
func launch()
```

#### Discussion

This call is synchronous. When it returns, the application launches and is ready to handle user events. The system reports any failure in the launch sequence as a test failure and halts the test at this point.

If the application is already running, this call terminates the existing instance, to ensure a clean launch state for the newly launched instance.

## See Also

- [var launchArguments: [String]](xcuiapplication/launcharguments.md)
  The arguments that pass to the application on launch.
- [var launchEnvironment: [String : String]](xcuiapplication/launchenvironment.md)
  The environment variables that pass to the application on launch.
- [func open(URL)](xcuiapplication/open(_:).md)
  Launches the application by URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/launch())*