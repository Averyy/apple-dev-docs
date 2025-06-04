# setVisibleMapRect(_:)

**Framework**: Watchkit  
**Kind**: method

Changes the map’s visible region to the specified map rectangle.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setVisibleMapRect(_ mapRect: MKMapRect)
```

## Overview

The method may adjust the specified map rectangle slightly to fit the available display space for the map. The adjusted region always includes the entire region you specified.

Changing the visible region may require the loading of additional map tiles to render the map. Loading tiles requires an active network connection.

## Parameters

- `mapRect`: The region to be displayed, specified as a map rectangle. The size of the rectangle provides an implicit zoom value for the map. For more information about the   type, see  .

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func setRegion(MKCoordinateRegion)](setregion(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setregion(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setvisiblemaprect(_:))*