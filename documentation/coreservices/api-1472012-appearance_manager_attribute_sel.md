# Appearance Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Appearance Manager.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltAppearanceAttr](./api-1472012-appearance_manager_attribute_sel/gestaltappearanceattr.md)
  The `Gestalt` selector passed to determine whether the Appearance Manager is present. Produces a 32-bit value whose bits you should test to determine which Appearance Manager features are available.
- [gestaltAppearanceExists](./api-1472012-appearance_manager_attribute_sel/gestaltappearanceexists.md)
- [gestaltAppearanceCompatMode](./api-1472012-appearance_manager_attribute_sel/gestaltappearancecompatmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472012-appearance_manager_attribute_sel)*