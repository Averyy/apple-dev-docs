# openSystemURL(_:)

**Framework**: Watchkit  
**Kind**: method

Opens the specified system URL.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
func openSystemURL(_ url: URL)
```

#### Discussion

Use this method to initiate phone calls or send messages. The URL you open is sent to the appropriate system app for handling, at which point the user can choose whether to continue the operation.

## Parameters

- `url`: A URL that supports the   or   scheme. For information about the format of these URL schemes, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/opensystemurl(_:))*