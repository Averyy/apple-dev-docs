# standardAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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
var standardAppearance: UITabBarAppearance { get set }
```

```objc
@property (nonatomic, copy, readwrite) UITabBarAppearance * standardAppearance;
```

#### Discussion

The default value of this property is an appearance object containing the system’s default appearance settings.

## See Also

### Customizing tab bar appearance
- [var scrollEdgeAppearance: UITabBarAppearance?](./scrolledgeappearance.md)
  The appearance settings for the tab bar when the edge of scrollable content aligns with the edge of the tab bar.
- [var leadingAccessoryView: UIView](./leadingaccessoryview.md)
  The view at the leading edge of a tab bar on tvOS.
- [var trailingAccessoryView: UIView](./trailingaccessoryview.md)
  The view at the trailing edge of a tab bar on tvOS.
- [var isTranslucent: Bool](./istranslucent.md)
  A Boolean value that indicates whether the tab bar is translucent.
- [Legacy customizations](../uitabbar-legacy-customizations.md)
  Customize appearance information directly on the tab bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbar/standardappearance)*