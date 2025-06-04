# didAppear()

**Framework**: Watchkit  
**Kind**: method

Tells the interface controller that its view is now onscreen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func didAppear()
```

## Mentions

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

## Overview

WatchKit calls this method shortly after the interface controller’s contents appear onscreen. Use this method to configure animations or other interface-related tasks.

The system calls this method on your WatchKit extension’s main thread. The `super` implementation of this method does nothing.

## See Also

- [func willActivate()](willactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()))
- [func didDeactivate()](diddeactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()))
- [func willDisappear()](willdisappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willdisappear()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear())*