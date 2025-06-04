# addAnnotation(_:with:centerOffset:)

**Framework**: WatchKit  
**Kind**: method

Displays the specified image on top of the map.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func addAnnotation(_ location: CLLocationCoordinate2D, with image: UIImage?, centerOffset offset: CGPoint)
```

#### Discussion

This method adds an image to the map at the specified geographic location. The image is positioned just above the actual coordinate and centered on the coordinate horizontally.

## Parameters

- `location`: The location at which to display the image.
- `image`: The image to display at the specified location. If the value of this parameter is  , the map adds a red pin at the specified location.
- `offset`: The offset (in points) at which to place the center of the image. Normally, the center point of an annotation image is placed at the specified location on the map. Use this parameter to reposition the image relative to that point. Positive offset values move the annotation image down and to the right, while negative values move it up and to the left.

## See Also

- [func addAnnotation(CLLocationCoordinate2D, withImageNamed: String?, centerOffset: CGPoint)](wkinterfacemap/addannotation(_:withimagenamed:centeroffset:).md)
  Displays an image from the WatchKit app’s bundle on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, with: WKInterfaceMapPinColor)](wkinterfacemap/addannotation(_:with:).md)
  Adds a pin to the map at the specified location.
- [enum WKInterfaceMapPinColor](wkinterfacemappincolor.md)
  Constants for map pin colors.
- [func removeAllAnnotations()](wkinterfacemap/removeallannotations.md)
  Removes all annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:with:centeroffset:))*