# kIOStorageFeaturesKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of any object in the storage stack.

**Availability**:
- macOS 10.5+

## Declaration

```c
#define kIOStorageFeaturesKey
```

#### Discussion

kIOStorageFeaturesKey is a property of any object in the storage stack that wishes to express support of additional features, such as Force Unit Access. It is typically defined in the device object below the block storage driver object. It has an OSDictionary value, where each entry describes one given feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiostoragefeatureskey)*