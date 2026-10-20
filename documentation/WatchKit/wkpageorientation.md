# WKPageOrientation

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Scrolling orientations for page-based interfaces.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
enum WKPageOrientation
```

```c
enum WKPageOrientation : NSInteger;
```

## Topics

### Enumeration Cases
- [WKPageOrientation.horizontal](./wkpageorientation/horizontal.md)
  A horizontal page-based scrolling orientation.
- [WKPageOrientation.vertical](./wkpageorientation/vertical.md)
  A vertical page-based scrolling orientation.
### Initializers
- [init?(rawValue: Int)](./wkpageorientation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Navigating a page-based interface
- [class func reloadRootPageControllers(withNames: [String], contexts: [Any]?, orientation: WKPageOrientation, pageIndex: Int)](./wkinterfacecontroller/reloadrootpagecontrollers%28withnames,contexts,orientation,pageindex%29.md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface for the given scrolling orientation.
- [class func reloadRootControllers(withNamesAndContexts: [(name: String, context: AnyObject)])](./wkinterfacecontroller/reloadrootcontrollers%28withnamesandcontexts%29.md)
  Loads the specified interface controllers and rebuilds the app’s page-based interface.
- [func becomeCurrentPage()](./wkinterfacecontroller/becomecurrentpage%28%29.md)
  Displays the interface controller in the page-based interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkpageorientation)*