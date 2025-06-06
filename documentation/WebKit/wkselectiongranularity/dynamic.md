# WKSelectionGranularity.dynamic

**Framework**: Webkit  
**Kind**: case

Granularity that varies automatically depending on the selection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case dynamic
```

#### Discussion

When the selection is within a single block, the granularity may be single character. When the selection is not confined to a single block, the granularity may be a single block.

## See Also

- [WKSelectionGranularity.character](wkselectiongranularity/character.md)
  Granularity that allows the user to place selection endpoints at any character boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkselectiongranularity/dynamic)*