# kHFSCatalogKeyMinimumLength

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.12+

## Declaration

```c
kHFSCatalogKeyMinimumLength = kHFSCatalogKeyMaximumLength - (kHFSMaxFileNameChars + 1) + sizeof(u_int8_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1646121-anonymous/khfscatalogkeyminimumlength)*