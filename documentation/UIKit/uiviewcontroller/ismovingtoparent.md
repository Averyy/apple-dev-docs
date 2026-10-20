# isMovingToParent

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view controller is moving to a parent view controller.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isMovingToParent: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isMovingToParentViewController) BOOL movingToParentViewController;
```

## See Also

### Responding to view-related events
- [func viewWillAppear(Bool)](./viewwillappear%28_%29.md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
- [func viewIsAppearing(Bool)](./viewisappearing%28_%29.md)
  Notifies the view controller that the system is adding the view controller’s view to a view hierarchy.
- [func viewDidAppear(Bool)](./viewdidappear%28_%29.md)
  Notifies the view controller that its view was added to a view hierarchy.
- [func viewWillDisappear(Bool)](./viewwilldisappear%28_%29.md)
  Notifies the view controller that its view is about to be removed from a view hierarchy.
- [func viewDidDisappear(Bool)](./viewdiddisappear%28_%29.md)
  Notifies the view controller that its view was removed from a view hierarchy.
- [var isBeingDismissed: Bool](./isbeingdismissed.md)
  A Boolean value indicating whether the view controller is in the process of being dismissed by one of its ancestors.
- [var isBeingPresented: Bool](./isbeingpresented.md)
  A Boolean value indicating whether the view controller in the process of being presented by one of its ancestors.
- [var isMovingFromParent: Bool](./ismovingfromparent.md)
  A Boolean value indicating whether the view controller is moving from a parent view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/ismovingtoparent)*