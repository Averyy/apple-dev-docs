# UIToolbarAppearance

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object for customizing the appearance of a toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIToolbarAppearance
```

```objc
@interface UIToolbarAppearance : UIBarAppearance
```

#### Overview

After creating a [`UIToolbarAppearance`](./uitoolbarappearance.md) object, use the methods and properties of this class to specify the appearance of items in the toolbar. Use the inherited properties from [`UIBarAppearance`](./uibarappearance.md) to configure the background and shadow attributes of the toolbar itself.

## Topics

### Configuring bar button items
- [var buttonAppearance: UIBarButtonItemAppearance](./uitoolbarappearance/buttonappearance.md)
  The appearance attributes for plain bar button items in the toolbar.
- [var prominentButtonAppearance: UIBarButtonItemAppearance](./uitoolbarappearance/prominentbuttonappearance.md)
  The appearance attributes for Prominent buttons.
### Configuring the Done button
- [var doneButtonAppearance: UIBarButtonItemAppearance](./uitoolbarappearance/donebuttonappearance.md)
  The appearance attributes for Done buttons.

## Relationships

### Inherits From
- [UIBarAppearance](./uibarappearance.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitoolbarappearance)*