# openSystemURL(_:)

**Framework**: WatchKit  
**Kind**: method

Opens the specified system URL.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
func openSystemURL(_ url: URL)
```

#### Discussion

Use this method to initiate phone calls or send messages. The URL you open is sent to the appropriate system app for handling, at which point the user can choose whether to continue the operation.

## Parameters

- `url`: A URL that supports the `tel:` or `sms:` scheme. For information about the format of these URL schemes, see [`Apple URL Scheme Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/opensystemurl(_:))*