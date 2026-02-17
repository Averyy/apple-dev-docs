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

You can configure Maps dynamically from your interface controller. Use the methods of [`WKInterfaceMap`](wkinterfacemap.md) to specify the visible region of the map and to add any annotations or points of interest. Tapping the map launches the Maps app on the user’s Apple Watch and displays the corresponding location.

Using a map object, you specify a geographic region to display and you can optionally add annotations to the surface of the map. Maps display annotations as images on top of the map content. You can use custom images or display the built-in pin images. Maps can display no more than five annotations at a time.

Don’t subclass or create instances of this class yourself. Instead, define outlets in your interface controller class and connect them to the corresponding objects in your storyboard file. For example, to refer to a map object in your interface, define a property with the following syntax in your interface controller class:

During the initialization of your interface controller, WatchKit creates a new instance of this class and assigns it to your outlet. At that point, you can use the object in your outlet to make changes to the onscreen map.

The Apple Watch must have an active network connection to download map tiles.

##### Configure the Map in Interface Builder

In Xcode, you can configure information about your map from your storyboard file. The map interface object has an Enabled attribute that appears as a checkbox in the Attributes inspector. When you enable the map interface object in this checkbox, tapping the map launches the Maps app and displays the current selected location.

## Topics

### Specifying the Map Region
- [func setVisibleMapRect(MKMapRect)](wkinterfacemap/setvisiblemaprect(_:).md)
  Changes the map’s visible region to the specified map rectangle.
- [func setRegion(MKCoordinateRegion)](wkinterfacemap/setregion(_:).md)
  Changes the map’s visible region to the specified coordinate region.
### Managing Map Annotations
- [func addAnnotation(CLLocationCoordinate2D, with: UIImage?, centerOffset: CGPoint)](wkinterfacemap/addannotation(_:with:centeroffset:).md)
  Displays the specified image on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, withImageNamed: String?, centerOffset: CGPoint)](wkinterfacemap/addannotation(_:withimagenamed:centeroffset:).md)
  Displays an image from the WatchKit app’s bundle on top of the map.
- [func addAnnotation(CLLocationCoordinate2D, with: WKInterfaceMapPinColor)](wkinterfacemap/addannotation(_:with:).md)
  Adds a pin to the map at the specified location.
- [enum WKInterfaceMapPinColor](wkinterfacemappincolor.md)
  Constants for map pin colors.
- [func removeAllAnnotations()](wkinterfacemap/removeallannotations.md)
  Removes all annotations from the map.
### Displaying the User’s Location
- [func setShowsUserLocation(Bool)](wkinterfacemap/setshowsuserlocation(_:).md)
  Sets whether the map shows the user’s current location.
- [func setShowsUserHeading(Bool)](wkinterfacemap/setshowsuserheading(_:).md)
  Sets whether the map shows the user heading.
- [func setUserTrackingMode(WKInterfaceMap.UserTrackingMode, animated: Bool)](wkinterfacemap/setusertrackingmode(_:animated:).md)
  Sets the map’s tracking mode.
- [WKInterfaceMap.UserTrackingMode](wkinterfacemap/usertrackingmode.md)
  Modes for tracking the user’s location on the map.
### Initializing for SwiftUI
- [init()](wkinterfacemap/init.md)
  Creates a map for use in SwiftUI.

## Relationships

### Inherits From
- [WKInterfaceObject](wkinterfaceobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class WKInterfaceLabel](wkinterfacelabel.md)
  An interface element that displays static text.
- [class WKInterfaceDate](wkinterfacedate.md)
  A label that displays the current date or time.
- [class WKInterfaceTimer](wkinterfacetimer.md)
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md)
  A button in the user interface of your watchOS app.
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md)
  A button that you can use to trigger a Sign in with Apple request.
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md)
  A button that you can use to trigger payments through Apple Pay.
- [class WKInterfaceTextField](wkinterfacetextfield.md)
  An interface element that displays an editable text area.
- [class WKInterfaceSwitch](wkinterfaceswitch.md)
  An interface element that toggles between an On and Off state.
- [class WKInterfaceSlider](wkinterfaceslider.md)
  An interface element that lets users select a single floating-point value from a range of values.
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md)
  A view that displays data from a HealthKit activity summary object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacemap)*