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

WatchKit calls this method when the [`WKInterfaceDevice`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice) object’s  [`wristLocation`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/wristlocation), [`crownOrientation`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/crownorientation), or [`isAutorotated`](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated) properties change.

## See Also

- [var isAutorotating: Bool](isautorotating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating))
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated))
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [static func main()](main().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main()))
  Provides the top-level entry point for an app.
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()))
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidbecomeactive()))
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillresignactive()))
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground()))
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](applicationdidenterbackground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground()))
  Tells the delegate that the app has transitioned from the foreground to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/deviceorientationdidchange())*