# loadViewIfNeeded()

**Framework**: UIKit  
**Kind**: method

Loads the view controller’s view if it’s not loaded yet.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func loadViewIfNeeded()
```

#### Discussion

Calling this method loads the view controller’s view from its storyboard file, or creates the view as needed based on the established rules.

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
- [var title: String?](uiviewcontroller/title.md)
  A localized string that represents the view this controller manages.
- [var preferredContentSize: CGSize](uiviewcontroller/preferredcontentsize.md)
  The preferred size for the view controller’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/loadviewifneeded())*