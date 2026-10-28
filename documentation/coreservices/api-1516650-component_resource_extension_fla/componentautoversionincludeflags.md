# componentAutoVersionIncludeFlags

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
componentAutoVersionIncludeFlags = (1 << 2)
```

## Discussion

Specify this flag if you want the Component Manager to include the `componentFlags` field of the component description structure when it searches for identical components in the process of performing automatic version control for your component. If you do not specify this flag, the Component Manager searches only the `componentType`, `componentSubType`, and `componentManufacturer` fields.

Note that the setting of the `componentAutoVersionIncludeFlags` flag affects automatic version control only and does not affect the search operations performed by `FindNextComponent` and `CountComponents`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516650-component_resource_extension_fla/componentautoversionincludeflags)*