# subscribedService

**Framework**: Wi-Fi Aware  
**Kind**: property  
**Role**: Instance Property

The subscribable service that is, or can be, connected.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var subscribedService: WASubscribableService? { get }
```

## Discussion

Use `nil` if a subscribable service isn’t in use.

## See Also

### Getting the service
- [var publishedService: WAPublishableService?](./publishedservice.md)
  The publishable service that is, or can be, connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/waendpoint/subscribedservice)*