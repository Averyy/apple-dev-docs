# gestaltAppearanceExists

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltAppearanceExists = 0
```

#### Discussion

If this bit is set, Appearance Manager functions are available. To determine which version of the Appearance Manager is installed, check for the presence of the `Gestalt` selector `gestaltAppearanceVersion`. If this bit is not set, Appearance Manager functions are not available. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472012-appearance_manager_attribute_sel/gestaltappearanceexists)*