# sflt_register

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

## Declaration

```c
errno_t sflt_register(const struct sflt_filter *filter, int domain, int type, int protocol);
```

#### Return Value

0 on success otherwise the errno error.

#### Discussion

Registers a socket filter. See 'man 2 socket' for a desciption of domain, type, and protocol.

## Parameters

- `filter`: A structure describing the filter.
- `domain`: The protocol domain these filters will be attached to.
- `type`: The socket type these filters will be attached to.
- `protocol`: The protocol these filters will be attached to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1433228-sflt_register)*