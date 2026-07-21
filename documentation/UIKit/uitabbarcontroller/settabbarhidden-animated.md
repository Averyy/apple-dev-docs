# setTabBarHidden(_:animated:)

**Framework**: UIKit  
**Kind**: method

Changes the active tab bar’s visibility with an option to animate the change.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func setTabBarHidden(_ hidden: Bool, animated: Bool)
```

## See Also

- [var isTabBarHidden: Bool](uitabbarcontroller/istabbarhidden.md)
  Determines if the active tab bar is currently hidden.
- [var bottomAccessory: UITabAccessory?](uitabbarcontroller/bottomaccessory.md)
  An optional bottom accessory of the tab bar controller.
- [func setBottomAccessory(UITabAccessory?, animated: Bool)](uitabbarcontroller/setbottomaccessory(_:animated:).md)
  Sets a bottom accessory with an option to animate the change.
- [var compactTabIdentifiers: [String]?](uitabbarcontroller/compacttabidentifiers.md)
  An optional filter to display only select root-level tabs when in a compact appearance.
- [var customizationIdentifier: String?](uitabbarcontroller/customizationidentifier.md)
  The customization identifier for the tab bar and sidebar for persistence.
- [var prominentTabIdentifier: String?](uitabbarcontroller/prominenttabidentifier.md)
  The identifier of the tab that should be displayed as prominent. Where supported, the specified tab receives enhanced visual emphasis in the tab bar. If this property is nil, and there is a `UISearchTab` that could become prominent (when `automaticallyActivatesSearch = true`), then the search tab will receive the prominent treatment by default.
- [func setProminentTabIdentifier(String?, animated: Bool)](uitabbarcontroller/setprominenttabidentifier(_:animated:).md)
  Sets the prominent tab identifier with an option to animate the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/settabbarhidden(_:animated:))*