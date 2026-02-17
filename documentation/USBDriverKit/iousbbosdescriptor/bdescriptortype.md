# bDescriptorType

**Framework**: USBDriverKit  
**Kind**: property

The type of the descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
uint8_t bDescriptorType;
```

#### Discussion

The value in this field is always [`kIOUSBDescriptorTypeBOS`](tiousbdescriptortype/kiousbdescriptortypebos.md).

## See Also

- [bLength](iousbbosdescriptor/blength.md)
  The size of the descriptor in bytes.
- [wTotalLength](iousbbosdescriptor/wtotallength.md)
  The length, in bytes, of the descriptor and all of its subdescriptors.
- [bNumDeviceCaps](iousbbosdescriptor/bnumdevicecaps.md)
  The number of separate device capability descriptors in the binary object store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbbosdescriptor/bdescriptortype)*