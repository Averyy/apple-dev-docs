# appleArchive

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type that represents an Apple archive of files and directories.

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
static var appleArchive: UTType { get }
```

#### Discussion

The identifier for this type is `com.apple.archive`.

This type conforms to [`data`](uttype-swift.struct/data.md) and [`archive`](uttype-swift.struct/archive.md).

## See Also

- [static var archive: UTType](uttype-swift.struct/archive.md)
  A base type that represents an archive of files and directories.
- [static var zip: UTType](uttype-swift.struct/zip.md)
  A type that represents a zip archive.
- [static var gzip: UTType](uttype-swift.struct/gzip.md)
  A type that represents a GNU zip archive.
- [static var bz2: UTType](uttype-swift.struct/bz2.md)
  A type that represents a bzip2 archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/applearchive)*