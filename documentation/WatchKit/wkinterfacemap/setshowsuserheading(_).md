# setShowsUserHeading(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the map shows the user heading.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func setShowsUserHeading(_ showsUserHeading: Bool)
```

```objc
- (void) setShowsUserHeading:(BOOL) showsUserHeading;
```

## Discussion

By default, the map doesn’t show the user’s heading.

> **Note**:  Calling this method has no effect unless the map is showing the user’s location. For more information, see [`setShowsUserLocation(_:)`](./setshowsuserlocation%28_%29.md).

## See Also

### Displaying the User’s Location
- [func setShowsUserLocation(Bool)](./setshowsuserlocation%28_%29.md)
  Sets whether the map shows the user’s current location.
- [func setUserTrackingMode(WKInterfaceMap.UserTrackingMode, animated: Bool)](./setusertrackingmode%28_,animated%29.md)
  Sets the map’s tracking mode.
- [WKInterfaceMap.UserTrackingMode](./usertrackingmode.md)
  Modes for tracking the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserheading(_:))*