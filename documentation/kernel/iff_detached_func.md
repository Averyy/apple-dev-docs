# iff_detached_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef void (*iff_detached_func)(void *cookie, ifnet_t interface);
```

#### Discussion

iff_detached_func is called to notify the filter that it has been detached from an interface. This is the last call to the filter that will be made. A filter may be detached if the interface is detached or the detach filter function is called. In the case that the interface is being detached, your filter's event function will be called with the interface detaching event before the your detached function will be called.

## Parameters

- `cookie`: The cookie specified when this filter was attached.
- `interface`: The interface this filter was detached from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iff_detached_func)*