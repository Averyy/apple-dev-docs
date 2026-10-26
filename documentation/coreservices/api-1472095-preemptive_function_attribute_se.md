# Preemptive Function Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for preemptive system software functions.

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
- [gestaltMPCallableAPIsAttr](./api-1472095-preemptive_function_attribute_se/gestaltmpcallableapisattr.md)
  The Gestalt selector passed to determine the availability of preemptive system software functions. The `Gestalt` function produces a 32-bit value that you should test to determine which what type of preemptive calls are allowed. 
- [gestaltMPFileManager](./api-1472095-preemptive_function_attribute_se/gestaltmpfilemanager.md)
  If this bit is set, you can call preemptively safe File Manager functions.
- [gestaltMPDeviceManager](./api-1472095-preemptive_function_attribute_se/gestaltmpdevicemanager.md)
  If this bit is set, you can call preemptively safe Device Manager function.
- [gestaltMPTrapCalls](./api-1472095-preemptive_function_attribute_se/gestaltmptrapcalls.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472095-preemptive_function_attribute_se)*