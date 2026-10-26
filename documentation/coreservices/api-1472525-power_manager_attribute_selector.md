# Power Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability for the Power Manager.

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
- [gestaltPowerMgrAttr](./api-1472525-power_manager_attribute_selector/gestaltpowermgrattr.md)
  The `Gestalt` selector you pass to determine which Power Manager capabilities are available.
- [gestaltPMgrExists](./api-1472525-power_manager_attribute_selector/gestaltpmgrexists.md)
  If true, the Power Manager is present.
- [gestaltPMgrCPUIdle](./api-1472525-power_manager_attribute_selector/gestaltpmgrcpuidle.md)
  If true the CPU is capable of going into a low–power-consumption state. 
- [gestaltPMgrSCC](./api-1472525-power_manager_attribute_selector/gestaltpmgrscc.md)
  If true, it is possible to stop the SCC clock, thus effectively turning off the serial ports. 
- [gestaltPMgrSound](./api-1472525-power_manager_attribute_selector/gestaltpmgrsound.md)
  If true, it is possible to turn off power to the sound circuits.
- [gestaltPMgrDispatchExists](./api-1472525-power_manager_attribute_selector/gestaltpmgrdispatchexists.md)
  If true, Dispatch is present.
- [gestaltPMgrSupportsAVPowerStateAtSleepWake](./api-1472525-power_manager_attribute_selector/gestaltpmgrsupportsavpowerstateatsleepwake.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472525-power_manager_attribute_selector)*