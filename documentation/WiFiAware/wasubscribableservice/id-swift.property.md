# id

**Framework**: Wi-Fi Aware  
**Kind**: property  
**Role**: Instance Property

A stable ID that can be used to identify this subscribable service.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var id: WASubscribableService.ID { get }
```

#### Discussion

The ID is stable for a given unique service name.

## See Also

### Checking a service name and ID
- [WASubscribableService.ID](./id-swift.typealias.md)
  The type of value that uniquely identifies the service.
- [let name: String](./name.md)
  The full name of the service, as sent over the air.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wasubscribableservice/id-swift.property)*