# Set Default Component Flags

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [defaultComponentIdentical](./api-1516455-set_default_component_flags/defaultcomponentidentical.md)
  The Component Manager places the component specified in the call to `SetDefaultComponent` in front of all other components that have the same component description.
- [defaultComponentAnyFlags](./api-1516455-set_default_component_flags/defaultcomponentanyflags.md)
  The Component Manager ignores the value of the `componentFlags` field during the reorder operation.
- [defaultComponentAnyManufacturer](./api-1516455-set_default_component_flags/defaultcomponentanymanufacturer.md)
  The Component Manager ignores the value of the `componentManufacturer` field during the reorder operation.
- [defaultComponentAnySubType](./api-1516455-set_default_component_flags/defaultcomponentanysubtype.md)
  The Component Manager ignores the value of the `componentSubType` field during the reorder operation.
- [defaultComponentAnyFlagsAnyManufacturer](./api-1516455-set_default_component_flags/defaultcomponentanyflagsanymanufacturer.md)
- [defaultComponentAnyFlagsAnyManufacturerAnySubType](./api-1516455-set_default_component_flags/defaultcomponentanyflagsanymanufactureranysubtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1516455-set_default_component_flags)*