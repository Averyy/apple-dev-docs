# IOUSBDevRequestDesc

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.8+

## Declaration

```c
typedef struct IOUSBDevRequestDesc {
    ...
} IOUSBDevRequestDesc;
```

#### Overview

Parameter block for control requests, using a memory descriptor for the data to be transferred. Only available in the kernel.

## Topics

### Instance Properties
- [bRequest](./iousbdevrequestdesc/api-1546108-brequest.md)
- [bmRequestType](./iousbdevrequestdesc/api-1545895-bmrequesttype.md)
- [pData](./iousbdevrequestdesc/api-1546016-pdata.md)
- [wIndex](./iousbdevrequestdesc/api-1546062-windex.md)
- [wLenDone](./iousbdevrequestdesc/api-1546205-wlendone.md)
- [wLength](./iousbdevrequestdesc/api-1545931-wlength.md)
- [wValue](./iousbdevrequestdesc/api-1546381-wvalue.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevrequestdesc)*