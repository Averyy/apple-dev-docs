# kIOOutputStatusRetry

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.12+

## Declaration

```c
kIOOutputStatusRetry = 0x0002
```

## Discussion

Target ran out of resources, and is unable to accept the packet. The ownership of the packet reverts back to the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1646401-anonymous/kiooutputstatusretry)*