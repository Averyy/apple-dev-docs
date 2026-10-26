# kUSBPowerRequestSleepReallocate

**Framework**: IOKit  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
kUSBPowerRequestSleepReallocate = 5
```

#### Discussion

When used with ReturnExtraPower(), it will send a message to all devices indicating that they can ask for more sleep power, as some device has released it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usbpowerrequesttypes/kusbpowerrequestsleepreallocate)*