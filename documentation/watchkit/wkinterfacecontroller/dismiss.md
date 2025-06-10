# dismiss()

**Framework**: WatchKit  
**Kind**: method

Dismisses the current interface controller from the screen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func dismiss()
```

#### Discussion

Call this method when you want to dismiss an interface controller that you presented modally. Always call this method from your WatchKit extension’s main thread.

## See Also

- [func presentController(withName: String, context: Any?)](wkinterfacecontroller/presentcontroller(withname:context:).md)
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](wkinterfacecontroller/presentcontroller(withnames:contexts:).md)
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(withnamesandcontexts:).md)
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:).md)
  Presents an alert or action sheet over the current interface controller.
- [enum WKAlertControllerStyle](wkalertcontrollerstyle.md)
  Constants indicating the styles for standard system alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss())*