# init(configuration:)

**Framework**: WebKit  
**Kind**: init

Create a new WebPage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
convenience init(configuration: WebPage.Configuration = Configuration())
```

## Parameters

- `configuration`: A   value to use when initializing the page.

## See Also

- [WebPage.Configuration](webpage/configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [convenience init(configuration: WebPage.Configuration, dialogPresenter: some WebPage.DialogPresenting)](webpage/init(configuration:dialogpresenter:).md)
  Create a new WebPage.
- [convenience init(configuration: WebPage.Configuration, navigationDecider: some WebPage.NavigationDeciding)](webpage/init(configuration:navigationdecider:).md)
  Create a new WebPage.
- [convenience init(configuration: WebPage.Configuration, navigationDecider: some WebPage.NavigationDeciding, dialogPresenter: some WebPage.DialogPresenting)](webpage/init(configuration:navigationdecider:dialogpresenter:).md)
  Create a new WebPage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/init(configuration:))*