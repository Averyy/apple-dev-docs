# compactAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance settings to use for a compact-height toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var compactAppearance: UIToolbarAppearance? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UIToolbarAppearance * compactAppearance;
```

#### Discussion

If the value of this property is `nil`, UIKit uses the same settings found in the [`standardAppearance`](./standardappearance.md) property.

## See Also

### Customizing appearance
- [var standardAppearance: UIToolbarAppearance](./standardappearance.md)
  The appearance settings to use for a standard-height toolbar.
- [var scrollEdgeAppearance: UIToolbarAppearance?](./scrolledgeappearance.md)
  The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [var compactScrollEdgeAppearance: UIToolbarAppearance?](./compactscrolledgeappearance.md)
  The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [var isTranslucent: Bool](./istranslucent.md)
  A Boolean value that indicates whether the toolbar is translucent.
- [Legacy customizations](../uitoolbar-legacy-customizations.md)
  Customize appearance information directly on the toolbar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/compactappearance)*