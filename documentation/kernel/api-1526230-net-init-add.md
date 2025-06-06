# net_init_add

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
errno_t net_init_add(net_init_func_ptr init_func);
```

#### Return_value

EINVAL - the init_func value was NULL. EALREADY - the network has already been initialized ENOMEM - there was not enough memory to perform this operation 0 - success

#### Discussion

Add a function to be called during network initialization. Your kext must not unload until the function you register is called if net_init_add returns success.

## Parameters

- `init_func`: A pointer to a function to be called when the stack is initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1526230-net_init_add)*