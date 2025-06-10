# UIViewControllerPreviewingDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIViewControllerPreviewingDelegate : NSObjectProtocol
```

#### Overview

To learn about 3D Touch, read [`Adopting 3D Touch on iPhone`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Adopting3DTouchOniPhone/index.html#//apple_ref/doc/uid/TP40016543).

> **Note**:  The end-user terminology for the views presented during the phases of force-based touches includes  and . For clarity here, and to align with the API names, this document uses the corresponding terms  and .

## Topics

### Providing preview and commit views for 3D Touch
- [func previewingContext(any UIViewControllerPreviewing, viewControllerForLocation: CGPoint) -> UIViewController?](uiviewcontrollerpreviewingdelegate/previewingcontext(_:viewcontrollerforlocation:).md)
  Called when the user has pressed a source view in a previewing view controller, thereby obtaining a surrounding blur to indicate that a preview (peek) is available.
- [func previewingContext(any UIViewControllerPreviewing, commit: UIViewController)](uiviewcontrollerpreviewingdelegate/previewingcontext(_:commit:).md)
  Called to let you prepare the presentation of a commit (pop) view from your commit view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol UIAccelerometerDelegate](uiaccelerometerdelegate.md)
  The interface for receiving acceleration-related data from the system.
- [protocol UIActionSheetDelegate](uiactionsheetdelegate.md)
  The interface for the delegate of an action sheet object.
- [protocol UIAlertViewDelegate](uialertviewdelegate.md)
  The interface for the delegate of an alert view object.
- [protocol UIPopoverControllerDelegate](uipopovercontrollerdelegate.md)
  The interface for the delegate of a popover controller object.
- [protocol UISearchDisplayDelegate](uisearchdisplaydelegate.md)
  The interface for the delegate of a search display controller.
- [protocol UIViewControllerPreviewing](uiviewcontrollerpreviewing.md)
  A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate)*