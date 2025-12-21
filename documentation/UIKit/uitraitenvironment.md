# UITraitEnvironment

**Framework**: UIKit  
**Kind**: protocol

A set of methods that makes the iOS interface environment available to your app.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITraitEnvironment : NSObjectProtocol
```

## Mentions

- [Checking the availability of 3D Touch](checking-the-availability-of-3d-touch.md)
- [Providing data to the view hierarchy with custom traits](providing-data-to-the-view-hierarchy-with-custom-traits.md)

#### Overview

The system represents the iOS interface environment with , such as horizontal and vertical size class, display scale, and user interface idiom. You access the trait environment of an object that adopts this protocol with the [`traitCollection`](uitraitenvironment/traitcollection.md) property.

The trait system propagates values from the top of the view hierarchy downward, to every view controller and view in your app. When you modify a trait at any level using trait overrides, that change affects the modified object and all of its descendants. This hierarchical propagation makes it easy to apply configuration changes to entire subtrees of your interface.

For example, setting a trait override on a window scene affects all view controllers and views within that scene. Similarly, setting a trait override on a specific view affects only that view and its subviews.

For more information about how traits propagate through the system, see [`Unleash the UIKit trait system`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10057).

## Topics

### Accessing a trait collection
- [var traitCollection: UITraitCollection](uitraitenvironment/traitcollection.md)
  The traits, such as the size class and scale factor, that describe the current environment of the object.
### Responding to a change in the interface environment
- [func traitCollectionDidChange(UITraitCollection?)](uitraitenvironment/traitcollectiondidchange(_:).md)
  Reports changes in the iOS interface environment.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIActionSheet](uiactionsheet.md)
- [UIActivityIndicatorView](uiactivityindicatorview.md)
- [UIActivityViewController](uiactivityviewcontroller.md)
- [UIAlertController](uialertcontroller.md)
- [UIAlertView](uialertview.md)
- [UIBackgroundExtensionView](uibackgroundextensionview.md)
- [UIButton](uibutton.md)
- [UICalendarView](uicalendarview.md)
- [UICloudSharingController](uicloudsharingcontroller.md)
- [UICollectionReusableView](uicollectionreusableview.md)
- [UICollectionView](uicollectionview.md)
- [UICollectionViewCell](uicollectionviewcell.md)
- [UICollectionViewController](uicollectionviewcontroller.md)
- [UICollectionViewListCell](uicollectionviewlistcell.md)
- [UIColorPickerViewController](uicolorpickerviewcontroller.md)
- [UIColorWell](uicolorwell.md)
- [UIContentUnavailableView](uicontentunavailableview.md)
- [UIControl](uicontrol.md)
- [UIDatePicker](uidatepicker.md)
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
- [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md)
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)
- [UIDocumentViewController](uidocumentviewcontroller.md)
- [UIEventAttributionView](uieventattributionview.md)
- [UIFontPickerViewController](uifontpickerviewcontroller.md)
- [UIImagePickerController](uiimagepickercontroller.md)
- [UIImageView](uiimageview.md)
- [UIInputView](uiinputview.md)
- [UIInputViewController](uiinputviewcontroller.md)
- [UILabel](uilabel.md)
- [UIListContentView](uilistcontentview.md)
- [UINavigationBar](uinavigationbar.md)
- [UINavigationController](uinavigationcontroller.md)
- [UIPageControl](uipagecontrol.md)
- [UIPageViewController](uipageviewcontroller.md)
- [UIPasteControl](uipastecontrol.md)
- [UIPickerView](uipickerview.md)
- [UIPopoverBackgroundView](uipopoverbackgroundview.md)
- [UIPopoverPresentationController](uipopoverpresentationcontroller.md)
- [UIPresentationController](uipresentationcontroller.md)
- [UIProgressView](uiprogressview.md)
- [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md)
- [UIRefreshControl](uirefreshcontrol.md)
- [UIScreen](uiscreen.md)
- [UIScrollView](uiscrollview.md)
- [UISearchBar](uisearchbar.md)
- [UISearchContainerViewController](uisearchcontainerviewcontroller.md)
- [UISearchController](uisearchcontroller.md)
- [UISearchTextField](uisearchtextfield.md)
- [UISegmentedControl](uisegmentedcontrol.md)
- [UISheetPresentationController](uisheetpresentationcontroller.md)
- [UISlider](uislider.md)
- [UISplitViewController](uisplitviewcontroller.md)
- [UIStackView](uistackview.md)
- [UIStandardTextCursorView](uistandardtextcursorview.md)
- [UIStepper](uistepper.md)
- [UISwitch](uiswitch.md)
- [UITabBar](uitabbar.md)
- [UITabBarController](uitabbarcontroller.md)
- [UITableView](uitableview.md)
- [UITableViewCell](uitableviewcell.md)
- [UITableViewController](uitableviewcontroller.md)
- [UITableViewHeaderFooterView](uitableviewheaderfooterview.md)
- [UITextField](uitextfield.md)
- [UITextFormattingViewController](uitextformattingviewcontroller.md)
- [UITextView](uitextview.md)
- [UIToolbar](uitoolbar.md)
- [UIVideoEditorController](uivideoeditorcontroller.md)
- [UIView](uiview.md)
- [UIViewController](uiviewcontroller.md)
- [UIVisualEffectView](uivisualeffectview.md)
- [UIWebView](uiwebview.md)
- [UIWindow](uiwindow.md)
- [UIWindowScene](uiwindowscene.md)

## See Also

- [class UITraitCollection](uitraitcollection.md)
  A collection of data that represents the environment for an individual element in your app’s user interface.
- [Automatic trait tracking](automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitenvironment)*