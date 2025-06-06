# WKSelectionGranularity

**Framework**: Webkit  
**Kind**: enum

The granularity with which the user can select and modify web view content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum WKSelectionGranularity
```

## Topics

### Getting the Granularity Options
- [WKSelectionGranularity.dynamic](wkselectiongranularity/dynamic.md)
  Granularity that varies automatically depending on the selection.
- [WKSelectionGranularity.character](wkselectiongranularity/character.md)
  Granularity that allows the user to place selection endpoints at any character boundary.
### Initializers
- [init?(rawValue: Int)](wkselectiongranularity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var selectionGranularity: WKSelectionGranularity](wkwebviewconfiguration/selectiongranularity.md)
  The level of granularity with which the user can interactively select web view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkselectiongranularity)*