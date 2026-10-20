# viewWillAppear(_:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Performs some action before the view appears.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
override dynamic func viewWillAppear(_ animated: Bool)
```

## Parameters

- `animated`: A Boolean value that indicates whether the view will appear using an animation.

## See Also

### Responding to view controller events
- [func loadView()](./loadview%28%29.md)
  Creates the view that the controller manages.
- [func viewDidLoad()](./viewdidload%28%29.md)
  Performs some action after the system loads the view into memory.
- [func viewDidDisappear(Bool)](./viewdiddisappear%28_%29.md)
  Performs some action after the view disappears.
- [func removeFromParent()](./removefromparent%28%29.md)
  Removes the view controller from its parent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/viewwillappear(_:))*