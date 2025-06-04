# presentAlert(withTitle:message:preferredStyle:actions:)

**Framework**: WatchKit  
**Kind**: method

Presents an alert or action sheet over the current interface controller.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func presentAlert(withTitle title: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

Use action and alert sheets to interrupt the current workflow temporarily and display a message to the user. The sheet itself places a blurred layer over your interface controller and displays the title and message text on top of that. If you provided action buttons, those buttons are displayed at the bottom of the sheet. When the user taps one of your buttons, WatchKit dismisses the sheet automatically and executes your button’s handler block. You can also dismiss the sheet programmatically by calling the [`dismiss()`](wkinterfacecontroller/dismiss().md) method.

For the [`WKAlertControllerStyle.actionSheet`](wkalertcontrollerstyle/actionsheet.md) style, this method automatically includes a localized Cancel button at the top of the sheet if you do not specify one in the `actions` array. If one of your buttons is configured to be a Cancel button—that is, you initialize it with the [`WKAlertActionStyle.cancel`](wkalertactionstyle/cancel.md) style—the sheet displays your button’s text in place of the default Cancel button text.

Only one action or alert sheet may be visible at a time. If you call this method and a sheet is already visible, this method dismisses the previous sheet before displaying the new one.

## Parameters

- `title`: The title of the alert. Use this string to convey the intent of your alert.
- `message`: The text to display for the body of the alert. Use this string to display secondary information related to the alert.
- `preferredStyle`: The preferred style of the sheet. Use the available constants to specify the type of sheet (alert or action) to display and the configuration of the buttons.
- `actions`: An array of   objects that describe the custom buttons to display. The array must contain at least one button. For the   style, the array must contain exactly two buttons. The block associated with each button should dismiss the sheet in addition to performing any other tasks.

## See Also

- [func presentController(withName: String, context: Any?)](wkinterfacecontroller/presentcontroller(withname:context:).md)
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](wkinterfacecontroller/presentcontroller(withnames:contexts:).md)
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(withnamesandcontexts:).md)
  Presents a page-based interface modally.
- [enum WKAlertControllerStyle](wkalertcontrollerstyle.md)
  Constants indicating the styles for standard system alerts.
- [func dismiss()](wkinterfacecontroller/dismiss.md)
  Dismisses the current interface controller from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:))*