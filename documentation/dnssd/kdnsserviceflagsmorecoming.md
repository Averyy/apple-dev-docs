# kDNSServiceFlagsMoreComing

**Framework**: dnssd  
**Kind**: var

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var kDNSServiceFlagsMoreComing: UInt32 { get }
```

#### Discussion

MoreComing indicates to a callback that at least one more result is queued and will be delivered following immediately after this one. When the MoreComing flag is set, applications should not immediately update their UI, because this can result in a great deal of ugly flickering on the screen, and can waste a great deal of CPU time repeatedly updating the screen with content that is then immediately erased, over and over. Applications should wait until MoreComing is not set, and then update their UI when no more changes are imminent.

When MoreComing is not set, that doesn’t mean there will be no more answers EVER, just that there are no more answers immediately available right now at this instant. If more answers become available in the future they will be delivered as usual.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsmorecoming)*