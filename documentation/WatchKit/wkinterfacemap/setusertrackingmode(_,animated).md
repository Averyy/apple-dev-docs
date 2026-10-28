# setUserTrackingMode(_:animated:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the map’s tracking mode.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func setUserTrackingMode(_ mode: WKInterfaceMap.UserTrackingMode, animated: Bool)
```

```objc
- (void) setUserTrackingMode:(WKInterfaceMapUserTrackingMode) mode animated:(BOOL) animated;
```

## Discussion

By default, the tracking mode is [`WKInterfaceMap.UserTrackingMode.none`](./usertrackingmode/none.md).

Setting the tracking mode to [`WKInterfaceMap.UserTrackingMode.follow`](./usertrackingmode/follow.md) causes the map to center on the user’s location and begin tracking the user. If the map is zoomed out, the map view automatically zooms in on the user’s location, effectively changing the current visible region.

## Parameters

- `mode`: The desired tracking mode. For a complete list of valid tracking modes, see [`WKInterfaceMap.UserTrackingMode`](./usertrackingmode.md).
- `animated`: A Boolean value that indicates whether the map animates the change to the tracking mode.

## See Also

### Displaying the User’s Location
- [func setShowsUserLocation(Bool)](./setshowsuserlocation%28_%29.md)
  Sets whether the map shows the user’s current location.
- [func setShowsUserHeading(Bool)](./setshowsuserheading%28_%29.md)
  Sets whether the map shows the user heading.
- [WKInterfaceMap.UserTrackingMode](./usertrackingmode.md)
  Modes for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setusertrackingmode(_:animated:))*