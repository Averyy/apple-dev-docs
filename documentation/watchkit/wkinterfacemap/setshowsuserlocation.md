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

Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) displays the users current location on the map. The default value is [`false`](https://developer.apple.com/documentation/swift/false).

This property doesn’t indicate whether the user’s position is visible on the map. Setting this property to [`true`](https://developer.apple.com/documentation/swift/true) causes the map view to use the Core Location framework to track the user’s current location and display the location when it’s visible on screen. To keep the map centered on the user’s location, pass [`WKInterfaceMap.UserTrackingMode.follow`](https://developer.apple.com/documentation/watchkit/wkinterfacemap/usertrackingmode/follow) to the [`setUserTrackingMode(_:animated:)`](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setusertrackingmode(_:animated:)) method.

## Parameters

- `showsUserLocation`: A Boolean value that indicates whether the map shows the user’s current location.

## See Also

- [func setShowsUserHeading(Bool)](setshowsuserheading(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserheading(_:)))
  Sets whether the map shows the user heading.
- [func setUserTrackingMode(WKInterfaceMap.UserTrackingMode, animated: Bool)](setusertrackingmode(_:animated:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setusertrackingmode(_:animated:)))
  Sets the map’s tracking mode.
- [WKInterfaceMap.UserTrackingMode](usertrackingmode.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/usertrackingmode))
  Modes for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserlocation(_:))*