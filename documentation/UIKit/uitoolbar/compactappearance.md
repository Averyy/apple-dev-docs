# compactAppearance

**Framework**: UIKit  
**Kind**: property

The appearance settings to use for a compact-height toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var compactAppearance: UIToolbarAppearance? { get set }
```

#### Discussion

If the value of this property is `nil`, UIKit uses the same settings found in the [`standardAppearance`](uitoolbar/standardappearance.md) property.

## See Also

- [var standardAppearance: UIToolbarAppearance](uitoolbar/standardappearance.md)
  The appearance settings to use for a standard-height toolbar.
- [var scrollEdgeAppearance: UIToolbarAppearance?](uitoolbar/scrolledgeappearance.md)
  The appearance settings for a standard-height toolbar when the edge of scrollable content aligns with the edge of the toolbar.
- [var compactScrollEdgeAppearance: UIToolbarAppearance?](uitoolbar/compactscrolledgeappearance.md)
  The appearance settings for a compact-height toolbar when the edge of any scrollable content aligns with the edge of a compact-height toolbar.
- [var isTranslucent: Bool](uitoolbar/istranslucent.md)
  A Boolean value that indicates whether the toolbar is translucent.
- [Legacy customizations](uitoolbar-legacy-customizations.md)
  Customize appearance information directly on the toolbar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbar/compactappearance)*