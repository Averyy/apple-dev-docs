# standardAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance settings to use for a standard-height toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var standardAppearance: UIToolbarAppearance { get set }
```

```objc
@property (nonatomic, copy, readwrite) UIToolbarAppearance * standardAppearance;
```

## Discussion

The default value of this property is an appearance object containing the system’s default appearance settings.

## See Also

### Customizing appearance
- [var compactAppearance: UIToolbarAppearance?](./compactappearance.md)
  The appearance settings to use for a compact-height toolbar.
- [var scrollEdgeAppearance: UIToolbarAppearance?](./scrolledgeappearance.md)
  The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [var compactScrollEdgeAppearance: UIToolbarAppearance?](./compactscrolledgeappearance.md)
  The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [var isTranslucent: Bool](./istranslucent.md)
  A Boolean value that indicates whether the toolbar is translucent.
- [Legacy customizations](../uitoolbar-legacy-customizations.md)
  Customize appearance information directly on the toolbar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/standardappearance)*