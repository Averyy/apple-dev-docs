# scrollEdgeAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var scrollEdgeAppearance: UIToolbarAppearance? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UIToolbarAppearance * scrollEdgeAppearance;
```

#### Discussion

When a navigation controller contains a toolbar and a scroll view, part of the scroll view’s content appears underneath the toolbar. If the edge of the scrolled content reaches the toolbar, UIKit applies the appearance settings in this property.

This property applies to standard-height toolbars. If the value of this property is `nil`, UIKit uses the value of the [`standardAppearance`](./standardappearance.md) property, modified to have a transparent background. If no navigation controller manages your toolbar, UIKit ignores this property and uses the tool bar’s standard appearance.

## See Also

### Customizing appearance
- [var standardAppearance: UIToolbarAppearance](./standardappearance.md)
  The appearance settings to use for a standard-height toolbar.
- [var compactAppearance: UIToolbarAppearance?](./compactappearance.md)
  The appearance settings to use for a compact-height toolbar.
- [var compactScrollEdgeAppearance: UIToolbarAppearance?](./compactscrolledgeappearance.md)
  The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [var isTranslucent: Bool](./istranslucent.md)
  A Boolean value that indicates whether the toolbar is translucent.
- [Legacy customizations](../uitoolbar-legacy-customizations.md)
  Customize appearance information directly on the toolbar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/scrolledgeappearance)*