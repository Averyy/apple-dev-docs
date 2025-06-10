# kev_subclass

**Framework**: Kernel  
**Kind**: structp

All kernel events that don't match this subclass will be ignored. KEV_ANY_SUBCLASS can be used to receive kernel events with any subclass.

**Availability**:
- macOS 10.9+

## Declaration

```swift
u_int32_t kev_subclass;
```

## See Also

- [total_size](kev_request/1809281-total_size.md)
  Total size of the kernel event message including the header.
- [vendor_code](kev_request/1446920-vendor_code.md)
  All kernel events that don't match this vendor code will be ignored. KEV_ANY_VENDOR can be used to receive kernel events with any vendor code.
- [kev_class](kev_request/1446933-kev_class.md)
  All kernel events that don't match this class will be ignored. KEV_ANY_CLASS can be used to receive kernel events with any class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kev_request/1446979-kev_subclass)*