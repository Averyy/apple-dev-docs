# setShowsUserHeading(_:)

**Framework**: WatchKit  
**Kind**: method

Sets whether the map shows the user heading.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func setShowsUserHeading(_ showsUserHeading: Bool)
```

#### Discussion

By default, the map doesn’t show the user’s heading.

> **Note**:  Calling this method has no effect unless the map is showing the user’s location. For more information, see [`setShowsUserLocation(_:)`](wkinterfacemap/setshowsuserlocation(_:).md).

 Calling this method has no effect unless the map is showing the user’s location. For more information, see [`setShowsUserLocation(_:)`](wkinterfacemap/setshowsuserlocation(_:).md).

## See Also

- [func setShowsUserLocation(Bool)](wkinterfacemap/setshowsuserlocation(_:).md)
  Sets whether the map shows the user’s current location.
- [func setUserTrackingMode(WKInterfaceMap.UserTrackingMode, animated: Bool)](wkinterfacemap/setusertrackingmode(_:animated:).md)
  Sets the map’s tracking mode.
- [WKInterfaceMap.UserTrackingMode](wkinterfacemap/usertrackingmode.md)
  Modes for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserheading(_:))*