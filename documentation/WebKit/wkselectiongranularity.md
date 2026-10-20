# WKSelectionGranularity

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

The granularity with which the user can select and modify web view content.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This property is ignored; selection granularity is always `character`.

## Declaration

```swift
enum WKSelectionGranularity
```

```c
enum WKSelectionGranularity : NSInteger;
```

## Topics

### Getting the Granularity Options
- [WKSelectionGranularity.dynamic](./wkselectiongranularity/dynamic.md)
  Granularity that varies automatically depending on the selection.
- [WKSelectionGranularity.character](./wkselectiongranularity/character.md)
  Granularity that allows the user to place selection endpoints at any character boundary.
### Initializers
- [init?(rawValue: Int)](./wkselectiongranularity/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting selection granularity
- [var selectionGranularity: WKSelectionGranularity](./wkwebviewconfiguration/selectiongranularity.md)
  The level of granularity with which the user can interactively select web view content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkselectiongranularity)*