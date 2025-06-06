# GetDescriptors

**Framework**: USBDriverKit  
**Kind**: method

Retrieves the endpoint descriptors associated with this pipe.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kern_return_t GetDescriptors(IOUSBStandardEndpointDescriptors * descriptors, IOUSBGetEndpointDescriptorOptions type);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `descriptors`: A pointer to a variable. On output, this variable contains the endpoint descriptors for the pipe.
- `type`: The options indicating which descriptors to retrieve. For a list of possible values, see  .

## See Also

- [IOUSBStandardEndpointDescriptors](iousbstandardendpointdescriptors.md)
  Encapsulates the descriptors for a single endpoint.
- [IOUSBGetEndpointDescriptorOptions](iousbgetendpointdescriptoroptions.md)
  Options for fetching the endpoint descriptors of a pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/getdescriptors)*