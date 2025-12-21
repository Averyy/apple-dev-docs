# ornaments

**Framework**: UIKit  
**Kind**: property

SwiftUI ornaments to display adjacent to the view controller.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var ornaments: [UIOrnament] { get set }
```

## See Also

- [var view: UIView!](uiviewcontroller/view.md)
  The view that the controller manages.
- [var viewIfLoaded: UIView?](uiviewcontroller/viewifloaded.md)
  The view controller’s view, or `nil` if the view isn’t yet loaded.
- [var isViewLoaded: Bool](uiviewcontroller/isviewloaded.md)
  A Boolean value indicating whether the view is currently loaded into memory.
- [func loadView()](uiviewcontroller/loadview.md)
  Creates the view that the controller manages.
- [func viewDidLoad()](uiviewcontroller/viewdidload.md)
  Called after the controller’s view is loaded into memory.
- [func loadViewIfNeeded()](uiviewcontroller/loadviewifneeded.md)
  Loads the view controller’s view if it’s not loaded yet.
- [var title: String?](uiviewcontroller/title.md)
  A localized string that represents the view this controller manages.
- [var preferredContentSize: CGSize](uiviewcontroller/preferredcontentsize.md)
  The preferred size for the view controller’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/ornaments)*