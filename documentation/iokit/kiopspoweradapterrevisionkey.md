# kIOPSPowerAdapterRevisionKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

The power adapter's revision. The value associated with this key is a CFNumberRef kCFNumberIntType integer value

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPSPowerAdapterRevisionKey
```

#### Discussion

This key may be present in the dictionary returned from [`IOPSCopyExternalPowerAdapterDetails`](./api-1523866-iopscopyexternalpoweradapterdeta.md) This key might not be defined in the adapter details dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopspoweradapterrevisionkey)*