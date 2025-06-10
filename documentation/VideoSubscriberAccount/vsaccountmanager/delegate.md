# delegate

**Framework**: Video Subscriber Account  
**Kind**: property

The delegate of the account manager object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any VSAccountManagerDelegate)? { get set }
```

#### Discussion

The system notifies the delegate when the app needs to present or dismiss authentication views, or decide whether to authenticate the person with their chosen provider.

The delegate must adopt the [`VSAccountManagerDelegate`](vsaccountmanagerdelegate.md) protocol.

## See Also

- [protocol VSAccountManagerDelegate](vsaccountmanagerdelegate.md)
  The methods you use to respond to authentication view controller requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanager/delegate)*