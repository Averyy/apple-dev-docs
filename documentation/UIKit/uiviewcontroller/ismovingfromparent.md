# isMovingFromParent

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the view controller is moving from a parent view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isMovingFromParent: Bool { get }
```

## See Also

- [func viewWillAppear(Bool)](uiviewcontroller/viewwillappear(_:).md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
- [func viewIsAppearing(Bool)](uiviewcontroller/viewisappearing(_:).md)
  Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.
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
- [var isMovingToParent: Bool](uiviewcontroller/ismovingtoparent.md)
  A Boolean value indicating whether the view controller is moving to a parent view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/ismovingfromparent)*