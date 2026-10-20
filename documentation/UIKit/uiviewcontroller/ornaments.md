# ornaments

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

SwiftUI ornaments to display adjacent to the view controller.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var ornaments: [UIOrnament] { get set }
```

## See Also

### Managing the view
- [var view: UIView!](./view.md)
  The view that the controller manages.
- [var viewIfLoaded: UIView?](./viewifloaded.md)
  The view controller’s view, or `nil` if the view isn’t yet loaded.
- [var isViewLoaded: Bool](./isviewloaded.md)
  A Boolean value indicating whether the view is currently loaded into memory.
- [func loadView()](./loadview%28%29.md)
  Creates the view that the controller manages.
- [func viewDidLoad()](./viewdidload%28%29.md)
  Called after the controller’s view is loaded into memory.
- [func loadViewIfNeeded()](./loadviewifneeded%28%29.md)
  Loads the view controller’s view if it’s not loaded yet.
- [var title: String?](./title.md)
  A localized string that represents the view this controller manages.
- [var preferredContentSize: CGSize](./preferredcontentsize.md)
  The preferred size for the view controller’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/ornaments)*