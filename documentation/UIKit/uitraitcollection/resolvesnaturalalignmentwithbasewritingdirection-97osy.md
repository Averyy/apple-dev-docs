# resolvesNaturalAlignmentWithBaseWritingDirection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Specifies the behavior for resolving `NSTextAlignment.natural` to the visual alignment.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, readonly) BOOL resolvesNaturalAlignmentWithBaseWritingDirection;
```

#### Discussion

When set to `true`, the resolved visual alignment is determined by the resolved base writing direction; otherwise, it is using the user’s preferred language.

## See Also

### Retrieving interface-related traits
- [var userInterfaceStyle: UIUserInterfaceStyle](./userinterfacestyle.md)
  The style associated with the user interface.
- [enum UIUserInterfaceStyle](../uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](./userinterfaceidiom.md)
  The user interface idiom of the trait collection.
- [enum UIUserInterfaceIdiom](../uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [var userInterfaceLevel: UIUserInterfaceLevel](./userinterfacelevel.md)
  The elevation level of the interface.
- [enum UIUserInterfaceLevel](../uiuserinterfacelevel.md)
  Constants that indicate the visual level for content in the window.
- [var layoutDirection: UITraitEnvironmentLayoutDirection](./layoutdirection.md)
  The layout direction associated with the current environment.
- [enum UITraitEnvironmentLayoutDirection](../uitraitenvironmentlayoutdirection.md)
  Constants that indicate the layout direction associated with the current environment.
- [var accessibilityContrast: UIAccessibilityContrast](./accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [enum UIAccessibilityContrast](../uiaccessibilitycontrast.md)
  Constants that indicate the accessibility contrast setting.
- [var legibilityWeight: UILegibilityWeight](./legibilityweight.md)
  The font weight to apply to text.
- [enum UILegibilityWeight](../uilegibilityweight.md)
  Constants that indicate the weight to apply to text in your interface.
- [var activeAppearance: UIUserInterfaceActiveAppearance](./activeappearance.md)
  A property that indicates whether a scene has an active appearance.
- [enum UIUserInterfaceActiveAppearance](../uiuserinterfaceactiveappearance.md)
  Constants that indicate whether the user interface has an active appearance.
- [var toolbarItemPresentationSize: UINSToolbarItemPresentationSize](./toolbaritempresentationsize.md)
  The presentation size of a toolbar item in an AppKit toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-97osy)*