# deviceOrientationDidChange()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the device’s orientation has changed.

**Availability**:
- watchOS 4.0+ - Deprecated in 9.2

## Declaration

```swift
optional func deviceOrientationDidChange()
```

```objc
- (void) deviceOrientationDidChange;
```

## Discussion

This method is called when the [`WKInterfaceDevice`](../wkinterfacedevice.md) object’s  [`wristLocation`](../wkinterfacedevice/wristlocation.md), [`crownOrientation`](../wkinterfacedevice/crownorientation.md), or [`isAutorotated`](../wkextension/isautorotated.md) properties change.

## See Also

### Related Documentation
- [var isAutorotating: Bool](../wkextension/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](../wkextension/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
### Monitoring state changes
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [func applicationDidFinishLaunching()](./applicationdidfinishlaunching%28%29.md)
  Tells the delegate that the launch process is almost done and the extension is almost ready to run.
- [func applicationDidBecomeActive()](./applicationdidbecomeactive%28%29.md)
  Tells the delegate that the watchOS app is visible and processing events.
- [func applicationWillResignActive()](./applicationwillresignactive%28%29.md)
  Tells the delegate that the system is about to deactivate the watchOS app.
- [func applicationWillEnterForeground()](./applicationwillenterforeground%28%29.md)
  Tells the delegate that the app is about to transition from the background to the foreground.
- [func applicationDidEnterBackground()](./applicationdidenterbackground%28%29.md)
  Tells the delegate that the app has transitioned from the foreground to the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/deviceorientationdidchange())*