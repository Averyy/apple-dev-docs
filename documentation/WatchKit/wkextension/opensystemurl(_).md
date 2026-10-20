# openSystemURL(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Opens the specified system URL.

**Availability**:
- watchOS 2.0+ - Deprecated in 9.2 (renamed: WKApplication)

## Declaration

```swift
func openSystemURL(_ url: URL)
```

```objc
- (void) openSystemURL:(NSURL *) url;
```

#### Discussion

Use this method to initiate phone calls or send messages. The URL you open is sent to the appropriate system app for handling, at which point the user can choose whether to continue the operation.

## Parameters

- `url`: A URL that supports the `tel:` or `sms:` scheme. For information about the format of these URL schemes, see [Apple URL Scheme Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/opensystemurl(_:))*