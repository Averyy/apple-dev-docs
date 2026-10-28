# kIOUSBGetEndpointDescriptorCurrentPolicy

**Framework**: USBDriverKit  
**Kind**: case  
**Role**: Enumeration Case

The descriptor controlling the current endpoint policy.

**Availability**:
- DriverKit 19.0+

## Declaration

```c
kIOUSBGetEndpointDescriptorCurrentPolicy
```

## Discussion

Specify this option when you want the include descriptor changes you made using the [`AdjustPipe`](../iousbhostpipe/adjustpipe.md) method.

## See Also

### Getting the Descriptor Options
- [kIOUSBGetEndpointDescriptorOriginal](./kiousbgetendpointdescriptororiginal.md)
  The original descriptor used to create the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptorcurrentpolicy)*