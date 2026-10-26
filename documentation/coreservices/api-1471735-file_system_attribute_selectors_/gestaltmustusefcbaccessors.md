# gestaltMustUseFCBAccessors

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

If this bit is set in the `response` parameter, the File Manager no longer supports the low memory globals `FCBSPtr` and `FSFCBLen`. All access to file or fork control blocks must use the File System Manager utility functions instead. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltMustUseFCBAccessors = 13
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471735-file_system_attribute_selectors_/gestaltmustusefcbaccessors)*