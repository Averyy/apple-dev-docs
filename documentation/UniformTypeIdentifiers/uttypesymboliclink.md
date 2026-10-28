# UTTypeSymbolicLink

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

A type that represents a symbolic link.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```c
extern UTType * const UTTypeSymbolicLink;
```

## Discussion

The identifier for this type is `public.symlink`.

This type conforms to [`UTTypeItem`](./uttypeitem.md) and [`UTTypeResolvable`](./uttyperesolvable.md).

## See Also

### Apple file system objects
- [UTTypeDirectory](./uttypedirectory.md)
  A type that represents a file system directory, including packages and folders.
- [UTTypeMountPoint](./uttypemountpoint.md)
  A type that represents a volume mount point.
- [UTTypeAliasFile](./uttypealiasfile.md)
  A type that represents an alias file.
- [UTTypeFolder](./uttypefolder.md)
  A type that represents a user-browsable directory.
- [UTTypeVolume](./uttypevolume.md)
  A type that represents the root folder of a volume or mount point.
- [UTTypeDiskImage](./uttypediskimage.md)
  A type that represents a data item that’s mountable as a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypesymboliclink)*