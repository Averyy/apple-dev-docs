# gestaltAppearanceVersion

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltAppearanceVersion = 'apvr'
```

#### Discussion

The `Gestalt` selector passed to determine which version of the Appearance Manager is installed. If this selector exists, Appearance Manager 1.0.1 (or later) is installed. The version number of the currently installed Appearance Manager is returned in the low-order word of the result in binary code decimal format (for example, version 1.0.1 would be 0x0101). If this selector does not exist but `gestaltAppearanceAttr` does, Appearance Manager 1.0 is installed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471531-appearance_manager_version_selec/gestaltappearanceversion)*