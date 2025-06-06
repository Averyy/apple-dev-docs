# UISheetPresentationController

**Framework**: UIKit  
**Kind**: class

A presentation controller that manages the appearance and behavior of a sheet.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISheetPresentationController
```

#### Overview

[`UISheetPresentationController`](uisheetpresentationcontroller.md) lets you present your view controller as a sheet. Before you present your view controller, configure the sheet presentation controller in its [`sheetPresentationController`](uiviewcontroller/sheetpresentationcontroller.md) property with the behavior and appearance you want for your sheet.

```swift
// In a subclass of UIViewController, customize and present the sheet.
func showMyViewControllerInACustomizedSheet() {
    let viewControllerToPresent = MyViewController()
    if let sheet = viewControllerToPresent.sheetPresentationController {
        sheet.detents = [.medium(), .large()]
        sheet.largestUndimmedDetentIdentifier = .medium
        sheet.prefersScrollingExpandsWhenScrolledToEdge = false
        sheet.prefersEdgeAttachedInCompactHeight = true
        sheet.widthFollowsPreferredContentSizeWhenEdgeAttached = true
    }
    present(viewControllerToPresent, animated: true, completion: nil)
}
```

Sheet presentation controllers specify a sheet’s size based on a , a height where a sheet naturally rests. Detents allow a sheet to resize from one edge of its fully expanded frame while the other three edges remain fixed. You specify the detents that a sheet supports using [`detents`](uisheetpresentationcontroller/detents.md), and monitor its most recently selected detent using [`selectedDetentIdentifier`](uisheetpresentationcontroller/selecteddetentidentifier.md).

> **Note**:  Session 10063: [`Customize and Resize Sheets in UIKit`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10063) Session 10068: [`What’s new in UIKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10068)

 Session 10063: [`Customize and Resize Sheets in UIKit`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10063)

Session 10068: [`What’s new in UIKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10068)

## Topics

### Specifying the height
- [var detents: [UISheetPresentationController.Detent]](uisheetpresentationcontroller/detents.md)
  The array of heights where a sheet can rest.
- [var selectedDetentIdentifier: UISheetPresentationController.Detent.Identifier?](uisheetpresentationcontroller/selecteddetentidentifier.md)
  The identifier of the most recently selected detent.
- [UISheetPresentationController.Detent](uisheetpresentationcontroller/detent.md)
  An object that represents a height where a sheet naturally rests.
### Managing the delegate
- [var delegate: (any UISheetPresentationControllerDelegate)?](uisheetpresentationcontroller/delegate.md)
  The delegate of the sheet presentation controller.
- [protocol UISheetPresentationControllerDelegate](uisheetpresentationcontrollerdelegate.md)
  The interface that an object implements to respond to size changes in a sheet presentation controller.
### Managing user interaction
- [var largestUndimmedDetentIdentifier: UISheetPresentationController.Detent.Identifier?](uisheetpresentationcontroller/largestundimmeddetentidentifier.md)
  The largest detent that doesn’t dim the view underneath the sheet.
- [var prefersScrollingExpandsWhenScrolledToEdge: Bool](uisheetpresentationcontroller/prefersscrollingexpandswhenscrolledtoedge.md)
  A Boolean value that determines whether scrolling expands the sheet to a larger detent.
### Managing the appearance
- [var prefersGrabberVisible: Bool](uisheetpresentationcontroller/prefersgrabbervisible.md)
  A Boolean value that determines whether the sheet shows a grabber at the top.
- [var prefersPageSizing: Bool](uisheetpresentationcontroller/preferspagesizing.md)
  A Boolean value that indicates whether the sheet sizes itself for readable content.
- [var prefersEdgeAttachedInCompactHeight: Bool](uisheetpresentationcontroller/prefersedgeattachedincompactheight.md)
  A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool](uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached.md)
  A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [var preferredCornerRadius: CGFloat?](uisheetpresentationcontroller/preferredcornerradius-3mb5.md)
  The corner radius that the sheet attempts to present with.
### Customizing the position
- [var sourceView: UIView?](uisheetpresentationcontroller/sourceview.md)
  The view that the sheet centers itself over.
### Working with custom detents
- [func invalidateDetents()](uisheetpresentationcontroller/invalidatedetents.md)
  Notifies the sheet to re-evaluate its detent value in the next layout pass.
### Animating changes to the sheet
- [func animateChanges(() -> Void)](uisheetpresentationcontroller/animatechanges(_:).md)
  Animates the UI changes to the sheet’s properties.

## Relationships

### Inherits From
- [UIPresentationController](uipresentationcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)

## See Also

- [Disabling the pull-down gesture for a sheet](disabling-the-pull-down-gesture-for-a-sheet.md)
  Ensure a positive user experience when presenting a view controller as a sheet.
- [class UIPresentationController](uipresentationcontroller.md)
  An object that manages the transition animations and the presentation of view controllers onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller)*