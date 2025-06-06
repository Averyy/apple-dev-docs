# cancel()

**Framework**: Videosubscriberaccount  
**Kind**: method

Cancels an in-progress request for subscriber account information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- macOS ?+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

#### Discussion

Your app uses this method to notify a [`VSAccountManager`](vsaccountmanager.md) instance to cancel the current request for subscriber account information. No guarantees are made that the cancellation request will succeed or finish immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsaccountmanagerresult/cancel())*