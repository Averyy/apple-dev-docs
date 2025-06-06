# kern_event_msg

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct kern_event_msg {
    ...
};
```

#### Discussion

This structure is prepended to all kernel events. This structure is used to determine the format of the remainder of the kernel event. This structure will appear on all messages received on a kernel event socket. To post a kernel event, a slightly different structure is used.

## Topics

### Fields
- [total_size](kern_event_msg/1446925-total_size.md)
  Total size of the kernel event message including the header.
- [vendor_code](kern_event_msg/1446929-vendor_code.md)
  The vendor code indicates which vendor generated the kernel event. This gives every vendor a unique set of classes and subclasses to use. Use the SIOCGKEVVENDOR ioctl to look up vendor codes for vendors other than Apple. Apple uses KEV_VENDOR_APPLE.
- [kev_class](kern_event_msg/1446955-kev_class.md)
  The class of the kernel event.
- [kev_subclass](kern_event_msg/1446935-kev_subclass.md)
  The subclass of the kernel event.
- [id](kern_event_msg/1446959-id.md)
  Monotonically increasing value.
- [event_code](kern_event_msg/1446927-event_code.md)
  The event code.
- [event_data](kern_event_msg/1446985-event_data.md)
  Any additional data about this event. Format will depend on the vendor_code, kev_class, kev_subclass, and event_code. The length of the event_data can be determined using total_size - KEV_MSG_HEADER_SIZE.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kern_event_msg)*