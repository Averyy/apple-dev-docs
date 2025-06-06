# scrollEdgeAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var scrollEdgeAppearance: UITabBarAppearance? { get set }
```

#### Discussion

When a tab bar controller contains a tab bar and a scroll view, part of the scroll view’s content appears underneath the tab bar. If the edge of the scrolled content reaches that bar, UIKit applies the appearance settings in this property.

If the value of this property is `nil`, UIKit uses the value of the tab bar’s [`standardAppearance`](uitabbar/standardappearance.md) property, modified to have a transparent background. If no tab bar controller manages your tab bar, UIKit ignores this property and uses the tab bar’s standard appearance.

You can customize the appearance for specific tab bar items with the [`scrollEdgeAppearance`](uitabbaritem/scrolledgeappearance.md) property of [`UITabBarItem`](uitabbaritem.md).

## See Also

- [var standardAppearance: UITabBarAppearance](uitabbar/standardappearance.md)
  The appearance settings for a standard-height tab bar.
- [var leadingAccessoryView: UIView](uitabbar/leadingaccessoryview.md)
  The view at the leading edge of a tab bar on tvOS.
- [var trailingAccessoryView: UIView](uitabbar/trailingaccessoryview.md)
  The view at the trailing edge of a tab bar on tvOS.
- [var isTranslucent: Bool](uitabbar/istranslucent.md)
  A Boolean value that indicates whether the tab bar is translucent.
- [Legacy customizations](uitabbar-legacy-customizations.md)
  Customize appearance information directly on the tab bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/scrolledgeappearance)*