# registerPMSettingController

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
IOReturn registerPMSettingController(const OSSymbol *settings[], uint32_t supportedPowerSources, IOPMSettingControllerCallback callout, OSObject *target, uintptr_t refcon, OSObject **handle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopmrootdomain/3516722-registerpmsettingcontroller)*