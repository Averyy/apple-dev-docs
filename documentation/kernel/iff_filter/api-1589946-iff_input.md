# iff_input

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

The filter function to handle inbound packets, may be NULL.

**Availability**:
- macOS 10.6+

## Declaration

```c
iff_input_func iff_input;
```

## See Also

### Fields
- [iff_cookie](./api-1589954-iff_cookie.md)
  A kext defined cookie that will be passed to all filter functions.
- [iff_name](./api-1589945-iff_name.md)
  A filter name used for debugging purposes.
- [iff_protocol](./api-1589949-iff_protocol.md)
  The protocol of the packets this filter is interested in. If you specify zero, packets from all protocols will be passed to the filter.
- [iff_output](./api-1589942-iff_output.md)
  The filter function to handle outbound packets, may be NULL.
- [iff_event](./api-1589952-iff_event.md)
  The filter function to handle interface events, may be null.
- [iff_ioctl](./api-1589948-iff_ioctl.md)
  The filter function to handle interface ioctls, may be null.
- [iff_detached](./api-1589944-iff_detached.md)
  The filter function used to notify the filter that it has been detached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iff_filter/1589946-iff_input)*