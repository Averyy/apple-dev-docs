# appRef

**Framework**: Core Services  
**Kind**: structp

A pointer to a file-system reference designatingthe application to launch; see the  inthe Carbon File Management Documentation for a description of the `FSRef` datatype. Set this field to `NULL` torequest that each item in the `itemRefs` arraybe opened in its own preferred application.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

## Declaration

```swift
var appRef: UnsafePointer<FSRef>!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1448321-appref)*