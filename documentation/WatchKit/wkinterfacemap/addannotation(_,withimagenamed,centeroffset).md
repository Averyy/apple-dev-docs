# addAnnotation(_:withImageNamed:centerOffset:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Displays an image from the WatchKit app’s bundle on top of the map.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func addAnnotation(_ location: CLLocationCoordinate2D, withImageNamed name: String?, centerOffset offset: CGPoint)
```

```objc
- (void) addAnnotation:(CLLocationCoordinate2D) location withImageNamed:(NSString *) name centerOffset:(CGPoint) offset;
```

## Discussion

This method adds an image to the map at the specified geographic location. The image is positioned just above the actual coordinate and centered on the coordinate horizontally.

## Parameters

- `location`: The location at which to display the image.
- `name`: The name of the image to be loaded from the WatchKit app’s bundle or device-side cache. For images in the bundle, specify the filename of the image and include the filename extension in the name. If no image with the specified name can be found in the WatchKit app bundle, WatchKit displays a red pin at the location.
- `offset`: The offset (in points) at which to place the center of the image. Normally, the center point of an annotation image is placed at the specified location on the map. Use this parameter to reposition the image relative to that point.

## See Also

### Managing Map Annotations
- [func addAnnotation(CLLocationCoordinate2D, with: UIImage?, centerOffset: CGPoint)](./addannotation%28_,with,centeroffset%29.md)
  Displays the specified image on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, with: WKInterfaceMapPinColor)](./addannotation%28_,with%29.md)
  Adds a pin to the map at the specified location.
- [enum WKInterfaceMapPinColor](../wkinterfacemappincolor.md)
  Constants for map pin colors.
- [func removeAllAnnotations()](./removeallannotations%28%29.md)
  Removes all annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:withimagenamed:centeroffset:))*