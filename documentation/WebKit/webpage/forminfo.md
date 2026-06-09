# WebPage.FormInfo

**Framework**: WebKit  
**Kind**: struct

A type that contains information about a form submission from a webpage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
struct FormInfo
```

## Topics

### Instance Properties
- [var formValues: [String : String]](webpage/forminfo/formvalues.md)
  A dictionary of the form values that will be submitted during the navigation.
- [var httpMethod: String](webpage/forminfo/httpmethod.md)
  The HTTP method used to submit the form; generally either @“GET” or @“POST”.
- [var sourceFrame: WebPage.FrameInfo](webpage/forminfo/sourceframe.md)
  The frame that caused the form submission.
- [var submissionURL: URL](webpage/forminfo/submissionurl.md)
  The URL that the frame is being navigated to.
- [var targetFrame: WebPage.FrameInfo](webpage/forminfo/targetframe.md)
  The frame where the form is being submitted will cause a navigation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/forminfo)*