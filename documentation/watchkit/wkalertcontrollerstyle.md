# WKAlertControllerStyle

**Framework**: WatchKit  
**Kind**: enum

Constants indicating the styles for standard system alerts.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKAlertControllerStyle
```

## Topics

### Constants
- [WKAlertControllerStyle.alert](wkalertcontrollerstyle/alert.md)
  An alert sheet with stacked buttons. The alert sheet includes a default Cancel button at the bottom of the sheet. You can add other buttons, which are placed above the Cancel button.
- [WKAlertControllerStyle.sideBySideButtonsAlert](wkalertcontrollerstyle/sidebysidebuttonsalert.md)
  An alert sheet with side-by-side buttons.
- [WKAlertControllerStyle.actionSheet](wkalertcontrollerstyle/actionsheet.md)
  An action sheet style. Action sheets are modal sheets that can be dismissed using the Cancel button in the top-left corner of the sheet. You can also add one or two custom buttons to perform related tasks.
### Initializers
- [init?(rawValue: Int)](wkalertcontrollerstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [RawRepresentable](https://developer.apple.com/documentation/Swift/RawRepresentable)
- [Sendable](https://developer.apple.com/documentation/Swift/Sendable)

## See Also

- [func presentController(withName: String, context: Any?)](wkinterfacecontroller/presentcontroller(withname:context:).md)
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](wkinterfacecontroller/presentcontroller(withnames:contexts:).md)
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(withnamesandcontexts:).md)
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:).md)
  Presents an alert or action sheet over the current interface controller.
- [func dismiss()](wkinterfacecontroller/dismiss.md)
  Dismisses the current interface controller from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle)*