# UISearchDisplayDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface for the delegate of a search display controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst

> **Deprecated**: Use [`UISearchControllerDelegate`](./uisearchcontrollerdelegate.md) instead.

## Declaration

```swift
@MainActor
protocol UISearchDisplayDelegate : NSObjectProtocol
```

```objc
@protocol UISearchDisplayDelegate <NSObject>
```

#### Overview

This protocol defines delegate methods for [`UISearchDisplayController`](./uisearchdisplaycontroller.md) objects.

## Topics

### Deprecated
- [Deprecated symbols](./uisearchdisplaydelegate-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

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
- [protocol UIViewControllerPreviewing](./uiviewcontrollerpreviewing.md)
  A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch.
- [protocol UIViewControllerPreviewingDelegate](./uiviewcontrollerpreviewingdelegate.md)
  A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate)*