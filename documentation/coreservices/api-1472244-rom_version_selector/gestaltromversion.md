# gestaltROMVersion

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltROMVersion = 'romv'
```

#### Discussion

This selector is NOT supported in Carbon.

The selector you pass to the `Gestalt` function to determine the version number of the installed ROM (in the low-order word of the return value).

Never infer the existence of certain hardware or software features from the responses that `Gestalt` returns when you pass it this selector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472244-rom_version_selector/gestaltromversion)*