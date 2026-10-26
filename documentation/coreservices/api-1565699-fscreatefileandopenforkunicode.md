# FSCreateFileAndOpenForkUnicode

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.8

## Declaration

```c
OSStatus FSCreateFileAndOpenForkUnicode(const FSRef *parentRef, UniCharCount nameLength, const UniChar *name, FSCatalogInfoBitmap whichInfo, const FSCatalogInfo *catalogInfo, UniCharCount forkNameLength, const UniChar *forkName, SInt8 permissions, FSIORefNum *forkRefNum, FSRef *newRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565699-fscreatefileandopenforkunicode)*