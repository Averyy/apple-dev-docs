# willActivate()

**Framework**: WatchKit  
**Kind**: method

Tells the interface controller that the system is about to activate its view.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func willActivate()
```

## Mentions

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

#### Discussion

The system calls this method when it is getting ready to display your interface controller. Use this method to perform last minute tasks required to ensure your content is up to date. Do not use this method to perform the initial setup of your interface. Your interface should be mostly initialized and ready to use by the time this method is called.

The calling of this method is not a guarantee that your interface controller is onscreen or about to appear onscreen. The system may call this method early to give you time to update your content.  Use the [`didAppear()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()) method to determine when your interface appears onscreen.

The system calls this method on your WatchKit extension’s main thread. The `super` implementation of this method does nothing.

## See Also

- [func didDeactivate()](diddeactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()))
  Tells the interface controller that its view is no longer active.
- [func didAppear()](didappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()))
  Tells the interface controller that its view is now onscreen.
- [func willDisappear()](willdisappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willdisappear()))
  Tells the interface controller that its view is now offscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate())*