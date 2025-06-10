# update

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual IOReturn update(
 UInt32 offset,
 const UInt32 *&romBase);
```

#### Return_value

kIOReturnSuccess if the specified offset is now accessable at romBase[offset].

#### Overview

makes sure that the ROM has at least the specified capacity, and that the ROM is uptodate from its start to at least the specified quadlet offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iolocalconfigdirectory/1812690-update)*