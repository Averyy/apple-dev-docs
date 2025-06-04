# setRegion(_:)

**Framework**: WatchKit  
**Kind**: method

Changes the map’s visible region to the specified coordinate region.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setRegion(_ coordinateRegion: MKCoordinateRegion)
```

#### Discussion

This method changes the currently visible region of the map. The method may adjust the map rectangle slightly to fit the available display space for the map. The adjusted region always includes the entire region you specified.

Changing the visible region may require the loading of additional map tiles to render the map. Loading tiles requires an active network connection.

## Parameters

- `coordinateRegion`: The new region of the map to be displayed. The span value of this parameter provides an implicit zoom value for the map. For more information about the   type, see  .

## See Also

- [func setVisibleMapRect(MKMapRect)](wkinterfacemap/setvisiblemaprect(_:).md)
  Changes the map’s visible region to the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setregion(_:))*