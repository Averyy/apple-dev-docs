# RegistryPropertySet

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.6+

## Declaration

```c
OSStatus RegistryPropertySet(const RegEntryID *entryID, const RegPropertyName *propertyName, const void *propertyValue, RegPropertyValueSize propertySize);
```

## See Also

### Property Management
- [RegistryPropertyCreate](./api-1573027-registrypropertycreate.md)
- [RegistryPropertyDelete](./api-1573057-registrypropertydelete.md)
- [RegistryPropertyGet](./api-1573042-registrypropertyget.md)
- [RegistryPropertyGetMod](./api-1573058-registrypropertygetmod.md)
- [RegistryPropertyGetSize](./api-1573059-registrypropertygetsize.md)
- [RegistryPropertyIterate](./api-1573092-registrypropertyiterate.md)
- [RegistryPropertyIterateCreate](./api-1573069-registrypropertyiteratecreate.md)
- [RegistryPropertyIterateDispose](./api-1573062-registrypropertyiteratedispose.md)
- [RegistryPropertySetMod](./api-1573127-registrypropertysetmod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1573129-registrypropertyset)*