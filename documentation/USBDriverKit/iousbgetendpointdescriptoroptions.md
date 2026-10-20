# IOUSBGetEndpointDescriptorOptions

**Framework**: USBDriverKit  
**Kind**: enum  
**Role**: Enumeration

Options for fetching the endpoint descriptors of a pipe.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
enum IOUSBGetEndpointDescriptorOptions : unsigned int;
```

## Topics

### Getting the Descriptor Options
- [kIOUSBGetEndpointDescriptorOriginal](./iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptororiginal.md)
  The original descriptor used to create the pipe.
- [kIOUSBGetEndpointDescriptorCurrentPolicy](./iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptorcurrentpolicy.md)
  The descriptor controlling the current endpoint policy.

## See Also

### Getting the Endpoint Descriptors
- [GetDescriptors](./iousbhostpipe/getdescriptors.md)
  Retrieves the endpoint descriptors associated with this pipe.
- [IOUSBStandardEndpointDescriptors](./iousbstandardendpointdescriptors.md)
  Encapsulates the descriptors for a single endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointdescriptoroptions)*