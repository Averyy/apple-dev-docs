# presentController(withNames:contexts:)

**Framework**: Watchkit  
**Kind**: method

Presents a page-based interface modally.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func presentController(withNames names: [String], contexts: [Any]?)
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

## Overview

After calling this method, WatchKit loads and initializes the new interface controllers and animates them into position on top of the current interface controller. A modal interface slides up from the bottom of the screen and completely cover the previous interface. WatchKit displays the first interface controller in the `names` array initially. The user can navigate to the other interfaces by swiping horizontally.

The title of the modal interface is set to the string `Cancel` by default. Change the title using the [`setTitle(_:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/settitle(_:)) method. Tapping the title dismisses the interface automatically. To dismiss the interface programmatically, call the [`dismiss()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss()) method.

Always call this method from your WatchKit extension’s main thread.

## Parameters

- `names`: An array of strings, each of which contains the name of an interface controller you want to display in the page-based interface. In your storyboard, the name of an interface controller is stored in the object’s Identifier property, which is located in the attributes inspector. The order of the strings in the array is used to set the order of the corresponding interface controllers. This parameter must not be   or an empty array.
- `contexts`: Each object in the array is passed to the interface controller at the same index in the   parameter.

## See Also

- [func presentController(withName: String, context: Any?)](presentcontroller(withname:context:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withname:context:)))
- [func presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](presentcontroller(withnamesandcontexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnamesandcontexts:)))
- [func presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](presentalert(withtitle:message:preferredstyle:actions:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentalert(withtitle:message:preferredstyle:actions:)))
- [enum WKAlertControllerStyle](wkalertcontrollerstyle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle))
- [func dismiss()](dismiss().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismiss()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentcontroller(withnames:contexts:))*