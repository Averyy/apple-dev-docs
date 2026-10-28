# FSExchangeObjects

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

> **Deprecated**: In macOS 10.8 and later, use [`replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:`](../Foundation/filemanager/replaceitem%28at,withitemat,backupitemname,options,resultingitemurl%29.md) instead.

## Declaration

```c
OSErr FSExchangeObjects(const FSRef *ref, const FSRef *destRef);
```

## Discussion

To determine whether [`FSExchangeObjects`](./api-1565474-fsexchangeobjects.md) is supported in the current file system, call the [`FSGetVolumeParms`](./api-1565147-fsgetvolumeparms.md) function and check whether the [`bSupportsFSExchangeObjects`](./api-1565582-anonymous/bsupportsfsexchangeobjects.md) bit is set in the [`vMAttrib`](./getvolparmsinfobuffer/api-1565870-vmattrib.md) field of the resulting [`GetVolParmsInfoBuffer`](./getvolparmsinfobuffer.md) value.

> ❗ **Important**: [`FSExchangeObjects`](./api-1565474-fsexchangeobjects.md) is not supported in APFS.

## See Also

### Exchanging the Contents of Two Files
- [PBExchangeObjectsSync](./api-1566627-pbexchangeobjectssync.md)
- [PBExchangeObjectsAsync](./api-1566021-pbexchangeobjectsasync.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1565474-fsexchangeobjects)*