# setShowsUserLocation(_:)

**Framework**: WatchKit  
**Kind**: method

Sets whether the map shows the user’s current location.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func setShowsUserLocation(_ showsUserLocation: Bool)
```

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) displays the users current location on the map. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

This property doesn’t indicate whether the user’s position is visible on the map. Setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) causes the map view to use the Core Location framework to track the user’s current location and display the location when it’s visible on screen. To keep the map centered on the user’s location, pass [`WKInterfaceMap.UserTrackingMode.follow`](wkinterfacemap/usertrackingmode/follow.md) to the [`setUserTrackingMode(_:animated:)`](wkinterfacemap/setusertrackingmode(_:animated:).md) method.

## Parameters

- `showsUserLocation`: A Boolean value that indicates whether the map shows the user’s current location.

## See Also

- [func setShowsUserHeading(Bool)](wkinterfacemap/setshowsuserheading(_:).md)
  Sets whether the map shows the user heading.
- [func setUserTrackingMode(WKInterfaceMap.UserTrackingMode, animated: Bool)](wkinterfacemap/setusertrackingmode(_:animated:).md)
  Sets the map’s tracking mode.
- [WKInterfaceMap.UserTrackingMode](wkinterfacemap/usertrackingmode.md)
  Modes for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserlocation(_:))*