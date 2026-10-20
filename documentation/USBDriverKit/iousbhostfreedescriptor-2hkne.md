# IOUSBHostFreeDescriptor

**Framework**: USBDriverKit  
**Kind**: func  
**Role**: Function

Releases the specified device descriptor.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
void IOUSBHostFreeDescriptor(const IOUSBDeviceDescriptor *descriptor);
```

## Parameters

- `descriptor`: The descriptor to release.

## See Also

### Disposing of Descriptors
- [IOUSBHostFreeDescriptor](./iousbhostfreedescriptor-2r7k.md)
  Releases the specified configuration descriptor.
- [IOUSBHostFreeDescriptor](./iousbhostfreedescriptor-5j4pp.md)
  Releases the specified BOS descriptor.
- [IOUSBHostFreeDescriptor](./iousbhostfreedescriptor-3fve6.md)
  Releases the specified string descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostfreedescriptor-2hkne)*