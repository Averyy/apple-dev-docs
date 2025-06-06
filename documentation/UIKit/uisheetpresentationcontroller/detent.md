# UISheetPresentationController.Detent

**Framework**: UIKit  
**Kind**: class

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

## Topics

### Creating a system detent
- [class func large() -> Self](uisheetpresentationcontroller/detent/large.md)
  Creates a system detent for a sheet at full height.
- [class func medium() -> Self](uisheetpresentationcontroller/detent/medium.md)
  Creates a system detent for a sheet that’s approximately half the height of the screen, and is inactive in compact height.
### Creating a custom detent
- [static func custom(identifier: UISheetPresentationController.Detent.Identifier?, resolver: (any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?) -> UISheetPresentationController.Detent](uisheetpresentationcontroller/detent/custom(identifier:resolver:).md)
  Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [func resolvedValue(in: any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?](uisheetpresentationcontroller/detent/resolvedvalue(in:).md)
  Resolves a detent to its value.
- [protocol UISheetPresentationControllerDetentResolutionContext](uisheetpresentationcontrollerdetentresolutioncontext.md)
  A context for resolving custom detent values.
### Identifying a detent
- [var identifier: UISheetPresentationController.Detent.Identifier](uisheetpresentationcontroller/detent/identifier-swift.property.md)
  The identifier of the detent.
- [UISheetPresentationController.Detent.Identifier](uisheetpresentationcontroller/detent/identifier-swift.struct.md)
  Constants that identify system detent sizes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var detents: [UISheetPresentationController.Detent]](uisheetpresentationcontroller/detents.md)
  The array of heights where a sheet can rest.
- [var selectedDetentIdentifier: UISheetPresentationController.Detent.Identifier?](uisheetpresentationcontroller/selecteddetentidentifier.md)
  The identifier of the most recently selected detent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detent)*