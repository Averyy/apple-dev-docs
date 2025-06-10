# WAError.connectionRequirementsNotMet(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs because of missing requirements.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
case connectionRequirementsNotMet(WAError.ConnectionRequirementsNotMetDetails)
```

#### Discussion

This error indicates that a remote device didn’t supply or support the required Wi-Fi Aware functionality or security mechanisms.

## See Also

- [WAError.ConnectionRequirementsNotMetDetails](waerror/connectionrequirementsnotmetdetails.md)
  The optional details describing the missing requirements that failed the connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/connectionrequirementsnotmet(_:))*