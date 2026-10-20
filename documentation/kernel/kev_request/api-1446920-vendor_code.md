# vendor_code

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

All kernel events that don't match this vendor code will be ignored. KEV_ANY_VENDOR can be used to receive kernel events with any vendor code.

**Availability**:
- macOS 10.9+

## Declaration

```c
u_int32_t vendor_code;
```

## See Also

### Fields
- [total_size](./api-1809281-total_size.md)
  Total size of the kernel event message including the header.
- [kev_class](./api-1446933-kev_class.md)
  All kernel events that don't match this class will be ignored. KEV_ANY_CLASS can be used to receive kernel events with any class.
- [kev_subclass](./api-1446979-kev_subclass.md)
  All kernel events that don't match this subclass will be ignored. KEV_ANY_SUBCLASS can be used to receive kernel events with any subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kev_request/1446920-vendor_code)*