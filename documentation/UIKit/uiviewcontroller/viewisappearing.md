# viewIsAppearing(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func viewIsAppearing(_ animated: Bool)
```

## Mentions

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)
- [Enhancing your app with fluid transitions](enhancing-your-app-with-fluid-transitions.md)

#### Discussion

The system calls this method once each time a view controller’s view appears after the [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) call. In contrast to `viewWillAppear(_:)`, the system calls this method after it adds the view controller’s view to the view hierarchy, and the superview lays out the view controller’s view. By the time the system calls this method, both the view controller and its view have received updated trait collections and the view has accurate geometry.

You can override this method to perform custom tasks associated with displaying the view. For example, you might use this method to configure or update views based on the trait collections of the view or view controller. Or, because computing a scroll position relies on the view’s size and geometry, you might programmatically scroll a collection or table view to ensure a selected cell is visible when the view appears.

If you override this method, you need to call `super` at some point in your implementation.

##### Choosing the Appropriate Callback

Although the system calls this method after [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md), both callbacks occur within the same [`CATransaction`](https://developer.apple.com/documentation/QuartzCore/CATransaction). This means that changes you make in either method become visible to the user at the same time.

![A diagram titled View controller appearance that consists of seven stacked horizontal bars in three distinct sections. An arrow on the right labeled Time descends from the top to the bottom. The top section is labeled Transaction and contains two horizontal bars labeled viewWillAppear and View added to hierarchy. The second section is labeled Layout and contains four horizontal bars labeled View laid out by superview; traits updated; viewIsAppearing; viewWillLayoutSubviews; and viewDidLayoutSubviews. There is a gap between the second and third sections that contains the text: Transition animates. The third section is labeled Transaction and contains one horizontal bar labeled viewDidAppear.](https://docs-assets.developer.apple.com/published/9f4992bcbe7b9858109d61db6c864256/media-4250012%402x.png)

The traits and geometry aren’t up to date when the system calls [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md), but they are when the system calls `viewIsAppearing(_:)`, so use `viewIsAppearing(_:)` to update your views.

Use `viewWillAppear(:_)` only when:

- You need a callback before the view transition begins, such as when accessing the [`transitionCoordinator`](uiviewcontroller/transitioncoordinator.md) to add alongside animations. Alongside animations are animations that you direct the framework to perform concurrently with the view controller transition animations.
- You need balanced callbacks to do something that doesn’t depend on the view controller or view traits, hierarchy, or geometry. Use cases include registering for database notifications in [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) and unregistering in [`viewDidDisappear(_:)`](uiviewcontroller/viewdiddisappear(_:).md).

For all other cases, use `viewIsAppearing(_:)` to update your views.

| State at callback time | `viewWillAppear(_:)` | `viewIsAppearing(_:)` |
| --- | --- | --- |
| Transition coordinator available for adding alongside animations |  | ✘ |
| View added to hierarchy |  |  |
| View controller and view trait collections updated | ✘ |  |
| View geometry (size, safe area, and so forth) is accurate | ✘ |  |

The system calls layout methods, such as [`viewWillLayoutSubviews()`](uiviewcontroller/viewwilllayoutsubviews().md) and [`viewDidLayoutSubviews()`](uiviewcontroller/viewdidlayoutsubviews().md), whenever the view runs [`layoutSubviews()`](uiview/layoutsubviews().md), which can happen multiple times during the transition, or at any time while the view is visible. However, the system calls `viewIsAppearing(_:)` only once during the appearance transition, and calls it even if the view doesn’t require laying out when it appears.

For more information about how a view controller adds views to view hierarchies, and the sequence of messages that occur, see [`Displaying and managing views with a view controller`](displaying-and-managing-views-with-a-view-controller.md).

## Parameters

- `animated`: If  , the system is adding the view to the window using an animation.

## See Also

- [func viewDidLoad()](uiviewcontroller/viewdidload.md)
  Called after the controller’s view is loaded into memory.
- [func viewWillAppear(Bool)](uiviewcontroller/viewwillappear(_:).md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
- [func viewDidAppear(Bool)](uiviewcontroller/viewdidappear(_:).md)
  Notifies the view controller that its view was added to a view hierarchy.
- [func viewWillDisappear(Bool)](uiviewcontroller/viewwilldisappear(_:).md)
  Notifies the view controller that its view is about to be removed from a view hierarchy.
- [func viewDidDisappear(Bool)](uiviewcontroller/viewdiddisappear(_:).md)
  Notifies the view controller that its view was removed from a view hierarchy.
- [var isBeingDismissed: Bool](uiviewcontroller/isbeingdismissed.md)
  A Boolean value indicating whether the view controller is in the process of being dismissed by one of its ancestors.
- [var isBeingPresented: Bool](uiviewcontroller/isbeingpresented.md)
  A Boolean value indicating whether the view controller in the process of being presented by one of its ancestors.
- [var isMovingFromParent: Bool](uiviewcontroller/ismovingfromparent.md)
  A Boolean value indicating whether the view controller is moving from a parent view controller.
- [var isMovingToParent: Bool](uiviewcontroller/ismovingtoparent.md)
  A Boolean value indicating whether the view controller is moving to a parent view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewisappearing(_:))*