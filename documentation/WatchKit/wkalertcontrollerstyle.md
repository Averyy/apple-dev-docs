# WKAlertControllerStyle

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the styles for standard system alerts.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKAlertControllerStyle
```

```c
enum WKAlertControllerStyle : NSInteger;
```

## Topics

### Constants
- [WKAlertControllerStyle.alert](./wkalertcontrollerstyle/alert.md)
  An alert sheet with stacked buttons. The alert sheet includes a default Cancel button at the bottom of the sheet. You can add other buttons, which are placed above the Cancel button.
- [WKAlertControllerStyle.sideBySideButtonsAlert](./wkalertcontrollerstyle/sidebysidebuttonsalert.md)
  An alert sheet with side-by-side buttons.
- [WKAlertControllerStyle.actionSheet](./wkalertcontrollerstyle/actionsheet.md)
  An action sheet style. Action sheets are modal sheets that can be dismissed using the Cancel button in the top-left corner of the sheet. You can also add one or two custom buttons to perform related tasks.
### Initializers
- [init?(rawValue: Int)](./wkalertcontrollerstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Presenting interface controllers modally
- [func presentController(withName: String, context: Any?)](./wkinterfacecontroller/presentcontroller%28withname,context%29.md)
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](./wkinterfacecontroller/presentcontroller%28withnames,contexts%29.md)
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](./wkinterfacecontroller/presentcontroller%28withnamesandcontexts%29.md)
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](./wkinterfacecontroller/presentalert%28withtitle,message,preferredstyle,actions%29.md)
  Presents an alert or action sheet over the current interface controller.
- [func dismiss()](./wkinterfacecontroller/dismiss%28%29.md)
  Dismisses the current interface controller from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle)*