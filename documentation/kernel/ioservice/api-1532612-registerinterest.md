# registerInterest

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual OSPtr<IONotifier> registerInterest(const OSSymbol *typeOfInterest, IOServiceInterestHandler handler, void *target, void *ref);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioservice/1532612-registerinterest)*