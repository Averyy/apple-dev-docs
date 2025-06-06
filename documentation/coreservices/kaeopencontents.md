# kAEOpenContents

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
var kAEOpenContents: AEEventID { get }
```

#### Discussion

Event that provides an application with dragged content, such as text or an image. Sent, for example, when a user drags an image file onto your application’s icon in the Dock. The application can use the content as desired—for example, if no document is currently open, it might open a new document and insert the provided text or image.

For more information, see Handling Apple Events Sent by the Mac OS in Responding to Apple Events in Apple Events Programming Guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kaeopencontents)*