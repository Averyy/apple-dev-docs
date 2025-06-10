# IOUSBGetEndpointDescriptorOptions

**Framework**: Kernel  
**Kind**: tag

Options for fetching the endpoint descriptors of a pipe.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum IOUSBGetEndpointDescriptorOptions : unsigned int {
    ...
};
```

## Topics

### Getting the Options
- [kIOUSBGetEndpointDescriptorOriginal](iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptororiginal.md)
  The original descriptor that the system uses to create the pipe.
- [kIOUSBGetEndpointDescriptorCurrentPolicy](iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptorcurrentpolicy.md)
  The descriptor controlling the current endpoint policy.

## See Also

- [IOUSBEndpointDescriptor](iousbendpointdescriptor.md)
  The structure for storing an endpoint descriptor.
- [IOUSBStandardEndpointDescriptors](iousbstandardendpointdescriptors.md)
  A container for descriptors for a single endpoint.
- [IOUSBEndpointDescriptorPtr](iousbendpointdescriptorptr.md)
  A pointer to the endpoint descriptor.
- [IOUSBEndpointProperties](iousbendpointproperties.md)
  A structure that holds USB endpoint properties.
- [IOUSBEndpointPropertiesPtr](iousbendpointpropertiesptr.md)
  A pointer to an endpoint properties object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbgetendpointdescriptoroptions)*