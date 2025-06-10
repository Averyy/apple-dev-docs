# IOUSBEndpointDescriptor

**Framework**: Kernel  
**Kind**: tdef

The structure for storing an endpoint descriptor.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef struct IOUSBEndpointDescriptor IOUSBEndpointDescriptor;
```

#### Discussion

A descriptor for a USB endpoint. See USB 3.2, 9.6.6.

## Topics

### Getting the Properties
- [bLength](iousbendpointdescriptor/1546156-blength.md)
  The size of the descriptor.
- [bDescriptorType](iousbendpointdescriptor/1545995-bdescriptortype.md)
  The type of the descriptor.
- [bEndpointAddress](iousbendpointdescriptor/1546243-bendpointaddress.md)
  The address of the endpoint.
- [bmAttributes](iousbendpointdescriptor/1546048-bmattributes.md)
  The attributes of the endpoint.
- [wMaxPacketSize](iousbendpointdescriptor/1546305-wmaxpacketsize.md)
  The maximum packet size that the endpoint supports.
- [bInterval](iousbendpointdescriptor/1546209-binterval.md)
  The interval to use when polling the endpoint for data transfers.

## See Also

- [IOUSBStandardEndpointDescriptors](iousbstandardendpointdescriptors.md)
  A container for descriptors for a single endpoint.
- [IOUSBEndpointDescriptorPtr](iousbendpointdescriptorptr.md)
  A pointer to the endpoint descriptor.
- [IOUSBEndpointProperties](iousbendpointproperties.md)
  A structure that holds USB endpoint properties.
- [IOUSBEndpointPropertiesPtr](iousbendpointpropertiesptr.md)
  A pointer to an endpoint properties object.
- [IOUSBGetEndpointDescriptorOptions](iousbgetendpointdescriptoroptions.md)
  Options for fetching the endpoint descriptors of a pipe.
- [IOUSBEndpointDescriptor](../iokit/usb_h_user-space/iousbendpointdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbendpointdescriptor)*