# WKInterfaceMap

**Framework**: WatchKit  
**Kind**: class

An interface element that displays a noninteractive map for the location you specify.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceMap
```

#### Overview

You can configure Maps dynamically from your interface controller. Use the methods of [`WKInterfaceMap`](https://developer.apple.com/documentation/watchkit/wkinterfacemap) to specify the visible region of the map and to add any annotations or points of interest. Tapping the map launches the Maps app on the user’s Apple Watch and displays the corresponding location.

Using a map object, you specify a geographic region to display and you can optionally add annotations to the surface of the map. Maps display annotations as images on top of the map content. You can use custom images or display the built-in pin images. Maps can display no more than five annotations at a time.

Don’t subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a map object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen map.

The Apple Watch must have an active network connection to download map tiles.

##### Configure the Map in Interface Builder

In Xcode, you can configure information about your map from your storyboard file. The map interface object has an Enabled attribute that appears as a checkbox in the Attributes inspector. When you enable the map interface object in this checkbox, tapping the map launches the Maps app and displays the current selected location.

## Topics

### Specifying the Map Region
- [func setVisibleMapRect(MKMapRect)](setvisiblemaprect(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setvisiblemaprect(_:)))
  Changes the map’s visible region to the specified map rectangle.
- [func setRegion(MKCoordinateRegion)](setregion(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setregion(_:)))
  Changes the map’s visible region to the specified coordinate region.
### Managing Map Annotations
- [func addAnnotation(CLLocationCoordinate2D, with: UIImage?, centerOffset: CGPoint)](addannotation(_:with:centeroffset:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:with:centeroffset:)))
  Displays the specified image on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, withImageNamed: String?, centerOffset: CGPoint)](addannotation(_:withimagenamed:centeroffset:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:withimagenamed:centeroffset:)))
  Displays an image from the WatchKit app’s bundle on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, with: WKInterfaceMapPinColor)](addannotation(_:with:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/addannotation(_:with:)))
  Adds a pin to the map at the specified location.
- [enum WKInterfaceMapPinColor](wkinterfacemappincolor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor))
  Constants for map pin colors.
- [func removeAllAnnotations()](removeallannotations().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/removeallannotations()))
  Removes all annotations from the map.
### Displaying the User’s Location
- [func setShowsUserLocation(Bool)](setshowsuserlocation(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserlocation(_:)))
  Sets whether the map shows the user’s current location.
- [func setShowsUserHeading(Bool)](setshowsuserheading(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setshowsuserheading(_:)))
  Sets whether the map shows the user heading.
- [func setUserTrackingMode(WKInterfaceMap.UserTrackingMode, animated: Bool)](setusertrackingmode(_:animated:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/setusertrackingmode(_:animated:)))
  Sets the map’s tracking mode.
- [WKInterfaceMap.UserTrackingMode](usertrackingmode.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/usertrackingmode))
  Modes for tracking the user’s location on the map.
### Initializing for SwiftUI
- [init()](init().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap/init()))
  Creates a map for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [class WKInterfaceLabel](wkinterfacelabel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel))
  An interface element that displays static text.
- [class WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
  A label that displays the current date or time.
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
  A button in the user interface of your watchOS app.
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
  A button that you can use to trigger a Sign in with Apple request.
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
  A button that you can use to trigger payments through Apple Pay.
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
  An interface element that displays an editable text area.
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
  An interface element that toggles between an On and Off state.
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
  An interface element that lets users select a single floating-point value from a range of values.
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
  A view that displays data from a HealthKit activity summary object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap)*