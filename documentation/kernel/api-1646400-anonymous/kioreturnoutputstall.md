# kIOReturnOutputStall

**Framework**: Kernel  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.12+

## Declaration

```c
kIOReturnOutputStall = (kIOOutputStatusRetry    | kIOOutputCommandStall)
```

## Discussion

Stall the queue and retry the same packet when the queue is restarted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1646400-anonymous/kioreturnoutputstall)*