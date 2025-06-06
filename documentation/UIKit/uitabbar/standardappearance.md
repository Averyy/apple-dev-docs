# standardAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings for a standard-height tab bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var standardAppearance: UITabBarAppearance { get set }
```

#### Discussion

The default value of this property is an appearance object containing the system’s default appearance settings.

## See Also

- [var scrollEdgeAppearance: UITabBarAppearance?](uitabbar/scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var leadingAccessoryView: UIView](uitabbar/leadingaccessoryview.md)
  The view at the leading edge of a tab bar on tvOS.
- [var trailingAccessoryView: UIView](uitabbar/trailingaccessoryview.md)
  The view at the trailing edge of a tab bar on tvOS.
- [var isTranslucent: Bool](uitabbar/istranslucent.md)
  A Boolean value that indicates whether the tab bar is translucent.
- [Legacy customizations](uitabbar-legacy-customizations.md)
  Customize appearance information directly on the tab bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/standardappearance)*