# bDescriptorType

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The type of the descriptor.

**Availability**:
- macOS 10.7+

## Declaration

```c
uint8_t bDescriptorType;
```

## See Also

### Getting the Properties
- [bLength](./api-1546150-blength.md)
  The size of the descriptor.
- [bMaxBurst](./api-1545987-bmaxburst.md)
  The maximum number of packets the endpoint can send or receive as part of a burst.
- [bmAttributes](./api-1545944-bmattributes.md)
  A bitmap encoding of supported device-level features.
- [wBytesPerInterval](./api-1546415-wbytesperinterval.md)
  The total number of bytes this endpoint transfers every service interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbsuperspeedendpointcompaniondescriptor/1546448-bdescriptortype)*