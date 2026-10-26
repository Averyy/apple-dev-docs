# IOUSBFamilyIOOptionBit

**Framework**: IOKit  
**Kind**: enum

## Declaration

```c
enum {
   kIOUSBInterfaceOpenAlt = 0x00010000,
   kIOUSBInterfaceOpenAlternateInterfaceBit = 16,
   kUSBOptionBitOpenExclusivelyBit = 17,
   kIOUSBInterfaceOpenAlternateInterfaceMask = (
   1 << kIOUSBInterfaceOpenAlternateInterfaceBit),
   kUSBOptionBitOpenExclusivelyMask = (
   1 << kUSBOptionBitOpenExclusivelyBit)
};
```

#### Overview

Options used exclusively by the USB Family when calling calling IOService APIs, such as open() and close().

## Topics

### Constants
- [kIOUSBInterfaceOpenAlt](../../kernel/api-1646355-anonymous/kiousbinterfaceopenalt.md)
- [kUSBOptionBitOpenExclusivelyBit](../../kernel/api-1646355-anonymous/kusboptionbitopenexclusivelybit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbfamilyiooptionbit)*