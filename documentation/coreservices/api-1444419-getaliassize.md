# GetAliasSize

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the size of an alias record referenced by a handle.

**Availability**:
- macOS 10.4+ - Deprecated in 10.8

> **Deprecated**: Use [`CFDataGetLength(_:)`](../CoreFoundation/cfdatagetlength%28_%29.md), passing in the bookmark data.

## Declaration

```c
Size GetAliasSize(AliasHandle alias);
```

#### Return Value

The size of the alias record.

#### Discussion

The returned size is smaller than the size returned by the function `GetHandleSize` if any custom data is added. This routine is thread safe.

## Parameters

- `alias`: A handle to the alias record from which to get the information.

## See Also

### Getting Alias Size
- [GetAliasSizeFromPtr](./api-1444380-getaliassizefromptr.md)
  Gets the size of an alias record referenced by a pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444419-getaliassize)*