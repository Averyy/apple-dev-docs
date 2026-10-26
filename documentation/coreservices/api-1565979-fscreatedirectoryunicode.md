# FSCreateDirectoryUnicode

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr FSCreateDirectoryUnicode(const FSRef *parentRef, UniCharCount nameLength, const UniChar *name, FSCatalogInfoBitmap whichInfo, const FSCatalogInfo *catalogInfo, FSRef *newRef, FSSpecPtr newSpec, UInt32 *newDirID);
```

## See Also

### Creating Directories
- [PBCreateDirectoryUnicodeSync](./api-1565315-pbcreatedirectoryunicodesync.md)
- [PBCreateDirectoryUnicodeAsync](./api-1565107-pbcreatedirectoryunicodeasync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565979-fscreatedirectoryunicode)*