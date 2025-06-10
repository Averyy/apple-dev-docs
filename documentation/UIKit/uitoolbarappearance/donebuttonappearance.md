# doneButtonAppearance

**Framework**: UIKit  
**Kind**: property

The appearance attributes for Done buttons.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var doneButtonAppearance: UIBarButtonItemAppearance { get set }
```

#### Discussion

Use this property to configure the appearance of bar button items that use the [`done`](uibarbuttonitem/style-swift.enum/done.md) style, when appropriate. If the toolbar doesn’t have a done button, setting the value of this property has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbarappearance/donebuttonappearance)*