# setUserTrackingMode(_:animated:)

**Framework**: WatchKit  
**Kind**: method

Sets the map’s tracking mode.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func setUserTrackingMode(_ mode: WKInterfaceMap.UserTrackingMode, animated: Bool)
```

#### Discussion

By default, the tracking mode is [`WKInterfaceMap.UserTrackingMode.none`](wkinterfacemap/usertrackingmode/none.md).

Setting the tracking mode to [`WKInterfaceMap.UserTrackingMode.follow`](wkinterfacemap/usertrackingmode/follow.md) causes the map to center on the user’s location and begin tracking the user. If the map is zoomed out, the map view automatically zooms in on the user’s location, effectively changing the current visible region.

## Parameters

- `mode`: The desired tracking mode. For a complete list of valid tracking modes, see  .
- `animated`: A Boolean value that indicates whether the map animates the change to the tracking mode.

## See Also

- [func setShowsUserLocation(Bool)](wkinterfacemap/setshowsuserlocation(_:).md)
  Sets whether the map shows the user’s current location.
- [func setShowsUserHeading(Bool)](wkinterfacemap/setshowsuserheading(_:).md)
  Sets whether the map shows the user heading.
- [WKInterfaceMap.UserTrackingMode](wkinterfacemap/usertrackingmode.md)
  Modes for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setusertrackingmode(_:animated:))*