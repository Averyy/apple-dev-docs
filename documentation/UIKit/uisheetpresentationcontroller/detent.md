# UISheetPresentationController.Detent

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that represents a height where a sheet naturally rests.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@MainActor
class Detent
```

```objc
@interface UISheetPresentationControllerDetent : NSObject
```

## Topics

### Creating a system detent
- [class func large() -> Self](./detent/large%28%29.md)
  Creates a system detent for a sheet at full height.
- [class func medium() -> Self](./detent/medium%28%29.md)
  Creates a system detent for a sheet that’s approximately half the height of the screen, and is inactive in compact height.
### Creating a custom detent
- [static func custom(identifier: UISheetPresentationController.Detent.Identifier?, resolver: (any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?) -> UISheetPresentationController.Detent](./detent/custom%28identifier,resolver%29.md)
  Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [func resolvedValue(in: any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?](./detent/resolvedvalue%28in%29.md)
  Resolves a detent to its value.
- [protocol UISheetPresentationControllerDetentResolutionContext](../uisheetpresentationcontrollerdetentresolutioncontext.md)
  A context for resolving custom detent values.
### Identifying a detent
- [var identifier: UISheetPresentationController.Detent.Identifier](./detent/identifier-swift.property.md)
  The identifier of the detent.
- [UISheetPresentationController.Detent.Identifier](./detent/identifier-swift.struct.md)
  Constants that identify system detent sizes.
### Instance Properties
- [var backgroundEffect: UIVisualEffect?](./detent/backgroundeffect.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Specifying the height
- [var detents: [UISheetPresentationController.Detent]](./detents.md)
  The array of heights where a sheet can rest.
- [var selectedDetentIdentifier: UISheetPresentationController.Detent.Identifier?](./selecteddetentidentifier.md)
  The identifier of the most recently selected detent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detent)*