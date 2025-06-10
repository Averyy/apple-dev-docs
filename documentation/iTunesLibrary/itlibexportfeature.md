# ITLibExportFeature

**Framework**: iTunes Library  
**Kind**: enum

These constants describe the features that an iTunes library supports.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
enum ITLibExportFeature
```

## Topics

### Export Features
- [ITLibExportFeature.none](itlibexportfeature/none.md)
  The iTunes library doesn’t support any export features.
### Initializers
- [init?(rawValue: UInt)](itlibexportfeature/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var features: ITLibExportFeature](itlibrary/features.md)
  A bitwise OR combination of the features of this library.
- [var musicFolderLocation: URL?](itlibrary/musicfolderlocation.md)
  The location of the iTunes music folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibexportfeature)*