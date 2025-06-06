# dismissAddPassesController()

**Framework**: Watchkit  
**Kind**: method

Dismisses the pass interface controller

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func dismissAddPassesController()
```

#### Discussion

Use this method to dismiss a pass controller you previously displayed using the [`presentAddPassesController(withPasses:completion:)`](wkinterfacecontroller/presentaddpassescontroller(withpasses:completion:).md) method. When dismissing the pass controller programmatically, WatchKit still calls the completion block you provided.

## See Also

- [func presentAddPassesController(withPasses: [PKPass], completion: () -> Void)](wkinterfacecontroller/presentaddpassescontroller(withpasses:completion:).md)
  Displays a modal interface for presenting passes to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaddpassescontroller())*