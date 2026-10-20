# IOUSBHostIsochronousTransactionCompletionAction

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 12.0+

## Declaration

```c
typedef void (*IOUSBHostIsochronousTransactionCompletionAction)(void *owner, void *parameter, IOReturn status, IOUSBHostIsochronousTransaction *transactionList);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostisochronoustransactioncompletionaction)*