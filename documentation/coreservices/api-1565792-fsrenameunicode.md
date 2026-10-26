# FSRenameUnicode

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr FSRenameUnicode(const FSRef *ref, UniCharCount nameLength, const UniChar *name, TextEncoding textEncodingHint, FSRef *newRef);
```

## See Also

### Moving and Renaming Files or Directories
- [PBMoveObjectSync](./api-1565935-pbmoveobjectsync.md)
- [FSMoveObjectAsync](./api-1566762-fsmoveobjectasync.md)
- [FSMoveObject](./api-1566291-fsmoveobject.md)
- [PBMoveObjectAsync](./api-1566270-pbmoveobjectasync.md)
- [PBRenameUnicodeAsync](./api-1566334-pbrenameunicodeasync.md)
- [PBRenameUnicodeSync](./api-1566879-pbrenameunicodesync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565792-fsrenameunicode)*