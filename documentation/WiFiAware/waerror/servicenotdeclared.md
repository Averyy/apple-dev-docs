# WAError.serviceNotDeclared(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs if your app didn’t declared the necessary services.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
case serviceNotDeclared(WAError.ServiceNotDeclaredDetails)
```

#### Discussion

This error indicates that your app declares services in the `Info.plist`.

## See Also

- [WAError.ServiceNotDeclaredDetails](waerror/servicenotdeclareddetails.md)
  The optional details that describe the app service wasn’t declared.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/servicenotdeclared(_:))*