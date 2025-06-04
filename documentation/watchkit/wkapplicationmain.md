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

## Overview

Even though this function specifies an integer return type, it never returns. When the user exits a watchOS app, the app moves to the background.

## Parameters

- `argc`: The count of arguments in  . This is usually the corresponding parameter to  .
- `argv`: A variable list of arguments. This is usually the corresponding parameter to  .
- `applicationDelegateClassName`: The name of the app delegate’s class. This class must subclass   and adopt the   protocol.

## Discussion

This function instantiates the application object and the specified delegate (if any), and then sets the delegate for the application. It also sets up the main event loop, including the application’s run loop, and begins processing events.

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/setting-up-a-watchos-project))
- [class WKApplication](wkapplication.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication))
- [protocol WKApplicationDelegate](wkapplicationdelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate))
- [class WKExtension](wkextension.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension))
- [protocol WKExtensionDelegate](wkextensiondelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate))
- [class WKInterfaceDevice](wkinterfacedevice.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice))
- WKPrefersNetworkUponForeground ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKPrefersNetworkUponForeground))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:))*