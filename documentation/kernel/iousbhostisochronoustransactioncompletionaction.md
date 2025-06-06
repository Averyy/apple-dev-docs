# IOUSBHostIsochronousTransactionCompletionAction

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 12.0+

## Declaration

```swift
typedef void (*IOUSBHostIsochronousTransactionCompletionAction)(void *owner, void *parameter, IOReturn status, IOUSBHostIsochronousTransaction *transactionList);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhostisochronoustransactioncompletionaction)*