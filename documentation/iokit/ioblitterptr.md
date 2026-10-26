# IOBlitterPtr

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.0+

## Declaration

```c
typedef IOReturn (*IOBlitterPtr)(void *thisPointer, IOOptionBits options, IOBlitType type, IOBlitSourceType sourceType, IOBlitOperation *operation, void *source);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioblitterptr)*