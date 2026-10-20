# SecureDTGetPropertyRegion

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 15.0+

## Declaration

```c
int SecureDTGetPropertyRegion(const DTEntry entry, const char *propertyName, const void **propertyValue, unsigned int *propertySize, const vm_offset_t region_start, vm_size_t region_size);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/4395345-securedtgetpropertyregion)*