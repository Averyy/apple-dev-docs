# WKInterfaceMap.UserTrackingMode

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Modes for tracking the user’s location on the map.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
enum UserTrackingMode
```

```c
enum WKInterfaceMapUserTrackingMode : NSInteger;
```

## Topics

### Tracking Modes
- [WKInterfaceMap.UserTrackingMode.follow](./usertrackingmode/follow.md)
  The map scrolls to follow the user as they move.
- [WKInterfaceMap.UserTrackingMode.none](./usertrackingmode/none.md)
  The map remains stationary, even if the user moves off the map.
- [WKInterfaceMap.UserTrackingMode.follow](./usertrackingmode/follow.md)
  The map scrolls to follow the user as they move.
- [WKInterfaceMap.UserTrackingMode.none](./usertrackingmode/none.md)
  The map remains stationary, even if the user moves off the map.
### Initializers
- [init?(rawValue: Int)](./usertrackingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Displaying the User’s Location
- [func setShowsUserLocation(Bool)](./setshowsuserlocation%28_%29.md)
  Sets whether the map shows the user’s current location.
- [func setShowsUserHeading(Bool)](./setshowsuserheading%28_%29.md)
  Sets whether the map shows the user heading.
- [func setUserTrackingMode(WKInterfaceMap.UserTrackingMode, animated: Bool)](./setusertrackingmode%28_,animated%29.md)
  Sets the map’s tracking mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/usertrackingmode)*