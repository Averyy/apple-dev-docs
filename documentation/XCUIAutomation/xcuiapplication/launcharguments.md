# launchArguments

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

The arguments that pass to the application on launch.

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
var launchArguments: [String] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * launchArguments;
```

## Discussion

If not modified, these are the arguments that Xcode passes to the application on launch. You can change, add to, or remove the arguments. Unlike with [`Process`](../../Foundation/process.md), you can also modify these arguments after the application launches. Such changes don’t affect the current launch session, but do take effect the next time the application launches.

## See Also

### Launching the application
- [func launch()](./launch%28%29.md)
  Launches the application.
- [var launchEnvironment: [String : String]](./launchenvironment.md)
  The environment variables that pass to the application on launch.
- [func open(URL)](./open%28_%29.md)
  Launches the application by URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/launcharguments)*