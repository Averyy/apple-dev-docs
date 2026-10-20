# AdjustPipe

**Framework**: USBDriverKit  
**Kind**: method  
**Role**: Instance Method

Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.

**Availability**:
- DriverKit 19.0+

## Declaration

```cpp
virtual kern_return_t AdjustPipe(const IOUSBStandardEndpointDescriptors *descriptors);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

Periodic (interrupt and isochronous) endpoints reserve bus bandwidth when they’re created. This reserved bandwidth takes into account the maximum packet size, burst size, and endpoint service interval. If you know the endpoint won’t use all of its allocated bandwidth, you can call the `AdjustPipe` method to reduce the bandwidth reserved for the endpoint.

## Parameters

- `descriptors`: A pointer to a descriptor’s structure describing the new endpoint policy. Copy the original endpoint descriptors and modify to adjust maximum packet size, burst, and interval values.

## See Also

### Adjusting the Pipe’s Status
- [ClearStall](./clearstall.md)
  Clears the halt condition of the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe/adjustpipe)*