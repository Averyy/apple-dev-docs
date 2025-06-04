# setUserTrackingMode(_:animated:)

**Framework**: Watchkit  
**Kind**: method

Sets the map’s tracking mode.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
func setUserTrackingMode(_ mode: WKInterfaceMap.UserTrackingMode, animated: Bool)
```

## Overview

By default, the tracking mode is [`WKInterfaceMap.UserTrackingMode.none`](https://developer.apple.com/documentation/watchkit/wkinterfacemap/usertrackingmode/none).

Setting the tracking mode to [`WKInterfaceMap.UserTrackingMode.follow`](https://developer.apple.com/documentation/watchkit/wkinterfacemap/usertrackingmode/follow) causes the map to center on the user’s location and begin tracking the user. If the map is zoomed out, the map view automatically zooms in on the user’s location, effectively changing the current visible region.

## Parameters

- `mode`: The desired tracking mode. For a complete list of valid tracking modes, see  .
- `animated`: A Boolean value that indicates whether the map animates the change to the tracking mode.

## See Also

- [func setShowsUserLocation(Bool)](setshowsuserlocation(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserlocation(_:)))
- [func setShowsUserHeading(Bool)](setshowsuserheading(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserheading(_:)))
- [WKInterfaceMap.UserTrackingMode](usertrackingmode.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/usertrackingmode))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setusertrackingmode(_:animated:))*