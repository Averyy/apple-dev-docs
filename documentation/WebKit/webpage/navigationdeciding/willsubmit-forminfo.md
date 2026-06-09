# willSubmit(formInfo:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Allow the application to process form autofill information before a form submission actually takes place.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
mutating func willSubmit(formInfo: WebPage.FormInfo) async
```

#### Discussion

This is an informative callback only. The form values cannot be changed, nor can the navigation be changed to not submit a form.

The form submission will not actually proceed until after this callback asynchronously resolves.

## Parameters

- `formInfo`: The form values that will be submitted for this navigation


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/willsubmit(forminfo:))*