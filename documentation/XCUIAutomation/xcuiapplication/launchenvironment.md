# launchEnvironment

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

The environment variables that pass to the application on launch.

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
var launchEnvironment: [String : String] { get set }
```

```objc
@property (nonatomic, copy) NSDictionary<NSString *,NSString *> * launchEnvironment;
```

#### Discussion

If not modified, these are the environment variables that Xcode passes to the application on launch. You can change, add to, or remove the environment variables. Unlike with [`Process`](../../Foundation/process.md), you can modify the environment variables after the application launches. Such changes don’t affect the current launch session, but do take effect the next time the application launches.

## See Also

### Launching the application
- [func launch()](./launch%28%29.md)
  Launches the application.
- [var launchArguments: [String]](./launcharguments.md)
  The arguments that pass to the application on launch.
- [func open(URL)](./open%28_%29.md)
  Launches the application by URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuiapplication/launchenvironment)*