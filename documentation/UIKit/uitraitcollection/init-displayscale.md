# init(displayScale:)

**Framework**: UIKit  
**Kind**: init

Creates a trait collection that contains only a specified display scale.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init(displayScale scale: CGFloat)
```

#### Return Value

A new trait collection containing only a specified display scale trait.

## Parameters

- `scale`: The display scale for the new trait collection. Use   to specify a non-Retina display scale, and a value of   or greater to specify a Retina display scale.

## See Also

- [init()](uitraitcollection/init.md)
  Creates a trait collection whose traits are set to their default (unspecified) values.
- [init(userInterfaceIdiom: UIUserInterfaceIdiom)](uitraitcollection/init(userinterfaceidiom:).md)
  Creates a trait collection that contains only a specified interface idiom.
- [init(horizontalSizeClass: UIUserInterfaceSizeClass)](uitraitcollection/init(horizontalsizeclass:).md)
  Creates a trait collection that contains only a specified horizontal size class.
- [init(verticalSizeClass: UIUserInterfaceSizeClass)](uitraitcollection/init(verticalsizeclass:).md)
  Creates a trait collection that contains only a specified vertical size class.
- [init(userInterfaceStyle: UIUserInterfaceStyle)](uitraitcollection/init(userinterfacestyle:).md)
  Creates a trait collection that contains only the specified user interface style trait.
- [init(accessibilityContrast: UIAccessibilityContrast)](uitraitcollection/init(accessibilitycontrast:).md)
  Creates a trait collection that contains only the specified accessibility contrast trait.
- [init(userInterfaceLevel: UIUserInterfaceLevel)](uitraitcollection/init(userinterfacelevel:).md)
  Creates a trait collection that contains only the specified user interface level trait.
- [init(legibilityWeight: UILegibilityWeight)](uitraitcollection/init(legibilityweight:).md)
  Creates a trait collection that contains only the specified legibility weight trait.
- [init(forceTouchCapability: UIForceTouchCapability)](uitraitcollection/init(forcetouchcapability:).md)
  Creates a trait collection that contains only a specified force touch capability trait.
- [init(displayGamut: UIDisplayGamut)](uitraitcollection/init(displaygamut:).md)
  Creates a trait collection that contains only the specified display gamut trait.
- [init(layoutDirection: UITraitEnvironmentLayoutDirection)](uitraitcollection/init(layoutdirection:).md)
  Creates a trait collection that contains only the specified layout direction trait.
- [init(preferredContentSizeCategory: UIContentSizeCategory)](uitraitcollection/init(preferredcontentsizecategory:).md)
  Creates a trait collection that contains only the specified content size category trait.
- [init(activeAppearance: UIUserInterfaceActiveAppearance)](uitraitcollection/init(activeappearance:).md)
  Creates a trait collection that contains only the specified active appearance trait.
- [init(toolbarItemPresentationSize: UINSToolbarItemPresentationSize)](uitraitcollection/init(toolbaritempresentationsize:).md)
  Creates a trait collection that contains only the specified toolbar item presentation size trait.
- [init?(coder: NSCoder)](uitraitcollection/init(coder:).md)
  Creates a trait collection from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/init(displayscale:))*