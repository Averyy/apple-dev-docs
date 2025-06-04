# dismiss()

**Framework**: Watchkit  
**Kind**: method

Dismisses the current interface controller from the screen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func dismiss()
```

## Overview

Call this method when you want to dismiss an interface controller that you presented modally. Always call this method from your WatchKit extension’s main thread.

## See Also

- [func presentController(withName: String, context: Any?)](presentcontroller(withname:context:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withname:context:)))
- [func presentController(withNames: [String], contexts: [Any]?)](presentcontroller(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnames:contexts:)))
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](presentcontroller(withnamesandcontexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnamesandcontexts:)))
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](presentalert(withtitle:message:preferredstyle:actions:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:)))
- [enum WKAlertControllerStyle](wkalertcontrollerstyle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss())*