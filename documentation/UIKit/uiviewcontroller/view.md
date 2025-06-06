# view

**Framework**: UIKit  
**Kind**: property

The view that the controller manages.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var view: UIView! { get set }
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Discussion

This property represents the root view of the view controller’s view hierarchy. The default value of this property is `nil`.

If you access this property when its value is `nil`, the view controller automatically calls the [`loadView()`](uiviewcontroller/loadview().md) method and returns the resulting view.

Each view controller is the sole owner of its view object. Don’t associate the same view object with multiple view controllers. The only exception is that a container view controller implementation may add another view controller’s view object to its own view hierarchy. Before adding the subview, the container must first call its [`addChild(_:)`](uiviewcontroller/addchild(_:).md) method to create a parent-child relationship between the two view controller objects.

Because accessing this property can cause the view to be loaded automatically, you can use [`isViewLoaded`](uiviewcontroller/isviewloaded.md) to determine if the view is currently in memory. Unlike this property, [`isViewLoaded`](uiviewcontroller/isviewloaded.md) doesn’t force the loading of the view if it’s not currently in memory.

For more information about how a view controller loads and unloads its view, see [`Managing your app’s life cycle`](managing-your-app-s-life-cycle.md).

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/view)*