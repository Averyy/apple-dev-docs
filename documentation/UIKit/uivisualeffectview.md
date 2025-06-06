# UIVisualEffectView

**Framework**: UIKit  
**Kind**: class

An object that implements some complex visual effects.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIVisualEffectView
```

#### Overview

Depending on the desired effect, the effect may affect content layered behind the view or content added to the visual effect view’s [`contentView`](uivisualeffectview/contentview.md). Apply a visual effect view to an existing view and then apply a [`UIBlurEffect`](uiblureffect.md) or [`UIVibrancyEffect`](uivibrancyeffect.md) object to apply a blur or vibrancy effect to the existing view. After you add the visual effect view to the view hierarchy, add any subviews to the [`contentView`](uivisualeffectview/contentview.md) property of the visual effect view. Don’t add subviews directly to the visual effect view itself.

##### Set the Correct Alpha Value

When using the [`UIVisualEffectView`](uivisualeffectview.md) class, avoid alpha values that are less than 1. Creating views that are partially transparent causes the system to combine the view and all the associated subviews during an offscreen render pass. [`UIVisualEffectView`](uivisualeffectview.md) objects need to be combined as part of the content they’re layered on top of in order to look correct. Setting the alpha to less than 1 on the visual effect view or any of its superviews causes many effects to look incorrect or not show up at all.

##### Use Masks with a Visual Effect View

Masks directly applied to a [`UIVisualEffectView`](uivisualeffectview.md) are forwarded to the internal views that provide the visual effect, including the [`contentView`](uivisualeffectview/contentview.md) itself. You can also apply masks directly to the [`contentView`](uivisualeffectview/contentview.md). Applying a mask to a superview of a [`UIVisualEffectView`](uivisualeffectview.md) object causes the effect to fail, and an exception is thrown.

Any mask provided to [`UIVisualEffectView`](uivisualeffectview.md) isn’t the view that actually performs the mask. UIKit makes a copy of the view and applies it to each subview. To reflect a size change to the mask, you must apply the change to the original mask and reset it on the effect view.

##### Capture a Snapshot of a Visual Effect View

Many effects require support from the window that hosts the [`UIVisualEffectView`](uivisualeffectview.md). Attempting to take a snapshot of only the [`UIVisualEffectView`](uivisualeffectview.md) results in a snapshot that doesn’t contain the effect. To take a snapshot of a view hierarchy that contains a [`UIVisualEffectView`](uivisualeffectview.md), you must take a snapshot of the entire [`UIWindow`](uiwindow.md) or [`UIScreen`](uiscreen.md) that contains it.

## Topics

### Creating a visual effect view
- [init(effect: UIVisualEffect?)](uivisualeffectview/init(effect:).md)
  Creates a new visual effect view with the designated visual effect.
- [init?(coder: NSCoder)](uivisualeffectview/init(coder:).md)
  Creates a visual effect view from data in an unarchiver.
### Retrieving view information
- [var contentView: UIView](uivisualeffectview/contentview.md)
  A view object that can have a visual effect view added to it.
- [var effect: UIVisualEffect?](uivisualeffectview/effect.md)
  The visual effect provided by the view.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIVisualEffect](uivisualeffect.md)
  An initializer for visual effect views and blur and vibrancy effect objects.
- [class UIVibrancyEffect](uivibrancyeffect.md)
  An object that amplifies and adjusts the color of the content layered behind a visual effect view.
- [class UIBlurEffect](uiblureffect.md)
  An object that applies a blurring effect to the content layered behind a visual effect view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uivisualeffectview)*