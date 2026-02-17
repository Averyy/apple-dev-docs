# kIOUSBGetEndpointDescriptorCurrentPolicy

**Framework**: USBDriverKit  
**Kind**: case

The descriptor controlling the current endpoint policy.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
kIOUSBGetEndpointDescriptorCurrentPolicy
```

#### Discussion

Specify this option when you want the include descriptor changes you made using the [`AdjustPipe`](iousbhostpipe/adjustpipe.md) method.

## See Also

- [kIOUSBGetEndpointDescriptorOriginal](iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptororiginal.md)
  The original descriptor used to create the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptorcurrentpolicy)*