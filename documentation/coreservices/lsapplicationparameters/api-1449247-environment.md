# environment

**Framework**: Core Services  
**Kind**: structp

A dictionary of `CFStringRef` keysand values for environment variables to set in the launched process.The value of this field can be `NULL`.

**Availability**:
- macOS 10.4+ - Deprecated in 10.10

## Declaration

```swift
var environment: Unmanaged<CFDictionary>!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lsapplicationparameters/1449247-environment)*