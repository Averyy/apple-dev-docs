# VSCheckAccessOption

**Framework**: Videosubscriberaccount  
**Kind**: struct

The options your app uses when checking access status.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct VSCheckAccessOption
```

## Topics

### Options
- [static let prompt: VSCheckAccessOption](vscheckaccessoption/prompt.md)
  A Boolean that indicates whether your app can prompt the user to grant access.
### Creating check access options
- [init(rawValue: String)](vscheckaccessoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func checkAccessStatus(options: [VSCheckAccessOption : Any], completionHandler: (VSAccountAccessStatus, (any Error)?) -> Void)](vsaccountmanager/checkaccessstatus(options:completionhandler:).md)
  Checks your app’s access to user subscription information, and requests access if needed.
- [enum VSAccountAccessStatus](vsaccountaccessstatus.md)
  Constants that represent your app’s access status to the user’s subscription information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vscheckaccessoption)*