# rootInterfaceController

**Framework**: Watchkit  
**Kind**: property

The app’s root interface controller.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor var rootInterfaceController: WKInterfaceController? { get }
```

## Overview

The root interface controller is located in the app’s main storyboard and has the Main Entry Point object associated with it. WatchKit displays the root interface controller at launch time, although the app can present a different interface controller before the launch sequence finishes.

## See Also

- [var visibleInterfaceController: WKInterfaceController?](visibleinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/visibleinterfacecontroller))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/rootinterfacecontroller)*