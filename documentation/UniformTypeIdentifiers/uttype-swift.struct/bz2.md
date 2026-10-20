# bz2

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

A type that represents a bzip2 archive.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static var bz2: UTType { get }
```

#### Discussion

The identifier for this type is `public.bzip2-archive`.

This type conforms to [`UTTypeData`](../uttypedata.md) and [`UTTypeArchive`](../uttypearchive.md).

## See Also

### Compressed archives
- [static var archive: UTType](./archive.md)
  A base type that represents an archive of files and directories.
- [static var zip: UTType](./zip.md)
  A type that represents a zip archive.
- [static var gzip: UTType](./gzip.md)
  A type that represents a GNU zip archive.
- [static var appleArchive: UTType](./applearchive.md)
  A type that represents an Apple archive of files and directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/bz2)*