# reloadRootControllers(withNamesAndContexts:)

**Framework**: WatchKit  
**Kind**: method

Loads the specified interface controllers and rebuilds the app’s page-based interface.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- watchOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class func reloadRootControllers(withNamesAndContexts namesAndContexts: [(name: String, context: AnyObject)])
```

#### Discussion

Call this method to reload the pages in your app’s page-based interface:

-  Use this method to customize the set of pages you want displayed.
-  Use it to change the active set of pages, adding or removing pages as needed.

## Parameters

- `namesAndContexts`: An array of tuples. Each tuple must contain the following named elements:

## See Also

- [class func reloadRootPageControllers(withNames: [String], contexts: [Any]?, orientation: WKPageOrientation, pageIndex: Int)](reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface for the given scrolling orientation.
- [enum WKPageOrientation](wkpageorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpageorientation))
  Scrolling orientations for page-based interfaces.
- [func becomeCurrentPage()](becomecurrentpage().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/becomecurrentpage()))
  Displays the interface controller in the page-based interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnamesandcontexts:))*