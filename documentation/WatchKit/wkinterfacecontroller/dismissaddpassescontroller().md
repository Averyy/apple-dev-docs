# dismissAddPassesController()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the pass interface controller

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func dismissAddPassesController()
```

```objc
- (void) dismissAddPassesController;
```

#### Discussion

Use this method to dismiss a pass controller you previously displayed using the [`presentAddPassesController(withPasses:completion:)`](./presentaddpassescontroller%28withpasses,completion%29.md) method. When dismissing the pass controller programmatically, WatchKit still calls the completion block you provided.

## See Also

### Adding PassKit passes
- [func presentAddPassesController(withPasses: [PKPass], completion: () -> Void)](./presentaddpassescontroller%28withpasses,completion%29.md)
  Displays a modal interface for presenting passes to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/dismissaddpassescontroller())*