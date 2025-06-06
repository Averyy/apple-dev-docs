# deviceOrientationDidChange()

**Framework**: Watchkit  
**Kind**: method

Tells the delegate that the device’s orientation has changed.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
optional func deviceOrientationDidChange()
```

#### Discussion

This method is called when the [`WKInterfaceDevice`](wkinterfacedevice.md) object’s  [`wristLocation`](wkinterfacedevice/wristlocation.md), [`crownOrientation`](wkinterfacedevice/crownorientation.md), or [`isAutorotated`](wkextension/isautorotated.md) properties change.

## See Also

- [var isAutorotating: Bool](wkextension/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](wkextension/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidFinishLaunching()](wkextensiondelegate/applicationdidfinishlaunching.md)
  Tells the delegate that the launch process is almost done and the extension is almost ready to run.
- [func applicationDidBecomeActive()](wkextensiondelegate/applicationdidbecomeactive.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](wkextensiondelegate/applicationwillresignactive.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](wkextensiondelegate/applicationwillenterforeground.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](wkextensiondelegate/applicationdidenterbackground.md)
  Tells the delegate that the app has transitioned from the foreground to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/deviceorientationdidchange())*