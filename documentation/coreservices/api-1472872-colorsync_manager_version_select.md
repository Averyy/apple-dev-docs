# ColorSync Manager Version Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify version information for the ColorSync Manager.

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
- [gestaltColorMatchingVersion](./api-1472872-colorsync_manager_version_select/gestaltcolormatchingversion.md)
  The selector for obtaining version information. Use when calling the `Gestalt` function to determine whether the ColorSync Manager is available.
- [gestaltColorSync10](./api-1472872-colorsync_manager_version_select/gestaltcolorsync10.md)
  A `Gestalt` response value of `gestaltColorSync10` indicates version 1.0 of the ColorSync Manager is present. This version supports general purpose color matching only and does not provide QuickDraw-specific matching functions.
- [gestaltColorSync11](./api-1472872-colorsync_manager_version_select/gestaltcolorsync11.md)
  A `Gestalt` response value of `gestaltColorSync11` indicates version 1.0.3 of the ColorSync Manager is present.
- [gestaltColorSync104](./api-1472872-colorsync_manager_version_select/gestaltcolorsync104.md)
  A `Gestalt` response value of `gestaltColorSync104` indicates version 1.4 of the ColorSync Manager is present.
- [gestaltColorSync105](./api-1472872-colorsync_manager_version_select/gestaltcolorsync105.md)
  A `Gestalt` response value of `gestaltColorSync105` indicates version 1.5 of the ColorSync Manager is present.
- [gestaltColorSync20](./api-1472872-colorsync_manager_version_select/gestaltcolorsync20.md)
  A `Gestalt` response value of `gestaltColorSync20` indicates version 2.0 of the ColorSync Manager is present.
- [gestaltColorSync21](./api-1472872-colorsync_manager_version_select/gestaltcolorsync21.md)
  A `Gestalt` response value of `gestaltColorSync21` indicates version 2.1 of the ColorSync Manager is present.
- [gestaltColorSync211](./api-1472872-colorsync_manager_version_select/gestaltcolorsync211.md)
- [gestaltColorSync212](./api-1472872-colorsync_manager_version_select/gestaltcolorsync212.md)
- [gestaltColorSync213](./api-1472872-colorsync_manager_version_select/gestaltcolorsync213.md)
- [gestaltColorSync25](./api-1472872-colorsync_manager_version_select/gestaltcolorsync25.md)
  A `Gestalt` response value of `gestaltColorSync25` indicates version 2.5 of the ColorSync Manager is present.
- [gestaltColorSync26](./api-1472872-colorsync_manager_version_select/gestaltcolorsync26.md)
- [gestaltColorSync261](./api-1472872-colorsync_manager_version_select/gestaltcolorsync261.md)
- [gestaltColorSync30](./api-1472872-colorsync_manager_version_select/gestaltcolorsync30.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472872-colorsync_manager_version_select)*