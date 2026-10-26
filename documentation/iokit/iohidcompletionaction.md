# IOHIDCompletionAction

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```c
typedef void (*IOHIDCompletionAction)(void *target, void *parameter, IOReturn status, uint32_t bufferSizeRemaining);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohidcompletionaction)*