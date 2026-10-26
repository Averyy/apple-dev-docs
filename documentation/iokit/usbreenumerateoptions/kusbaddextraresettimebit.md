# kUSBAddExtraResetTimeBit

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.3+

## Declaration

```c
kUSBAddExtraResetTimeBit = 31
```

#### Discussion

Setting this bit will cause the Hub driver to wait 100ms before addressing the device after the reset following the re-enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usbreenumerateoptions/kusbaddextraresettimebit)*