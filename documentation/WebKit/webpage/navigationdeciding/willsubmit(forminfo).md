# willSubmit(formInfo:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Allow the application to process form autofill information before a form submission actually takes place.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

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

## Default Implementations

### WebPage.NavigationDeciding Implementations
- [func willSubmit(formInfo: WebPage.FormInfo) async](./willsubmit%28forminfo%29-1wa4u.md)
  By default, this method does nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/willsubmit(forminfo:))*