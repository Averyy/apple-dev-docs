# UIViewControllerPreviewingDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

> **Deprecated**: Use [`UIContextMenuInteractionDelegate`](./uicontextmenuinteractiondelegate.md) instead.

## Declaration

```swift
@MainActor
protocol UIViewControllerPreviewingDelegate : NSObjectProtocol
```

```objc
@protocol UIViewControllerPreviewingDelegate <NSObject>
```

#### Overview

To learn about 3D Touch, read [Adopting 3D Touch on iPhone](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Adopting3DTouchOniPhone/index.html#//apple_ref/doc/uid/TP40016543).

> **Terminology Note**:  The end-user terminology for the views presented during the phases of force-based touches includes *peek* and *pop*. For clarity here, and to align with the API names, this document uses the corresponding terms *preview* and *commit view*.

## Topics

### Providing preview and commit views for 3D Touch
- [func previewingContext(any UIViewControllerPreviewing, viewControllerForLocation: CGPoint) -> UIViewController?](./uiviewcontrollerpreviewingdelegate/previewingcontext%28_,viewcontrollerforlocation%29.md)
  Called when the user has pressed a source view in a previewing view controller, thereby obtaining a surrounding blur to indicate that a preview (peek) is available.
- [func previewingContext(any UIViewControllerPreviewing, commit: UIViewController)](./uiviewcontrollerpreviewingdelegate/previewingcontext%28_,commit%29.md)
  Called to let you prepare the presentation of a commit (pop) view from your commit view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated protocols
- [protocol UIActionSheetDelegate](./uiactionsheetdelegate.md)
  The interface for the delegate of an action sheet object.
- [protocol UIAlertViewDelegate](./uialertviewdelegate.md)
  The interface for the delegate of an alert view object.
- [protocol UIPopoverControllerDelegate](./uipopovercontrollerdelegate.md)
  The interface for the delegate of a popover controller object.
- [protocol UISearchDisplayDelegate](./uisearchdisplaydelegate.md)
  The interface for the delegate of a search display controller.
- [protocol UIViewControllerPreviewing](./uiviewcontrollerpreviewing.md)
  A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.
- [UIAccelerometerDelegate](./uiaccelerometerdelegate.md)
  The interface for receiving acceleration-related data from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate)*