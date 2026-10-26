# Hardware Attribute Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for hardware.

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
- [gestaltHardwareAttr](./api-1472318-hardware_attribute_attribute_sel/gestalthardwareattr.md)
- [gestaltHasVIA1](./api-1472318-hardware_attribute_attribute_sel/gestalthasvia1.md)
- [gestaltHasVIA2](./api-1472318-hardware_attribute_attribute_sel/gestalthasvia2.md)
- [gestaltHasASC](./api-1472318-hardware_attribute_attribute_sel/gestalthasasc.md)
- [gestaltHasSCC](./api-1472318-hardware_attribute_attribute_sel/gestalthasscc.md)
- [gestaltHasSCSI](./api-1472318-hardware_attribute_attribute_sel/gestalthasscsi.md)
  The `gestaltHasSCSI` bit means the machine is equipped with a SCSI implementation based on the 53C80 chip, which was introduced in the Macintosh Plus. This bit is 0 on computers with a different SCSI implementation.
- [gestaltHasSoftPowerOff](./api-1472318-hardware_attribute_attribute_sel/gestalthassoftpoweroff.md)
- [gestaltHasSCSI961](./api-1472318-hardware_attribute_attribute_sel/gestalthasscsi961.md)
  This bit is set if the machine has a SCSI implementation based on the 53C96 chip installed on an internal  bus.
- [gestaltHasSCSI962](./api-1472318-hardware_attribute_attribute_sel/gestalthasscsi962.md)
  This bit is set if the machine has a SCSI implementation based on the 53C96 chip installed on an  external bus.
- [gestaltHasUniversalROM](./api-1472318-hardware_attribute_attribute_sel/gestalthasuniversalrom.md)
- [gestaltHasEnhancedLtalk](./api-1472318-hardware_attribute_attribute_sel/gestalthasenhancedltalk.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472318-hardware_attribute_attribute_sel)*