# UIUserInterfaceLevel

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the visual level for content in the window.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum UIUserInterfaceLevel
```

## Topics

### Interface levels
- [UIUserInterfaceLevel.unspecified](uiuserinterfacelevel/unspecified.md)
  An unspecified interface level.
- [UIUserInterfaceLevel.base](uiuserinterfacelevel/base.md)
  The level for your window’s main content.
- [UIUserInterfaceLevel.elevated](uiuserinterfacelevel/elevated.md)
  The level for content visually above your window’s main content.
### Initializers
- [init?(rawValue: Int)](uiuserinterfacelevel/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var userInterfaceStyle: UIUserInterfaceStyle](uitraitcollection/userinterfacestyle.md)
  The style associated with the user interface.
- [enum UIUserInterfaceStyle](uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](uitraitcollection/userinterfaceidiom.md)
  The user interface idiom of the trait collection.
- [enum UIUserInterfaceIdiom](uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [var userInterfaceLevel: UIUserInterfaceLevel](uitraitcollection/userinterfacelevel.md)
  The elevation level of the interface.
- [var layoutDirection: UITraitEnvironmentLayoutDirection](uitraitcollection/layoutdirection.md)
  The layout direction associated with the current environment.
- [enum UITraitEnvironmentLayoutDirection](uitraitenvironmentlayoutdirection.md)
  Constants that indicate the layout direction associated with the current environment.
- [var accessibilityContrast: UIAccessibilityContrast](uitraitcollection/accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [enum UIAccessibilityContrast](uiaccessibilitycontrast.md)
  Constants that indicate the accessibility contrast setting.
- [var legibilityWeight: UILegibilityWeight](uitraitcollection/legibilityweight.md)
  The font weight to apply to text.
- [enum UILegibilityWeight](uilegibilityweight.md)
  Constants that indicate the weight to apply to text in your interface.
- [var activeAppearance: UIUserInterfaceActiveAppearance](uitraitcollection/activeappearance.md)
  A property that indicates whether the user interface has an active appearance.
- [enum UIUserInterfaceActiveAppearance](uiuserinterfaceactiveappearance.md)
  Constants that indicate whether the user interface has an active appearance.
- [var toolbarItemPresentationSize: UINSToolbarItemPresentationSize](uitraitcollection/toolbaritempresentationsize.md)
  The presentation size of a toolbar item in an AppKit toolbar.
- [enum UINSToolbarItemPresentationSize](uinstoolbaritempresentationsize.md)
  Constants that specify the presentation size of a toolbar item in an AppKit toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuserinterfacelevel)*