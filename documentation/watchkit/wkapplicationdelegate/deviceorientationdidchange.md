# deviceOrientationDidChange()

**Framework**: WatchKit  
**Kind**: method

Tells the delegate that the device’s orientation has changed.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
optional func deviceOrientationDidChange()
```

#### Discussion

WatchKit calls this method when the [`WKInterfaceDevice`](wkinterfacedevice.md) object’s  [`wristLocation`](wkinterfacedevice/wristlocation.md), [`crownOrientation`](wkinterfacedevice/crownorientation.md), or [`isAutorotated`](wkextension/isautorotated.md) properties change.

## See Also

- [var isAutorotating: Bool](wkextension/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](wkextension/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [static func main()](wkapplicationdelegate/main.md)
  Provides the top-level entry point for an app.
- [func applicationDidFinishLaunching()](wkapplicationdelegate/applicationdidfinishlaunching.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [func applicationDidBecomeActive()](wkapplicationdelegate/applicationdidbecomeactive.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](wkapplicationdelegate/applicationwillresignactive.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](wkapplicationdelegate/applicationwillenterforeground.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](wkapplicationdelegate/applicationdidenterbackground.md)
  Tells the delegate that the app has transitioned from the foreground to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/deviceorientationdidchange())*