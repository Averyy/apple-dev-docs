# IOUSBHostIOSourceClientRecordLink

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

A structure that represents a USB host input/output source client record entry.

**Availability**:
- macOS 10.13+

## Declaration

```c
typedef struct IOUSBHostIOSourceClientRecordLink {
    ...
} IOUSBHostIOSourceClientRecordLink;
```

## Topics

### Getting the Properties
- [le_next](./iousbhostiosourceclientrecordlink/api-2882013-le_next.md)
  The pointer to the next USB host input/output source client record. 
- [le_prev](./iousbhostiosourceclientrecordlink/api-2882012-le_prev.md)
  The pointer to the previous USB host input/output source client record.

## See Also

### Device Communication
- [Building a Simple USB Driver](./hardware_families/usb/building_a_simple_usb_driver.md)
  Set up and load a driver that logs output to the Console app.
- [IOUSBHostIOSourceClientRecordList](./iousbhostiosourceclientrecordlist.md)
  A structure that represents a list of USB host input/output source client records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostiosourceclientrecordlink)*