# compactTabIdentifiers

**Framework**: UIKit  
**Kind**: property

An optional filter to display only select root-level tabs when in a compact appearance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var compactTabIdentifiers: [String]? { get set }
```

#### Discussion

The default value is is `nil`, which would make all tabs available.

## See Also

- [var isTabBarHidden: Bool](uitabbarcontroller/istabbarhidden.md)
  Determines if the active tab bar is currently hidden.
- [func setTabBarHidden(Bool, animated: Bool)](uitabbarcontroller/settabbarhidden(_:animated:).md)
  Changes the active tab bar’s visibility with an option to animate the change.
- [var bottomAccessory: UITabAccessory?](uitabbarcontroller/bottomaccessory.md)
  An optional bottom accessory of the tab bar controller.
- [func setBottomAccessory(UITabAccessory?, animated: Bool)](uitabbarcontroller/setbottomaccessory(_:animated:).md)
  Sets a bottom accessory with an option to animate the change.
- [var customizationIdentifier: String?](uitabbarcontroller/customizationidentifier.md)
  The customization identifier for the tab bar and sidebar for persistence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/compacttabidentifiers)*