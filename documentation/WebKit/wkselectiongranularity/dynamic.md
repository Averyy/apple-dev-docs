# WKSelectionGranularity.dynamic

**Framework**: WebKit  
**Kind**: case  
**Role**: Case

Granularity that varies automatically depending on the selection.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This property is ignored; selection granularity is always `character`.

## Declaration

```swift
case dynamic
```

```c
WKSelectionGranularityDynamic
```

## Discussion

When the selection is within a single block, the granularity may be single character. When the selection is not confined to a single block, the granularity may be a single block.

## See Also

### Getting the Granularity Options
- [WKSelectionGranularity.character](./character.md)
  Granularity that allows the user to place selection endpoints at any character boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkselectiongranularity/dynamic)*