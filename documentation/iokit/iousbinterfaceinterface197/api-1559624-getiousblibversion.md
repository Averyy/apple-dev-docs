# GetIOUSBLibVersion

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the version of the IOUSBLib and the version of the IOUSBFamily.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*GetIOUSBLibVersion)(void *self, NumVersion *ioUSBLibVersion, NumVersion *usbFamilyVersion);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

#### Discussion

The interface does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `ioUSBLibVersion`: Pointer to a NumVersion structure that on return will contain the version of the IOUSBLib.
- `usbFamilyVersion`: Pointer to a NumVersion structure that on return will contain the version of the IOUSBFamily.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface197/1559624-getiousblibversion)*