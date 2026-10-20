# init(displayScale:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a trait collection that contains only a specified display scale.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(displayScale scale: CGFloat)
```

```objc
+ (UITraitCollection *) traitCollectionWithDisplayScale:(CGFloat) scale;
```

#### Return Value

A new trait collection containing only a specified display scale trait.

## Parameters

- `scale`: The display scale for the new trait collection. Use `1.0` to specify a non-Retina display scale, and a value of `2.0` or greater to specify a Retina display scale.

## See Also

### Creating a trait collection
- [init()](./init%28%29.md)
  Creates a trait collection whose traits are set to their default (unspecified) values.
- [init(userInterfaceIdiom: UIUserInterfaceIdiom)](./init%28userinterfaceidiom%29.md)
  Creates a trait collection that contains only a specified interface idiom.
- [init(horizontalSizeClass: UIUserInterfaceSizeClass)](./init%28horizontalsizeclass%29.md)
  Creates a trait collection that contains only a specified horizontal size class.
- [init(verticalSizeClass: UIUserInterfaceSizeClass)](./init%28verticalsizeclass%29.md)
  Creates a trait collection that contains only a specified vertical size class.
- [init(userInterfaceStyle: UIUserInterfaceStyle)](./init%28userinterfacestyle%29.md)
  Creates a trait collection that contains only the specified user interface style trait.
- [init(accessibilityContrast: UIAccessibilityContrast)](./init%28accessibilitycontrast%29.md)
  Creates a trait collection that contains only the specified accessibility contrast trait.
- [init(userInterfaceLevel: UIUserInterfaceLevel)](./init%28userinterfacelevel%29.md)
  Creates a trait collection that contains only the specified user interface level trait.
- [init(legibilityWeight: UILegibilityWeight)](./init%28legibilityweight%29.md)
  Creates a trait collection that contains only the specified legibility weight trait.
- [init(forceTouchCapability: UIForceTouchCapability)](./init%28forcetouchcapability%29.md)
  Creates a trait collection that contains only a specified force touch capability trait.
- [init(displayGamut: UIDisplayGamut)](./init%28displaygamut%29.md)
  Creates a trait collection that contains only the specified display gamut trait.
- [init(layoutDirection: UITraitEnvironmentLayoutDirection)](./init%28layoutdirection%29.md)
  Creates a trait collection that contains only the specified layout direction trait.
- [init(preferredContentSizeCategory: UIContentSizeCategory)](./init%28preferredcontentsizecategory%29.md)
  Creates a trait collection that contains only the specified content size category trait.
- [init(activeAppearance: UIUserInterfaceActiveAppearance)](./init%28activeappearance%29.md)
  Creates a trait collection that contains only the specified active appearance trait.
- [init(toolbarItemPresentationSize: UINSToolbarItemPresentationSize)](./init%28toolbaritempresentationsize%29.md)
  Creates a trait collection that contains only the specified toolbar item presentation size trait.
- [init(hdrHeadroomUsageLimit: UIHDRHeadroomUsageLimit)](./init%28hdrheadroomusagelimit%29-5zqph.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/init(displayscale:))*