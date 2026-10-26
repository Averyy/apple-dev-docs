# IOBlitProcPtr

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
typedef IOReturn (*IOBlitProcPtr)(void *thisPointer, IOOptionBits options, IOBlitType type, IOBlitSourceDestType sourceDestType, IOBlitOperation *operation, void *source, void *destination, IOBlitCompletionToken *completionToken);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioblitprocptr)*