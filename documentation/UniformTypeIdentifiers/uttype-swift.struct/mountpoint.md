# mountPoint

**Framework**: Uniform Type Identifiers  
**Kind**: property  
**Role**: Type Property

A type that represents a volume mount point.

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
static var mountPoint: UTType { get }
```

#### Discussion

A mount point that resolves to the root directory of a volume.

The identifier for this type is `public.mount-point`.

This type conforms to [`UTTypeItem`](../uttypeitem.md) and [`UTTypeResolvable`](../uttyperesolvable.md).

## See Also

### Apple file system objects
- [static var directory: UTType](./directory.md)
  A type that represents a file system directory, including packages and folders.
- [static var symbolicLink: UTType](./symboliclink.md)
  A type that represents a symbolic link.
- [static var aliasFile: UTType](./aliasfile.md)
  A type that represents an alias file.
- [static var folder: UTType](./folder.md)
  A type that represents a user-browsable directory.
- [static var volume: UTType](./volume.md)
  A type that represents the root folder of a volume or mount point.
- [static var diskImage: UTType](./diskimage.md)
  A type that represents a data item that’s mountable as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/mountpoint)*