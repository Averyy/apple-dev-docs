# GetAliasSizeFromPtr

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Gets the size of an alias record referenced by a pointer.

**Availability**:
- macOS 10.4+ - Deprecated in 10.8

> **Deprecated**: Use [`CFDataGetLength(_:)`](../CoreFoundation/cfdatagetlength%28_%29.md), passing in the bookmark data.

## Declaration

```c
Size GetAliasSizeFromPtr(const AliasRecord *alias);
```

#### Return Value

The size of the alias record.

#### Discussion

This routine is thread safe. 

## Parameters

- `alias`: A pointer to the alias record from which to get the information.

## See Also

### Getting Alias Size
- [GetAliasSize](./api-1444419-getaliassize.md)
  Gets the size of an alias record referenced by a handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444380-getaliassizefromptr)*