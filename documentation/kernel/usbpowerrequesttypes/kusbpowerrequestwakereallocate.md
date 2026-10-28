# kUSBPowerRequestWakeReallocate

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

The system requests power reallocation upon waking.

**Availability**:
- macOS 10.7+

## Declaration

```c
kUSBPowerRequestWakeReallocate = 4
```

## Discussion

When you use this enumeration with [`ReturnExtraPower`](../../iokit/iousbdeviceinterface942/api-2977171-returnextrapower.md), it sends a message to all devices to return more wake power because some devices have released it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes/kusbpowerrequestwakereallocate)*