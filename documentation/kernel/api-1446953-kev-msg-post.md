# kev_msg_post

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.9+

## Declaration

```swift
errno_t kev_msg_post(struct kev_msg *event_msg);
```

#### Return_value

Will return zero upon success. May return a number of errors depending on the type of failure. EINVAL indicates that there was something wrong with the kerne event. The vendor code of the kernel event must be assigned using kev_vendor_code_find. If the message is too large, EMSGSIZE will be returned.

#### Discussion

Post a kernel event message.

## Parameters

- `event_msg`: A structure defining the kernel event message to post.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1446953-kev_msg_post)*