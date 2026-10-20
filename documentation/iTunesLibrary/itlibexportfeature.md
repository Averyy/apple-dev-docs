# ITLibExportFeature

**Framework**: iTunes Library  
**Kind**: enum  
**Role**: Enumeration

These constants describe the features that an iTunes library supports.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
enum ITLibExportFeature
```

```c
enum ITLibExportFeature : NSUInteger;
```

## Topics

### Export Features
- [ITLibExportFeature.none](./itlibexportfeature/none.md)
  The iTunes library doesn’t support any export features.
### Initializers
- [init?(rawValue: UInt)](./itlibexportfeature/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [var features: ITLibExportFeature](./itlibrary/features.md)
  A bitwise OR combination of the features of this library.
- [var musicFolderLocation: URL?](./itlibrary/musicfolderlocation.md)
  The location of the iTunes music folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibexportfeature)*