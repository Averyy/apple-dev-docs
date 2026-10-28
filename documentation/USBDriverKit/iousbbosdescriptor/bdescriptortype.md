# bDescriptorType

**Framework**: USBDriverKit  
**Kind**: property  
**Role**: Instance Property

The type of the descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
uint8_t bDescriptorType;
```

## Discussion

The value in this field is always [`kIOUSBDescriptorTypeBOS`](../tiousbdescriptortype/kiousbdescriptortypebos.md).

## See Also

### Accessing the Descriptor Properties
- [bLength](./blength.md)
  The size of the descriptor in bytes.
- [wTotalLength](./wtotallength.md)
  The length, in bytes, of the descriptor and all of its subdescriptors.
- [bNumDeviceCaps](./bnumdevicecaps.md)
  The number of separate device capability descriptors in the binary object store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbbosdescriptor/bdescriptortype)*