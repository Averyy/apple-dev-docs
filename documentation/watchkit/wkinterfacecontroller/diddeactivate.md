# didDeactivate()

**Framework**: Watchkit  
**Kind**: method

Tells the interface controller that its view is no longer active.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func didDeactivate()
```

## Mentions

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))

## Overview

The system calls this method as part of the cleanup process for the interface controller. Use this method to invalidate timers or save any app-related state information that has not already been saved. Any tasks you perform using this method should finish quickly. An inactive interface controller may be reactivated later or it may be deallocated.

Do not use this method to modify your interface. WatchKit ignores attempts to set values of interface objects while your interface is inactive, including during the execution of this method. Modifications can be made only during initialization of your interface controller and between calls to [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) and this method.

The system calls this method on your WatchKit extension’s main thread. The `super` implementation of this method does nothing.

In iOS Simulator, WatchKit calls this method for the current interface controller when you lock the simulator by selecting Hardware > Lock. When you subsequently unlock the simulator, WatchKit calls that interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method again. You can use this capability to debug your activation and deactivation code.

## See Also

- [func willActivate()](willactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()))
- [func didAppear()](didappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()))
- [func willDisappear()](willdisappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willdisappear()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate())*