# Addressing Mode Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the addressing mode of the operating system.

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
- [gestaltAddressingModeAttr](./api-1473033-addressing_mode_attribute_select/gestaltaddressingmodeattr.md)
  The `Gestalt` selector you pass to determine the addressing mode attributes that are present.
- [gestalt32BitAddressing](./api-1473033-addressing_mode_attribute_select/gestalt32bitaddressing.md)
  If `true`, the operating system is using 32-bit addressing mode.
- [gestalt32BitSysZone](./api-1473033-addressing_mode_attribute_select/gestalt32bitsyszone.md)
  If `true`, there is a 32-bit compatible system zone.
- [gestalt32BitCapable](./api-1473033-addressing_mode_attribute_select/gestalt32bitcapable.md)
  If `true`, Machine is 32-bit capable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1473033-addressing_mode_attribute_select)*