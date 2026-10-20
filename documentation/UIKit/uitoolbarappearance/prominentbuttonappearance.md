# prominentButtonAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The appearance attributes for Prominent buttons.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var prominentButtonAppearance: UIBarButtonItemAppearance { get set }
```

```objc
@property (nonatomic, copy, readwrite) UIBarButtonItemAppearance * prominentButtonAppearance;
```

#### Discussion

Use this property to configure the appearance of bar button items that use `UIBarButtonItemStyleProminent`. If the navigation bar doesn’t have any buttons using this style, this property has no effect.

## See Also

### Configuring bar button items
- [var buttonAppearance: UIBarButtonItemAppearance](./buttonappearance.md)
  The appearance attributes for plain bar button items in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbarappearance/prominentbuttonappearance)*