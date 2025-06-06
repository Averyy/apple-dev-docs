# trailingAccessoryView

**Framework**: UIKit  
**Kind**: property

The view at the trailing edge of a tab bar on tvOS.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var trailingAccessoryView: UIView { get }
```

#### Discussion

Use this property to integrate a custom view at the trailing edge of your tab bar interface. Use this view to display a custom logo or give access to custom accessories in your app.

## See Also

- [var standardAppearance: UITabBarAppearance](uitabbar/standardappearance.md)
  The appearance settings for a standard-height tab bar.
- [var scrollEdgeAppearance: UITabBarAppearance?](uitabbar/scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var leadingAccessoryView: UIView](uitabbar/leadingaccessoryview.md)
  The view at the leading edge of a tab bar on tvOS.
- [var isTranslucent: Bool](uitabbar/istranslucent.md)
  A Boolean value that indicates whether the tab bar is translucent.
- [Legacy customizations](uitabbar-legacy-customizations.md)
  Customize appearance information directly on the tab bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/trailingaccessoryview)*