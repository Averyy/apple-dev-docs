# dismiss()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the current interface controller from the screen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func dismiss()
```

```objc
- (void) dismissController;
```

#### Discussion

Call this method when you want to dismiss an interface controller that you presented modally. Always call this method from your WatchKit extension’s main thread.

## See Also

### Presenting interface controllers modally
- [func presentController(withName: String, context: Any?)](./presentcontroller%28withname,context%29.md)
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](./presentcontroller%28withnames,contexts%29.md)
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](./presentcontroller%28withnamesandcontexts%29.md)
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](./presentalert%28withtitle,message,preferredstyle,actions%29.md)
  Presents an alert or action sheet over the current interface controller.
- [enum WKAlertControllerStyle](../wkalertcontrollerstyle.md)
  Constants indicating the styles for standard system alerts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss())*