# System Architecture Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify the native system architecture.

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
- [gestaltSysArchitecture](./api-1472163-system_architecture_selectors/gestaltsysarchitecture.md)
  The selector you pass to the `Gestalt` function to determine the native system architecture.
- [gestalt68k](./api-1472163-system_architecture_selectors/gestalt68k.md)
  If the `Gestalt` function returns `gestalt68k`, the system is a MC680x0 Macintosh.
- [gestaltPowerPC](./api-1472163-system_architecture_selectors/gestaltpowerpc.md)
  If the `Gestalt` function returns `gestaltPowerPC`, the system is a PowerPC Macintosh.
- [gestaltIntel](./api-1472163-system_architecture_selectors/gestaltintel.md)
  If the `Gestalt` function returns `gestaltIntel`, the system is is an Intel-based Macintosh.
- [gestaltArm](./api-1472163-system_architecture_selectors/gestaltarm.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472163-system_architecture_selectors)*