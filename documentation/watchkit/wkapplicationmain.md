# WKApplicationMain(_:_:_:)

**Framework**: Watchkit  
**Kind**: func

Creates the application object and the application delegate, and sets up the app’s event cycle.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
func WKApplicationMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, _ applicationDelegateClassName: String?) -> Int32
```

#### Return Value

Even though this function specifies an integer return type, it never returns. When the user exits a watchOS app, the app moves to the background.

#### Discussion

This function instantiates the application object and the specified delegate (if any), and then sets the delegate for the application. It also sets up the main event loop, including the application’s run loop, and begins processing events.

## Parameters

- `argc`: The count of arguments in  . This is usually the corresponding parameter to  .
- `argv`: A variable list of arguments. This is usually the corresponding parameter to  .
- `applicationDelegateClassName`: The name of the app delegate’s class. This class must subclass   and adopt the   protocol.

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [class WKApplication](wkapplication.md)
  The centralized point of control and coordination for apps with a single watchOS app target.
- [protocol WKApplicationDelegate](wkapplicationdelegate.md)
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
- [class WKExtension](wkextension.md)
  The centralized point of control and coordination for extension-based apps running in watchOS.
- [protocol WKExtensionDelegate](wkextensiondelegate.md)
  A collection of methods that manages the app-level behavior of a WatchKit extension.
- [class WKInterfaceDevice](wkinterfacedevice.md)
  An object that provides information about the user’s Apple Watch.
- [WKPrefersNetworkUponForeground](../BundleResources/Information-Property-List/WKPrefersNetworkUponForeground.md)
  A Boolean value that indicates whether an app requires network access on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:))*