# kIOUSBGetEndpointDescriptorCurrentPolicy

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

The descriptor controlling the current endpoint policy.

**Availability**:
- macOS 10.15+

## Declaration

```c
kIOUSBGetEndpointDescriptorCurrentPolicy
```

#### Discussion

Specify this option when you want to include descriptor changes you made using the [`AdjustPipe`](../iousbhostpipe/api-3294684-adjustpipe.md) method.

## See Also

### Getting the Options
- [kIOUSBGetEndpointDescriptorOriginal](./kiousbgetendpointdescriptororiginal.md)
  The original descriptor that the system uses to create the pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbgetendpointdescriptoroptions/kiousbgetendpointdescriptorcurrentpolicy)*