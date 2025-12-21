# loadView()

**Framework**: UIKit  
**Kind**: method

Creates the view that the controller manages.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func loadView()
```

#### Discussion

You should never call this method directly. The view controller calls this method when its [`view`](uiviewcontroller/view.md) property is requested but is currently `nil`. This method loads or creates a view and assigns it to the [`view`](uiviewcontroller/view.md) property.

If the view controller has an associated nib file, this method loads the view from the nib file. A view controller has an associated nib file if the [`nibName`](uiviewcontroller/nibname.md) property returns a non-`nil` value, which occurs if the view controller was instantiated from a storyboard, if you explicitly assigned it a nib file using the [`init(nibName:bundle:)`](uiviewcontroller/init(nibname:bundle:).md) method, or if iOS finds a nib file in the app bundle with a name based on the view controller’s class name. If the view controller does not have an associated nib file, this method creates a plain [`UIView`](uiview.md) object instead.

If you use Interface Builder to create your views and initialize the view controller, you must not override this method.

You can override this method in order to create your views manually. If you choose to do so, assign the root view of your view hierarchy to the [`view`](uiviewcontroller/view.md) property. The views you create should be unique instances and should not be shared with any other view controller object. Your custom implementation of this method should not call `super`.

If you want to perform any additional initialization of your views, do so in the [`viewDidLoad()`](uiviewcontroller/viewdidload().md) method.

## See Also

- [var nibName: String?](uiviewcontroller/nibname.md)
  The name of the view controller’s nib file, if one was specified.
- [var view: UIView!](uiviewcontroller/view.md)
  The view that the controller manages.
- [var viewIfLoaded: UIView?](uiviewcontroller/viewifloaded.md)
  The view controller’s view, or `nil` if the view isn’t yet loaded.
- [var isViewLoaded: Bool](uiviewcontroller/isviewloaded.md)
  A Boolean value indicating whether the view is currently loaded into memory.
- [func viewDidLoad()](uiviewcontroller/viewdidload.md)
  Called after the controller’s view is loaded into memory.
- [func loadViewIfNeeded()](uiviewcontroller/loadviewifneeded.md)
  Loads the view controller’s view if it’s not loaded yet.
- [var title: String?](uiviewcontroller/title.md)
  A localized string that represents the view this controller manages.
- [var preferredContentSize: CGSize](uiviewcontroller/preferredcontentsize.md)
  The preferred size for the view controller’s view.
- [var ornaments: [UIOrnament]](uiviewcontroller/ornaments.md)
  SwiftUI ornaments to display adjacent to the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/loadview())*