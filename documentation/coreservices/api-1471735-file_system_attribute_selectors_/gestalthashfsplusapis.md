# gestaltHasHFSPlusAPIs

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltHasHFSPlusAPIs = 12
```

## Discussion

If this bit is set in the `response` parameter, the File Manager supports the HFS Plus APIs. Individual file systems may or may not implement the HFS Plus APIs. However, if this bit is set, the File Manager will emulate the HFS Plus APIs for file systems that do not implement them. Call the functions `PBHGetVolParmsSync` or `PBHGetVolParmsAsync` to determine whether the HFS Plus APIs are directly supported on a given volume. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471735-file_system_attribute_selectors_/gestalthashfsplusapis)*