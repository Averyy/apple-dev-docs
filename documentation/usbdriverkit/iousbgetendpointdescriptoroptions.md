# IOUSBGetEndpointDescriptorOptions

**Framework**: USBDriverKit  
**Kind**: enum

Options for fetching the endpoint descriptors of a pipe.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
enum IOUSBGetEndpointDescriptorOptions : unsigned int;
```

## Topics

### Getting the Descriptor Options
- [kIOUSBGetEndpointDescriptorOriginal](iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptororiginal.md)
  The original descriptor used to create the pipe.
- [kIOUSBGetEndpointDescriptorCurrentPolicy](iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptorcurrentpolicy.md)
  The descriptor controlling the current endpoint policy.

## See Also

- [GetDescriptors](iousbhostpipe/getdescriptors.md)
  Retrieves the endpoint descriptors associated with this pipe.
- [IOUSBStandardEndpointDescriptors](iousbstandardendpointdescriptors.md)
  Encapsulates the descriptors for a single endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointdescriptoroptions)*