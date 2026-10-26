# gestaltHasExtendedDiskInit

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltHasExtendedDiskInit = 6
```

#### Discussion

If this bit is set in the `response` parameter, the extended Disk Initialization Package functions are present. These are the `DIXFormat`, `DIXZero`, or `DIReformat` functions. See the *Guide to the File System Manager* for more information about the Disk Initialization Package interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471227-file_system_attribute_selectors/gestalthasextendeddiskinit)*