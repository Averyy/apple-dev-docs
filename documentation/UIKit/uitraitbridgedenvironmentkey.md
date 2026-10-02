# UITraitBridgedEnvironmentKey

**Framework**: UIKit  
**Kind**: protocol

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
protocol UITraitBridgedEnvironmentKey : EnvironmentKey
```

## Topics

### Reading trait values
- [static func read(from: UITraitCollection) -> Self.Value](uitraitbridgedenvironmentkey/read(from:).md)
### Writing trait values
- [static func write(to: inout any UIMutableTraits, value: Self.Value)](uitraitbridgedenvironmentkey/write(to:value:).md)

## Relationships

### Inherits From
- [EnvironmentKey](../swiftui/environmentkey.md)

## See Also

- [Providing data to the view hierarchy with custom traits](providing-data-to-the-view-hierarchy-with-custom-traits.md)
  Share data that needs to flow hierarchically across multiple levels of your view hierarchy.
- [protocol UIMutableTraits](uimutabletraits-13ja5.md)
  A mutable container of traits.
- [typealias UITrait](uitrait-9423.md)
  A type representing a trait in a trait collection.
- [protocol UITraitDefinition](uitraitdefinition-64c15.md)
  A type representing a trait in a trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitbridgedenvironmentkey)*