# WKInterfaceMapPinColor

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Constants for map pin colors.

**Availability**:
- watchOS

## Declaration

```swift
enum WKInterfaceMapPinColor
```

```c
enum WKInterfaceMapPinColor : NSInteger;
```

## Topics

### Constants
- [WKInterfaceMapPinColor.red](./wkinterfacemappincolor/red.md)
  A red pin.
- [WKInterfaceMapPinColor.green](./wkinterfacemappincolor/green.md)
  A green pin.
- [WKInterfaceMapPinColor.purple](./wkinterfacemappincolor/purple.md)
  A purple pin.
### Initializers
- [init?(rawValue: Int)](./wkinterfacemappincolor/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing Map Annotations
- [func addAnnotation(CLLocationCoordinate2D, with: UIImage?, centerOffset: CGPoint)](./wkinterfacemap/addannotation%28_,with,centeroffset%29.md)
  Displays the specified image on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, withImageNamed: String?, centerOffset: CGPoint)](./wkinterfacemap/addannotation%28_,withimagenamed,centeroffset%29.md)
  Displays an image from the WatchKit app’s bundle on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, with: WKInterfaceMapPinColor)](./wkinterfacemap/addannotation%28_,with%29.md)
  Adds a pin to the map at the specified location.
- [func removeAllAnnotations()](./wkinterfacemap/removeallannotations%28%29.md)
  Removes all annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor)*