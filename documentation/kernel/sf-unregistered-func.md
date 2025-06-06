# sf_unregistered_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef void (*sf_unregistered_func)(sflt_handle handle);
```

#### Discussion

sf_unregistered_func is called to notify the filter it has been unregistered. This is the last function the stack will call and this function will only be called once all other function calls in to your filter have completed. Once this function has been called, your kext may safely unload.

## Parameters

- `handle`: The socket filter handle used to identify this filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sf_unregistered_func)*