# CopyStringDescriptor

**Framework**: USBDriverKit  
**Kind**: method

Returns a string descriptor from the device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
const IOUSBStringDescriptor * CopyStringDescriptor(uint8_t index);
```

#### Return Value

A pointer to the descriptor, or `NULL` if the descriptor isn’t found. It’s your responsibility to free the returned descriptor.

#### Discussion

This method uses a `GET_DESCRIPTOR` control request (USB 2.0, section 9.4.3) to fetch the string descriptor from the device. The method puts the `index` value in the low byte of the `wValue` field of the request structure, and it uses US English as the language.

## Parameters

- `index`: The descriptor’s index value.

## See Also

- [CopyConfigurationDescriptor](iousbhostinterface/copyconfigurationdescriptor.md)
  Retrieves the parent configuration descriptor for this interface.
- [GetInterfaceDescriptor](iousbhostinterface/getinterfacedescriptor.md)
  Returns the version of the interface descriptor that is associated with the specified configuration.
- [CopyStringDescriptor](iousbhostinterface/copystringdescriptor-83du1.md)
  Returns a descriptor from the device in the specified language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface/copystringdescriptor-8k65j)*