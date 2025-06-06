# volume

**Framework**: Uniform Type Identifiers  
**Kind**: property

A type that represents the root folder of a volume or mount point.

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
static var volume: UTType { get }
```

#### Discussion

The identifier for this type is `public.volume`.

This type conforms to [`UTTypeFolder`](uttypefolder.md).

## See Also

- [static var directory: UTType](uttype-swift.struct/directory.md)
  A type that represents a file system directory, including packages and folders.
- [static var symbolicLink: UTType](uttype-swift.struct/symboliclink.md)
  A type that represents a symbolic link.
- [static var mountPoint: UTType](uttype-swift.struct/mountpoint.md)
  A type that represents a volume mount point.
- [static var aliasFile: UTType](uttype-swift.struct/aliasfile.md)
  A type that represents an alias file.
- [static var folder: UTType](uttype-swift.struct/folder.md)
  A type that represents a user-browsable directory.
- [static var diskImage: UTType](uttype-swift.struct/diskimage.md)
  A type that represents a data item that’s mountable as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/volume)*