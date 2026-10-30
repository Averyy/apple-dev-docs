# Interrupt Types

**Framework**: Kernel  
**Kind**: enum  
**Role**: Enumeration

Interrupt types that the device supports.

**Availability**:
- DriverKit 20.0+
- macOS 10.12+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Types
- [kIOInterruptTypePCIMessaged](../PCIDriverKit/kiointerrupttypepcimessaged.md)
  A message signaled interrupt (MSI) type for a PCI device.
- [kIOInterruptTypePCIMessagedX](../PCIDriverKit/kiointerrupttypepcimessagedx.md)
  An extended message signal interrupt (MSI-X) type for a PCI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1640325-interrupt_types)*