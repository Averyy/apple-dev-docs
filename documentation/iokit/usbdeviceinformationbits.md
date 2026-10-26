# USBDeviceInformationBits

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
typedef enum USBDeviceInformationBits : unsigned int {
    ...
} USBDeviceInformationBits;
```

#### Overview

GetUSBDeviceInformation will return a unit32_t value with bits set indicating that a particular state is present in the USB device. These bits are described here

## Topics

### Constants
- [kUSBInformationDeviceIsCaptiveBit](./usbdeviceinformationbits/kusbinformationdeviceiscaptivebit.md)
- [kUSBInformationDeviceIsAttachedToRootHubBit](./usbdeviceinformationbits/kusbinformationdeviceisattachedtoroothubbit.md)
- [kUSBInformationDeviceIsInternalBit](./usbdeviceinformationbits/kusbinformationdeviceisinternalbit.md)
- [kUSBInformationDeviceIsConnectedBit](./usbdeviceinformationbits/kusbinformationdeviceisconnectedbit.md)
- [kUSBInformationDeviceIsEnabledBit](./usbdeviceinformationbits/kusbinformationdeviceisenabledbit.md)
- [kUSBInformationDeviceIsSuspendedBit](./usbdeviceinformationbits/kusbinformationdeviceissuspendedbit.md)
- [kUSBInformationDeviceIsInResetBit](./usbdeviceinformationbits/kusbinformationdeviceisinresetbit.md)
- [kUSBInformationDeviceOvercurrentBit](./usbdeviceinformationbits/kusbinformationdeviceovercurrentbit.md)
- [kUSBInformationDevicePortIsInTestModeBit](./usbdeviceinformationbits/kusbinformationdeviceportisintestmodebit.md)
- [kUSBInformationDeviceIsRootHub](./usbdeviceinformationbits/kusbinformationdeviceisroothub.md)
- [kUSBInformationRootHubisBuiltIn](./usbdeviceinformationbits/kusbinformationroothubisbuiltin.md)
- [kUSBInformationDeviceIsRemote](./usbdeviceinformationbits/kusbinformationdeviceisremote.md)
- [kUSBInformationDeviceIsAttachedToEnclosure](./usbdeviceinformationbits/kusbinformationdeviceisattachedtoenclosure.md)
- [kUSBInformationDeviceIsOnThunderbolt](./usbdeviceinformationbits/kusbinformationdeviceisonthunderbolt.md)
  The USB device is downstream of a controller that attaches through a Thunderbolt port.
- [kUSBInformationDeviceIsAttachedToEnclosureMask](./usbdeviceinformationbits/kusbinformationdeviceisattachedtoenclosuremask.md)
- [kUSBInformationDeviceIsAttachedToRootHubMask](./usbdeviceinformationbits/kusbinformationdeviceisattachedtoroothubmask.md)
- [kUSBInformationDeviceIsCaptiveMask](./usbdeviceinformationbits/kusbinformationdeviceiscaptivemask.md)
- [kUSBInformationDeviceIsConnectedMask](./usbdeviceinformationbits/kusbinformationdeviceisconnectedmask.md)
- [kUSBInformationDeviceIsEnabledMask](./usbdeviceinformationbits/kusbinformationdeviceisenabledmask.md)
- [kUSBInformationDeviceIsInResetMask](./usbdeviceinformationbits/kusbinformationdeviceisinresetmask.md)
- [kUSBInformationDeviceIsInternalMask](./usbdeviceinformationbits/kusbinformationdeviceisinternalmask.md)
- [kUSBInformationDeviceIsOnThunderboltBit](./usbdeviceinformationbits/kusbinformationdeviceisonthunderboltbit.md)
- [kUSBInformationDeviceIsOnThunderboltMask](./usbdeviceinformationbits/kusbinformationdeviceisonthunderboltmask.md)
- [kUSBInformationDeviceIsRemoteMask](./usbdeviceinformationbits/kusbinformationdeviceisremotemask.md)
- [kUSBInformationDeviceIsRootHubMask](./usbdeviceinformationbits/kusbinformationdeviceisroothubmask.md)
- [kUSBInformationDeviceIsSuspendedMask](./usbdeviceinformationbits/kusbinformationdeviceissuspendedmask.md)
- [kUSBInformationDeviceOvercurrentMask](./usbdeviceinformationbits/kusbinformationdeviceovercurrentmask.md)
- [kUSBInformationDevicePortIsInTestModeMask](./usbdeviceinformationbits/kusbinformationdeviceportisintestmodemask.md)
- [kUSBInformationRootHubIsBuiltInBit](./usbdeviceinformationbits/kusbinformationroothubisbuiltinbit.md)
- [kUSBInformationRootHubIsBuiltInMask](./usbdeviceinformationbits/kusbinformationroothubisbuiltinmask.md)
- [kUSBInformationRootHubisBuiltInMask](./usbdeviceinformationbits/kusbinformationroothubisbuiltinmask-go5.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usbdeviceinformationbits)*