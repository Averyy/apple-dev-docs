# addAnnotation(_:with:)

**Framework**: Watchkit  
**Kind**: method

Adds a pin to the map at the specified location.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func addAnnotation(_ location: CLLocationCoordinate2D, with pinColor: WKInterfaceMapPinColor)
```

## Overview

The pin is positioned so that the base of the pin sits on top of the specified coordinate.

## Parameters

- `location`: The location at which to display the pin.
- `pinColor`: The color of the pin. For a list of possible values, see  .

## See Also

- [func addAnnotation(CLLocationCoordinate2D, with: UIImage?, centerOffset: CGPoint)](addannotation(_:with:centeroffset:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:with:centeroffset:)))
- [func addAnnotation(CLLocationCoordinate2D, withImageNamed: String?, centerOffset: CGPoint)](addannotation(_:withimagenamed:centeroffset:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:withimagenamed:centeroffset:)))
- [enum WKInterfaceMapPinColor](wkinterfacemappincolor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor))
- [func removeAllAnnotations()](removeallannotations().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/removeallannotations()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:with:))*