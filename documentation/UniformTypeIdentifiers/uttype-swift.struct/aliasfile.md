# aliasFile

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type that represents an alias file.

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
static var aliasFile: UTType { get }
```

#### Discussion

This type conforms to both [`data`](uttype-swift.struct/data.md) and [`resolvable`](uttype-swift.struct/resolvable.md), and its identifier is `com.apple.alias-file`.

## See Also

- [static var directory: UTType](uttype-swift.struct/directory.md)
  A type that represents a file system directory, including packages and folders.
- [static var symbolicLink: UTType](uttype-swift.struct/symboliclink.md)
  A type that represents a symbolic link.
- [static var mountPoint: UTType](uttype-swift.struct/mountpoint.md)
  A type that represents a volume mount point.
- [static var folder: UTType](uttype-swift.struct/folder.md)
  A type that represents a user-browsable directory.
- [static var volume: UTType](uttype-swift.struct/volume.md)
  A type that represents the root folder of a volume or mount point.
- [static var diskImage: UTType](uttype-swift.struct/diskimage.md)
  A type that represents a data item that’s mountable as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/aliasfile)*