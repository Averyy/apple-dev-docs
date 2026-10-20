# init(configuration:navigationDecider:dialogPresenter:)

**Framework**: WebKit  
**Kind**: init  
**Role**: Initializer

Create a new WebPage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
convenience init(configuration: WebPage.Configuration = Configuration(), navigationDecider: some WebPage.NavigationDeciding, dialogPresenter: some WebPage.DialogPresenting)
```

## Parameters

- `configuration`: A [`WebPage.Configuration`](./configuration.md) value to use when initializing the page.
- `navigationDecider`: A navigation decider used to customize navigations that happen within the page.
- `dialogPresenter`: A dialog presenter which controls how JavaScript dialogs are handled.

## See Also

### Creating a WebPage
- [WebPage.Configuration](./configuration.md)
  A configuration type that specifies the preferences and behaviors of a webpage.
- [convenience init(configuration: WebPage.Configuration)](./init%28configuration%29.md)
  Create a new WebPage.
- [convenience init(configuration: WebPage.Configuration, dialogPresenter: some WebPage.DialogPresenting)](./init%28configuration,dialogpresenter%29.md)
  Create a new WebPage.
- [convenience init(configuration: WebPage.Configuration, navigationDecider: some WebPage.NavigationDeciding)](./init%28configuration,navigationdecider%29.md)
  Create a new WebPage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/init(configuration:navigationdecider:dialogpresenter:))*