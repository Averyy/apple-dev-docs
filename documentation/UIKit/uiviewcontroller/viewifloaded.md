# viewIfLoaded

**Framework**: UIKit  
**Kind**: property

The view controller’s view, or `nil` if the view isn’t yet loaded.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var viewIfLoaded: UIView? { get }
```

#### Discussion

If the view controller’s view has already been loaded, this property contains that view. If the view has not yet been loaded, this property is set to `nil`.

## See Also

- [var view: UIView!](uiviewcontroller/view.md)
  The view that the controller manages.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewifloaded)*