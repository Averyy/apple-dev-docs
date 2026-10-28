# directory

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

A type that represents a file system directory, including packages and folders.

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
static var directory: UTType { get }
```

## Discussion

The identifier for this type is `public.directory`.

This type conforms to [`UTTypeItem`](../uttypeitem.md).

## See Also

### Apple file system objects
- [static var symbolicLink: UTType](./symboliclink.md)
  A type that represents a symbolic link.
- [static var mountPoint: UTType](./mountpoint.md)
  A type that represents a volume mount point.
- [static var aliasFile: UTType](./aliasfile.md)
  A type that represents an alias file.
- [static var folder: UTType](./folder.md)
  A type that represents a user-browsable directory.
- [static var volume: UTType](./volume.md)
  A type that represents the root folder of a volume or mount point.
- [static var diskImage: UTType](./diskimage.md)
  A type that represents a data item that’s mountable as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/directory)*