# kev_vendor_code

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct kev_vendor_code {
    ...
};
```

#### Discussion

This structure is used with the SIOCGKEVVENDOR ioctl to convert from a string identifying a kext or vendor, in the form of a bundle identifier, to a vendor code.

## Topics

### Fields
- [vendor_code](kev_vendor_code/1446971-vendor_code.md)
  After making the SIOCGKEVVENDOR ioctl call, this will be filled in with the vendor code if there is one.
- [vendor_string](kev_vendor_code/1446951-vendor_string.md)
  A bundle style identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kev_vendor_code)*