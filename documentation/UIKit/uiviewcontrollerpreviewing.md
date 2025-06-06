# UIViewControllerPreviewing

**Framework**: Uikit  
**Kind**: protocol

A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIViewControllerPreviewing : NSObjectProtocol
```

#### Overview

The system returns a context object conforming to this protocol when you call a view controller’s [`registerForPreviewing(with:sourceView:)`](uiviewcontroller/registerforpreviewing(with:sourceview:).md) method. This method registers the view controller to participate in 3D Touch preview (peek) and commit (pop) behaviors.

> **Note**:  The end-user terminology for the views presented during the phases of force-based touches includes  and . For clarity here, and to align with the API names, this document uses the corresponding terms  and .

To learn about 3D Touch, read [`Adopting 3D Touch on iPhone`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/Adopting3DTouchOniPhone/index.html#//apple_ref/doc/uid/TP40016543).

> ❗ **Important**:  Don’t adopt this protocol in custom classes.

## Topics

### Configuring a source view for a 3D Touch previewing view controller
- [var sourceRect: CGRect](uiviewcontrollerpreviewing/sourcerect.md)
  The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs.
- [var previewingGestureRecognizerForFailureRelationship: UIGestureRecognizer](uiviewcontrollerpreviewing/previewinggesturerecognizerforfailurerelationship.md)
  A gesture recognizer suitable for setting up failure requirements for a preview’s (peek’s) gestures.
### Accessing properties of a 3D Touch previewing view controller
- [var delegate: any UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewing/delegate.md)
  The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers.
- [var sourceView: UIView](uiviewcontrollerpreviewing/sourceview.md)
  A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user.

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
- [protocol UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md)
  A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uiviewcontrollerpreviewing)*