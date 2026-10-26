# FSRef

**Framework**: Core Services  
**Kind**: struct  
**Role**: Structure

Identifies a directory or file, including a volume’s root directory.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct FSRef {
    ...
} FSRef;
```

#### Overview

> ❗ **Important**: [`FSRef`](./fsref.md) structures are designed to work with 32-bit inode numbers. Because APFS uses 64-bit inode numbers, interacting with APIs that return an [`FSRef`](./fsref.md) value or that take one or more [`FSRef`](./fsref.md) values as an argument may result in performance issues in APFS.

This data type’s purpose is similar to an [`FSSpec`](./fsspec.md) except that an `FSRef` is completely opaque. An `FSRef` contains whatever information is needed to find the given object; the internal structure of an `FSRef` is likely to vary based on the volume format, and may vary based on the particular object being identified.

The client of the File Manager cannot examine the contents of an `FSRef` to extract information about the parent directory or the object’s name. Similarly, an `FSRef` cannot be constructed directly by the client; the `FSRef` must be constructed and returned via the File Manager. There is no need to call the File Manager to dispose an `FSRef`.

To determine the volume, parent directory and name associated with an `FSRef`, or to get an equivalent `FSSpec`, use the [`FSGetCatalogInfo`](./api-1565356-fsgetcataloginfo.md) call.

## Topics

### Instance Properties
- [hidden](./fsref/api-1565674-hidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/fsref)*