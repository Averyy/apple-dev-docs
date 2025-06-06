# reloadRootPageControllers(withNames:contexts:orientation:pageIndex:)

**Framework**: Watchkit  
**Kind**: method

Loads the specified interface controllers and rebuilds the app’s page-based interface for the given scrolling orientation.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
class func reloadRootPageControllers(withNames names: [String], contexts: [Any]?, orientation: WKPageOrientation, pageIndex: Int)
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md)

#### Discussion

Call this method to create or modify your app’s page-based interface:

-  Use this method to customize the set of pages you want displayed, and to set the scrolling orientation.
-  Use this method to change the active set of pages or the orientation, adding or removing pages as needed.

## Parameters

- `names`: An array of   objects, each of which contains the identifier of an interface controller in your storyboard file. The order of the identifiers in the array defines the order of the corresponding interface controllers in the page-based interface.
- `contexts`: An array of objects of type  . Use this parameter to pass context objects to each of the interface controllers loaded into the page-based interface. The first object in the array is passed to the first interface controller, the second object is passed to the second interface controller, and so on.
- `orientation`: The scrolling orientation for the page-based interface. For a list of valid values, see  .
- `pageIndex`: The index of the page that the system displays in the page-based interface.

## See Also

- [enum WKPageOrientation](wkpageorientation.md)
  Scrolling orientations for page-based interfaces.
- [class func reloadRootControllers(withNamesAndContexts: [(name: String, context: AnyObject)])](wkinterfacecontroller/reloadrootcontrollers(withnamesandcontexts:).md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func becomeCurrentPage()](wkinterfacecontroller/becomecurrentpage.md)
  Displays the interface controller in the page-based interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:))*