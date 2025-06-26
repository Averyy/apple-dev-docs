# init(configuration:dialogPresenter:)

**Framework**: WebKit  
**Kind**: init

Create a new WebPage.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
convenience init(configuration: WebPage.Configuration = Configuration(), dialogPresenter: some WebPage.DialogPresenting)
```

## Parameters

- `configuration`: A   value to use when initializing the page.
- `dialogPresenter`: A dialog presenter which controls how JS dialogs are handled.

## See Also

- [WebPage.Configuration](webpage/configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [convenience init(configuration: WebPage.Configuration)](webpage/init(configuration:).md)
  Create a new WebPage.
- [convenience init(configuration: WebPage.Configuration, navigationDecider: some WebPage.NavigationDeciding)](webpage/init(configuration:navigationdecider:).md)
  Create a new WebPage.
- [convenience init(configuration: WebPage.Configuration, navigationDecider: some WebPage.NavigationDeciding, dialogPresenter: some WebPage.DialogPresenting)](webpage/init(configuration:navigationdecider:dialogpresenter:).md)
  Create a new WebPage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/init(configuration:dialogpresenter:))*