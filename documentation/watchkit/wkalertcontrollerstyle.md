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
- [WKAlertControllerStyle.alert](alert.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle/alert))
  An alert sheet with stacked buttons. The alert sheet includes a default Cancel button at the bottom of the sheet. You can add other buttons, which are placed above the Cancel button.
- [WKAlertControllerStyle.sideBySideButtonsAlert](sidebysidebuttonsalert.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle/sidebysidebuttonsalert))
  An alert sheet with side-by-side buttons.
- [WKAlertControllerStyle.actionSheet](actionsheet.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle/actionsheet))
  An action sheet style. Action sheets are modal sheets that can be dismissed using the Cancel button in the top-left corner of the sheet. You can also add one or two custom buttons to perform related tasks.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [func presentController(withName: String, context: Any?)](presentcontroller(withname:context:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withname:context:)))
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](presentcontroller(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnames:contexts:)))
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](presentcontroller(withnamesandcontexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnamesandcontexts:)))
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](presentalert(withtitle:message:preferredstyle:actions:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:)))
  Presents an alert or action sheet over the current interface controller.
- [func dismiss()](dismiss().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss()))
  Dismisses the current interface controller from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle)*