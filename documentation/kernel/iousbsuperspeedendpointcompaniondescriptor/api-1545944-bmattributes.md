# bmAttributes

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

A bitmap encoding of supported device-level features.

**Availability**:
- macOS 10.7+

## Declaration

```c
uint8_t bmAttributes;
```

## See Also

### Getting the Properties
- [bLength](./api-1546150-blength.md)
  The size of the descriptor.
- [bDescriptorType](./api-1546448-bdescriptortype.md)
  The type of the descriptor.
- [bMaxBurst](./api-1545987-bmaxburst.md)
  The maximum number of packets the endpoint can send or receive as part of a burst.
- [wBytesPerInterval](./api-1546415-wbytesperinterval.md)
  The total number of bytes this endpoint transfers every service interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbsuperspeedendpointcompaniondescriptor/1545944-bmattributes)*