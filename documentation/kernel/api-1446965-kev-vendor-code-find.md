# kev_vendor_code_find

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.9+

## Declaration

```swift
errno_t kev_vendor_code_find(const char *vendor_string, u_int32_t *vendor_code);
```

#### Return_value

May return ENOMEM if memory constraints prevent allocation of a new vendor code.

#### Discussion

Lookup a vendor_code given a unique string. If the vendor code has not been used since launch, a unique integer will be assigned for that string. Vendor codes will remain the same until the machine is rebooted.

## Parameters

- `vendor_string`: A bundle style vendor identifier(i.e. com.apple).
- `vendor_code`: Upon return, a unique vendor code for use when posting kernel events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1446965-kev_vendor_code_find)*