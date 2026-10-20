# setVisibleMapRect(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Changes the map’s visible region to the specified map rectangle.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setVisibleMapRect(_ mapRect: MKMapRect)
```

```objc
- (void) setVisibleMapRect:(MKMapRect) mapRect;
```

#### Discussion

The method may adjust the specified map rectangle slightly to fit the available display space for the map. The adjusted region always includes the entire region you specified.

Changing the visible region may require the loading of additional map tiles to render the map. Loading tiles requires an active network connection.

## Parameters

- `mapRect`: The region to be displayed, specified as a map rectangle. The size of the rectangle provides an implicit zoom value for the map. For more information about the [`MKMapRect`](../../MapKit/mkmaprect.md) type, see [MapKit](../../MapKit/MapKit.md).

## See Also

### Related Documentation
- [App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
### Specifying the Map Region
- [func setRegion(MKCoordinateRegion)](./setregion%28_%29.md)
  Changes the map’s visible region to the specified coordinate region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setvisiblemaprect(_:))*