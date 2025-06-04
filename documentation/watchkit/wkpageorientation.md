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
- [WKPageOrientation.horizontal](horizontal.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpageorientation/horizontal))
  A horizontal page-based scrolling orientation.
- [WKPageOrientation.vertical](vertical.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpageorientation/vertical))
  A vertical page-based scrolling orientation.
### Initializers
- [init?(rawValue: Int)](init(rawvalue:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpageorientation/init(rawvalue:)))

## Relationships

### Conforms To
- BitwiseCopyable ([Apple Docs](https://developer.apple.com/documentation/Swift/BitwiseCopyable))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- RawRepresentable ([Apple Docs](https://developer.apple.com/documentation/Swift/RawRepresentable))
- Sendable ([Apple Docs](https://developer.apple.com/documentation/Swift/Sendable))

## See Also

- [class func reloadRootPageControllers(withNames: [String], contexts: [Any]?, orientation: WKPageOrientation, pageIndex: Int)](reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootpagecontrollers(withnames:contexts:orientation:pageindex:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface for the given scrolling orientation.
- [class func reloadRootControllers(withNamesAndContexts: [(name: String, context: AnyObject)])](reloadrootcontrollers(withnamesandcontexts:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/reloadrootcontrollers(withnamesandcontexts:)))
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func becomeCurrentPage()](becomecurrentpage().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/becomecurrentpage()))
  Displays the interface controller in the page-based interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpageorientation)*