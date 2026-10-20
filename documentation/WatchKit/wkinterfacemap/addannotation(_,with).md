# addAnnotation(_:with:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Adds a pin to the map at the specified location.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func addAnnotation(_ location: CLLocationCoordinate2D, with pinColor: WKInterfaceMapPinColor)
```

```objc
- (void) addAnnotation:(CLLocationCoordinate2D) location withPinColor:(WKInterfaceMapPinColor) pinColor;
```

#### Discussion

The pin is positioned so that the base of the pin sits on top of the specified coordinate.

## Parameters

- `location`: The location at which to display the pin.
- `pinColor`: The color of the pin. For a list of possible values, see [`WKInterfaceMapPinColor`](../wkinterfacemappincolor.md).

## See Also

### Managing Map Annotations
- [func addAnnotation(CLLocationCoordinate2D, with: UIImage?, centerOffset: CGPoint)](./addannotation%28_,with,centeroffset%29.md)
  Displays the specified image on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, withImageNamed: String?, centerOffset: CGPoint)](./addannotation%28_,withimagenamed,centeroffset%29.md)
  Displays an image from the WatchKit app’s bundle on top of the map.
- [enum WKInterfaceMapPinColor](../wkinterfacemappincolor.md)
  Constants for map pin colors.
- [func removeAllAnnotations()](./removeallannotations%28%29.md)
  Removes all annotations from the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:with:))*