# presentController(withName:context:)

**Framework**: WatchKit  
**Kind**: method

Presents a single interface controller modally.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func presentController(withName name: String, context: Any?)
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

After calling this method, the WatchKit extension loads and initializes the new interface controller and animates it into position on top of the current interface controller. A modal interface slides up from the bottom of the screen and completely covers the previous interface.

The title of the modal interface is set to the string `Cancel` by default. Change the title using the [`setTitle(_:)`](wkinterfacecontroller/settitle(_:).md) method. Tapping the title dismisses the interface automatically. To dismiss the interface programmatically, call the [`dismiss()`](wkinterfacecontroller/dismiss().md) method.

Always call this method from your WatchKit extension’s main thread.

## Parameters

- `name`: The name of the interface controller you want to display. In your storyboard, the name of an interface controller is stored in the object’s Identifier property, which is located in the attributes inspector. This parameter must not be  .
- `context`: An object to pass to the new interface controller. Use the object in this parameter to communicate important information to the new interface controller, such as the data to display or any relevant state information. You may specify   for this parameter, but doing so is not recommended.

## See Also

- [func presentController(withNames: [String], contexts: [Any]?)](wkinterfacecontroller/presentcontroller(withnames:contexts:).md)
  Presents a page-based interface modally.
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](wkinterfacecontroller/presentcontroller(withnamesandcontexts:).md)
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:).md)
  Presents an alert or action sheet over the current interface controller.
- [enum WKAlertControllerStyle](wkalertcontrollerstyle.md)
  Constants indicating the styles for standard system alerts.
- [func dismiss()](wkinterfacecontroller/dismiss.md)
  Dismisses the current interface controller from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withname:context:))*