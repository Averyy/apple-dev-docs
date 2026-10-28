# entry(configuration:context:)

**Framework**: WidgetKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the entry used to render a widget for a specific relevance configuration.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
func entry(configuration: Self.Configuration, context: Self.Context) async throws -> Self.Entry
```

## Mentions

- [Increasing the visibility of widgets in Smart Stacks](../widget-suggestions-in-smart-stacks.md)

## Return Value

A relevance entry representing the widget in this configuration.

## Parameters

- `configuration`: The configuration for when this widget is relevant.
- `context`: An object describing the context to show the widget in.

## See Also

### Generating relevance entries
- [func relevance() async -> WidgetRelevance<Self.Configuration>](./relevance%28%29.md)
  Provides a collection of conditions under which a specific widget could be relevant.
- [func placeholder(context: Self.Context) -> Self.Entry](./placeholder%28context%29.md)
  Provides the entry representing a placeholder version of the widget.
- [struct RelevanceEntriesProviderContext](../relevanceentriesprovidercontext.md)
  An object that contains details about how a widget is rendered, including its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/relevanceentriesprovider/entry(configuration:context:))*