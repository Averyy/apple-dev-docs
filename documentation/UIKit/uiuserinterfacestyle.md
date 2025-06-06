# UIUserInterfaceStyle

**Framework**: UIKit  
**Kind**: enum

Constants that indicate the interface style for the app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum UIUserInterfaceStyle
```

## Topics

### Interface styles
- [UIUserInterfaceStyle.unspecified](uiuserinterfacestyle/unspecified.md)
  An unspecified interface style.
- [UIUserInterfaceStyle.light](uiuserinterfacestyle/light.md)
  The light interface style.
- [UIUserInterfaceStyle.dark](uiuserinterfacestyle/dark.md)
  The dark interface style.
### Initializers
- [init(ColorScheme?)](uiuserinterfacestyle/init(_:).md)
  Creates a user interface style from the specified SwiftUI color scheme.
- [init?(rawValue: Int)](uiuserinterfacestyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var userInterfaceStyle: UIUserInterfaceStyle](uitraitcollection/userinterfacestyle.md)
  The style associated with the user interface.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](uitraitcollection/userinterfaceidiom.md)
  The user interface idiom of the trait collection.
- [enum UIUserInterfaceIdiom](uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [var userInterfaceLevel: UIUserInterfaceLevel](uitraitcollection/userinterfacelevel.md)
  The elevation level of the interface.
- [enum UIUserInterfaceLevel](uiuserinterfacelevel.md)
  Constants that indicate the visual level for content in the window.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle)*