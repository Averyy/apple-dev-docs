# viewDidAppear(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the view controller that its view was added to a view hierarchy.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func viewDidAppear(_ animated: Bool)
```

## Mentions

- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md)
- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Discussion

You can override this method to perform additional tasks associated with presenting the view. If you override this method, you must call `super` at some point in your implementation.

> **Note**:  If a view controller is presented by a view controller inside of a popover, this method is not invoked on the presenting view controller after the presented controller is dismissed.

## Parameters

- `animated`: If  , the view was added to the window using an animation.

## See Also

- [func viewWillAppear(Bool)](uiviewcontroller/viewwillappear(_:).md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
- [func viewIsAppearing(Bool)](uiviewcontroller/viewisappearing(_:).md)
  Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/viewdidappear(_:))*