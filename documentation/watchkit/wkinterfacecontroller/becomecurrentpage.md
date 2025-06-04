# becomeCurrentPage()

**Framework**: WatchKit  
**Kind**: method

Displays the interface controller in the page-based interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func becomeCurrentPage()
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

#### Discussion

Use this method to make the current interface controller become the current page of a page-based interface. The current interface controller must be installed in the page-based interface. After calling this method, WatchKit animates the interface controller into view.

Always call this method from your WatchKit extension’s main thread.

## See Also

- [class func reloadRootPageControllers(withNames: [String], contexts: [Any]?, orientation: WKPageOrientation, pageIndex: Int)](reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface for the given scrolling orientation.
- [enum WKPageOrientation](wkpageorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpageorientation))
  Scrolling orientations for page-based interfaces.
- [class func reloadRootControllers(withNamesAndContexts: [(name: String, context: AnyObject)])](reloadrootcontrollers(withnamesandcontexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnamesandcontexts:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/becomecurrentpage())*