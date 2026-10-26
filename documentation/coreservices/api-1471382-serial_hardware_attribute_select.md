# Serial Hardware Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify serial hardware attributes.

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
- [gestaltSerialAttr](./api-1471382-serial_hardware_attribute_select/gestaltserialattr.md)
  The selector you pass to the `Gestalt` function to determine the serial hardware attributes of the machine, such as whether or not the GPIa line is connected and can be used for external clocking.
- [gestaltHasGPIaToDCDa](./api-1471382-serial_hardware_attribute_select/gestalthasgpiatodcda.md)
- [gestaltHasGPIaToRTxCa](./api-1471382-serial_hardware_attribute_select/gestalthasgpiatortxca.md)
- [gestaltHasGPIbToDCDb](./api-1471382-serial_hardware_attribute_select/gestalthasgpibtodcdb.md)
- [gestaltHidePortA](./api-1471382-serial_hardware_attribute_select/gestalthideporta.md)
- [gestaltHidePortB](./api-1471382-serial_hardware_attribute_select/gestalthideportb.md)
- [gestaltPortADisabled](./api-1471382-serial_hardware_attribute_select/gestaltportadisabled.md)
- [gestaltPortBDisabled](./api-1471382-serial_hardware_attribute_select/gestaltportbdisabled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471382-serial_hardware_attribute_select)*