# kIOUSBGetEndpointDescriptorCurrentPolicy

**Framework**: Kernel  
**Kind**: econst

The descriptor controlling the current endpoint policy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
kIOUSBGetEndpointDescriptorCurrentPolicy
```

#### Discussion

Specify this option when you want to include descriptor changes you made using the [`AdjustPipe`](iousbhostpipe/3294684-adjustpipe.md) method.

## See Also

- [kIOUSBGetEndpointDescriptorOriginal](iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptororiginal.md)
  The original descriptor that the system uses to create the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptorcurrentpolicy)*