# Mixed Mode Manager Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify version and feature availability information for the Mixed Mode Manager.

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
- [gestaltMixedModeAttr](./api-1472719-mixed_mode_manager_selectors/gestaltmixedmodeattr.md)
  The Gestalt selector you pass to determine what version of Mixed Mode Manager is present.
- [gestaltMixedModePowerPC](./api-1472719-mixed_mode_manager_selectors/gestaltmixedmodepowerpc.md)
  True if Mixed Mode supports PowerPC ABI calling conventions
- [gestaltPowerPCAware](./api-1472719-mixed_mode_manager_selectors/gestaltpowerpcaware.md)
  Old name for `gestaltMixedModePowerPC`
- [gestaltMixedModeCFM68K](./api-1472719-mixed_mode_manager_selectors/gestaltmixedmodecfm68k.md)
  True if Mixed Mode supports CFM-68K calling conventions 
- [gestaltMixedModeCFM68KHasTrap](./api-1472719-mixed_mode_manager_selectors/gestaltmixedmodecfm68khastrap.md)
  True if CFM-68K Mixed Mode implements `_MixedModeDispatch` (versions 1.0.1 and prior did not) 
- [gestaltMixedModeCFM68KHasState](./api-1472719-mixed_mode_manager_selectors/gestaltmixedmodecfm68khasstate.md)
  True if CFM-68K Mixed Mode exports Save/RestoreMixedModeState


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472719-mixed_mode_manager_selectors)*