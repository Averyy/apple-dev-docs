# UTTypeDirectory

**Framework**: Uniform Type Identifiers  
**Kind**: var  
**Role**: Global Variable

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

```c
extern UTType * const UTTypeDirectory;
```

## Discussion

The identifier for this type is `public.directory`.

This type conforms to [`UTTypeItem`](./uttypeitem.md).

## See Also

### Apple file system objects
- [UTTypeSymbolicLink](./uttypesymboliclink.md)
  A type that represents a symbolic link.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uniformtypeidentifiers/uttypedirectory)*