# SetAliasUserType

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets the user type for an alias record referenced by a handle.

**Availability**:
- macOS 10.4+ - Deprecated in 10.8

> **Deprecated**: Use [`CFURLSetTemporaryResourcePropertyForKey(_:_:_:)`](../CoreFoundation/cfurlsettemporaryresourcepropertyforkey%28_,_,_%29.md) to set your own temporary properties on the CFURL object. Then, to embed these properties in the bookmark data, pass the properties in the `resourcePropertiesToInclude` parameter of [`CFURLCreateBookmarkData(_:_:_:_:_:_:)`](../CoreFoundation/cfurlcreatebookmarkdata%28_,_,_,_,_,_%29.md). To prevent conflicts, it’s recommended that you create reverse DNS names for temporary property key strings.

## Declaration

```c
void SetAliasUserType(AliasHandle alias, OSType userType);
```

## Discussion

This routine is thread safe.

## Parameters

- `alias`: A handle to the alias record for which to set the user type.
- `userType`: The user type associated with the alias.

## See Also

### Getting and Setting Alias User Types
- [GetAliasUserType](./api-1444311-getaliasusertype.md)
  Gets the user type for an alias record referenced by a handle.
- [GetAliasUserTypeFromPtr](./api-1444345-getaliasusertypefromptr.md)
  Gets the user type for the alias record referenced by a pointer.
- [SetAliasUserTypeWithPtr](./api-1444309-setaliasusertypewithptr.md)
  Sets the user type for the alias record referenced by a pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444428-setaliasusertype)*