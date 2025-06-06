# kUCCollateDigitsOverrideMask

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kUCCollateDigitsOverrideMask: Int { get }
```

#### Discussion

If the corresponding bit is set, then the number-handling behavior is specified by the remaining number-handling option bits, instead of by the collation information for the locale. If the bit is clear, the locale controls how numbers are handled and the remaining number-handling option bits are ignored. This option is available with Mac OS 9 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kuccollatedigitsoverridemask)*