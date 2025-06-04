# WKInterfaceMapPinColor

**Framework**: WatchKit  
**Kind**: enum

Constants for map pin colors.

**Availability**:
- watchOS ?+

## Declaration

```swift
enum WKInterfaceMapPinColor
```

## Topics

### Constants
- [WKInterfaceMapPinColor.red](wkinterfacemappincolor/red.md)
  A red pin.
- [WKInterfaceMapPinColor.green](wkinterfacemappincolor/green.md)
  A green pin.
- [WKInterfaceMapPinColor.purple](wkinterfacemappincolor/purple.md)
  A purple pin.
### Initializers
- [init?(rawValue: Int)](wkinterfacemappincolor/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](https://developer.apple.com/documentation/Swift/BitwiseCopyable)
- [Equatable](https://developer.apple.com/documentation/Swift/Equatable)
- [Hashable](https://developer.apple.com/documentation/Swift/Hashable)
- [RawRepresentable](https://developer.apple.com/documentation/Swift/RawRepresentable)
- [Sendable](https://developer.apple.com/documentation/Swift/Sendable)

## See Also

- [func addAnnotation(CLLocationCoordinate2D, with: UIImage?, centerOffset: CGPoint)](wkinterfacemap/addannotation(_:with:centeroffset:).md)
  Displays the specified image on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, withImageNamed: String?, centerOffset: CGPoint)](wkinterfacemap/addannotation(_:withimagenamed:centeroffset:).md)
  Displays an image from the WatchKit app’s bundle on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, with: WKInterfaceMapPinColor)](wkinterfacemap/addannotation(_:with:).md)
  Adds a pin to the map at the specified location.
- [func removeAllAnnotations()](wkinterfacemap/removeallannotations.md)
  Removes all annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor)*