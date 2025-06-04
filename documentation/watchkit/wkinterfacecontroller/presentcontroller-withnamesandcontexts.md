# presentController(withNamesAndContexts:)

**Framework**: WatchKit  
**Kind**: method

Presents a page-based interface modally.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- watchOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func presentController(withNamesAndContexts namesAndContexts: [(name: String, context: AnyObject)])
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

#### Discussion

After calling this method, the WatchKit extension loads and initializes the new interface controllers and animates them into position on top of the current interface controller. A modal interface slides up from the bottom of the screen and completely covers the previous interface. The watchOS app displays the first interface controller in the `names` array initially. The user can navigate to the other interfaces by swiping horizontally.

The title of the modal interface is set to the string `Cancel` by default. Change the title using the [`setTitle(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/settitle(_:)) method. Tapping the title dismisses the interface automatically. To dismiss the interface programmatically, call the [`dismiss()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss()) method.

Always call this method from your WatchKit extension’s main thread.

## Parameters

- `namesAndContexts`: An array of tuples. Each tuple must contain the following named elements:

## See Also

- [func presentController(withName: String, context: Any?)](presentcontroller(withname:context:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withname:context:)))
  Presents a single interface controller modally.
- [func presentController(withNames: [String], contexts: [Any]?)](presentcontroller(withnames:contexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnames:contexts:)))
  Presents a page-based interface modally.
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](presentalert(withtitle:message:preferredstyle:actions:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:)))
  Presents an alert or action sheet over the current interface controller.
- [enum WKAlertControllerStyle](wkalertcontrollerstyle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle))
  Constants indicating the styles for standard system alerts.
- [func dismiss()](dismiss().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss()))
  Dismisses the current interface controller from the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnamesandcontexts:))*