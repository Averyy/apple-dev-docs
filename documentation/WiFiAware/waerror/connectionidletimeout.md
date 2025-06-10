# WAError.connectionIdleTimeout(_:)

**Framework**: Wi-Fi Aware  
**Kind**: case

An error that occurs due to an idle or unused connection.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
case connectionIdleTimeout(WAError.ConnectionIdleTimeoutDetails)
```

#### Discussion

The service closes if the connection is idle or unused for an excessive duration.

## See Also

- [WAError.ConnectionIdleTimeoutDetails](waerror/connectionidletimeoutdetails.md)
  The optional details describing the missing resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waerror/connectionidletimeout(_:))*