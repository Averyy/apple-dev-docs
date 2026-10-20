# customizationIdentifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The customization identifier for the tab bar and sidebar for persistence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var customizationIdentifier: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * customizationIdentifier;
```

#### Discussion

The identifier is useful for when an app has multiple tab bar controllers, each with their own customizations. If the customization identifier is `nil`, a system default is used. Default is `nil`.

## See Also

### Customizing the tab bar appearance
- [var isTabBarHidden: Bool](./istabbarhidden.md)
  Determines if the active tab bar is currently hidden.
- [func setTabBarHidden(Bool, animated: Bool)](./settabbarhidden%28_,animated%29.md)
  Changes the active tab bar’s visibility with an option to animate the change.
- [var bottomAccessory: UITabAccessory?](./bottomaccessory.md)
  An optional bottom accessory of the tab bar controller.
- [func setBottomAccessory(UITabAccessory?, animated: Bool)](./setbottomaccessory%28_,animated%29.md)
  Sets a bottom accessory with an option to animate the change.
- [var compactTabIdentifiers: [String]?](./compacttabidentifiers.md)
  An optional filter to display only select root-level tabs when in a compact appearance.
- [var prominentTabIdentifier: String?](./prominenttabidentifier.md)
  The identifier of the tab that should be displayed as prominent. Where supported, the specified tab receives enhanced visual emphasis in the tab bar. If this property is nil, and there is a `UISearchTab` that could become prominent (when `automaticallyActivatesSearch = true`), then the search tab will receive the prominent treatment by default.
- [func setProminentTabIdentifier(String?, animated: Bool)](./setprominenttabidentifier%28_,animated%29.md)
  Sets the prominent tab identifier with an option to animate the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/customizationidentifier)*