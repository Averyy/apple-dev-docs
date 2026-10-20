# kev_msg

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct kev_msg {
    ...
};
```

#### Discussion

This structure is used when posting a kernel event.

## Topics

### Fields
- [vendor_code](kev_msg/1446947-vendor_code.md)
  The vendor code assigned by kev_vendor_code_find.
- [kev_class](kev_msg/1446923-kev_class.md)
  The event's class.
- [dv](kev_msg/1446996-dv.md)
  An array of vectors describing additional data to be appended to the kernel event.
### Instance Properties
- [event_code](kev_msg/1446986-event_code.md)
  The event's code.
- [kev_subclass](kev_msg/1446957-kev_subclass.md)
  The event's subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kev_msg)*