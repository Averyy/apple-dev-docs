# willDisappear()

**Framework**: Watchkit  
**Kind**: method

Tells the interface controller that its view is now offscreen.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func willDisappear()
```

## Mentions

- [Navigating Between Scenes](navigating-between-scenes.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/navigating-between-scenes))

## Overview

WatchKit calls this method shortly before removing your interface controller’s content from the screen. Use this method to stop animations or perform other interface-related tasks prior to deactivation.

The system calls this method on your WatchKit extension’s main thread. The `super` implementation of this method does nothing.

## See Also

- [func willActivate()](willactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()))
- [func didDeactivate()](diddeactivate().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()))
- [func didAppear()](didappear().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willdisappear())*