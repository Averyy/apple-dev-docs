# minphys

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

Adjust a buffer's count to be no more than maximum physical I/O transfer size for the host architecture.

**Availability**:
- macOS 10.4+

## Declaration

```c
u_int minphys(buf_t bp);
```

## Return Value

New byte count.

## Discussion

physio() takes as a parameter a function to bound transfer sizes for each VNOP_STRATEGY() call. minphys() is a default implementation. It calls buf_setcount() to make the buffer's count the min() of its current count and the max I/O size for the host architecture.

## Parameters

- `bp`: The buffer whose byte count to modify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1561824-minphys)*