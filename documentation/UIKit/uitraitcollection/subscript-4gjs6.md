# subscript(_:)

**Framework**: UIKit  
**Kind**: subscript

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
subscript<T>(trait: T.Type) -> T.Value where T : _UICustomRawRepresentableTraitDefinition, T._CustomRawValue == CGFloat { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection/subscript(_:)-4gjs6)*