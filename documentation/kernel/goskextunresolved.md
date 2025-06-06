# gOSKextUnresolved

**Framework**: Kernel  
**Kind**: data

The value to which a kext's unresolved, weakly-referenced symbols are bound.

**Availability**:
- macOS 10.6+

## Declaration

```swift
const void *const gOSKextUnresolved;
```

#### Discussion

A kext must test a weak symbol before using it. A weak symbol is only safe to use if it is not equal to `gOSKextUnresolved`.

Example for a weak symbol named `foo`:

```occ
 
 
      if (&foo != gOSKextUnresolved) {
          foo();
      } else {
          printf("foo() is not supported\n");
      }
 
 
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/goskextunresolved)*