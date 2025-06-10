# iterateObjects

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.14+

## Declaration

```swift
bool iterateObjects(void *refcon, bool (*callback)(void *refcon, const OSSymbol *key, OSObject *object));
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osdictionary/2967352-iterateobjects)*