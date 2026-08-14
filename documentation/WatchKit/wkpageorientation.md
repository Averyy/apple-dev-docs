# WKPageOrientation

**Framework**: WatchKit  
**Kind**: enum

Scrolling orientations for page-based interfaces.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
enum WKPageOrientation
```

## Topics

### Enumeration Cases
- [WKPageOrientation.horizontal](wkpageorientation/horizontal.md)
  A horizontal page-based scrolling orientation.
- [WKPageOrientation.vertical](wkpageorientation/vertical.md)
  A vertical page-based scrolling orientation.
### Initializers
- [init?(rawValue: Int)](wkpageorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class func reloadRootPageControllers(withNames: [String], contexts: [Any]?, orientation: WKPageOrientation, pageIndex: Int)](wkinterfacecontroller/reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:).md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface for the given scrolling orientation.
- [class func reloadRootControllers(withNamesAndContexts: [(name: String, context: AnyObject)])](wkinterfacecontroller/reloadrootcontrollers(withnamesandcontexts:).md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func becomeCurrentPage()](wkinterfacecontroller/becomecurrentpage.md)
  Displays the interface controller in the page-based interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpageorientation)*