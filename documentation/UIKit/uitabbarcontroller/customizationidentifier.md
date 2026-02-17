# customizationIdentifier

**Framework**: UIKit  
**Kind**: property

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

#### Discussion

The identifier is useful for when an app has multiple tab bar controllers, each with their own customizations. If the customization identifier is `nil`, a system default is used. Default is `nil`.

## See Also

- [var isTabBarHidden: Bool](uitabbarcontroller/istabbarhidden.md)
  Determines if the active tab bar is currently hidden.
- [func setTabBarHidden(Bool, animated: Bool)](uitabbarcontroller/settabbarhidden(_:animated:).md)
  Changes the active tab bar’s visibility with an option to animate the change.
- [var bottomAccessory: UITabAccessory?](uitabbarcontroller/bottomaccessory.md)
  An optional bottom accessory of the tab bar controller.
- [func setBottomAccessory(UITabAccessory?, animated: Bool)](uitabbarcontroller/setbottomaccessory(_:animated:).md)
  Sets a bottom accessory with an option to animate the change.
- [var compactTabIdentifiers: [String]?](uitabbarcontroller/compacttabidentifiers.md)
  An optional filter to display only select root-level tabs when in a compact appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/customizationidentifier)*