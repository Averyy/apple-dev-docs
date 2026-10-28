# setShowsUserLocation(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the map shows the user’s current location.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func setShowsUserLocation(_ showsUserLocation: Bool)
```

```objc
- (void) setShowsUserLocation:(BOOL) showsUserLocation;
```

## Discussion

Setting this property to [`true`](../../Swift/true.md) displays the users current location on the map. The default value is [`false`](../../Swift/false.md).

This property doesn’t indicate whether the user’s position is visible on the map. Setting this property to [`true`](../../Swift/true.md) causes the map view to use the Core Location framework to track the user’s current location and display the location when it’s visible on screen. To keep the map centered on the user’s location, pass [`WKInterfaceMap.UserTrackingMode.follow`](./usertrackingmode/follow.md) to the [`setUserTrackingMode(_:animated:)`](./setusertrackingmode%28_,animated%29.md) method.

## Parameters

- `showsUserLocation`: A Boolean value that indicates whether the map shows the user’s current location.

## See Also

### Displaying the User’s Location
- [func setShowsUserHeading(Bool)](./setshowsuserheading%28_%29.md)
  Sets whether the map shows the user heading.
- [func setUserTrackingMode(WKInterfaceMap.UserTrackingMode, animated: Bool)](./setusertrackingmode%28_,animated%29.md)
  Sets the map’s tracking mode.
- [WKInterfaceMap.UserTrackingMode](./usertrackingmode.md)
  Modes for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserlocation(_:))*