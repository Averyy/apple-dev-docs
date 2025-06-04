# dismissAddPassesController()

**Framework**: Watchkit  
**Kind**: method

Dismisses the pass interface controller

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor func dismissAddPassesController()
```

## Overview

Use this method to dismiss a pass controller you previously displayed using the [`presentAddPassesController(withPasses:completion:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaddpassescontroller(withpasses:completion:)) method. When dismissing the pass controller programmatically, WatchKit still calls the completion block you provided.

## See Also

- [func presentAddPassesController(withPasses: [PKPass], completion: () -> Void)](presentaddpassescontroller(withpasses:completion:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/presentaddpassescontroller(withpasses:completion:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaddpassescontroller())*