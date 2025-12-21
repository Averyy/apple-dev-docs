# placeholder(context:)

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Provides the entry representing a placeholder version of the widget.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
func placeholder(context: Self.Context) -> Self.Entry
```

## Mentions

- [Increasing the visibility of widgets in Smart Stacks](widget-suggestions-in-smart-stacks.md)

#### Return Value

A relevance entry that represents a placeholder version of the widget.

## Parameters

- `context`: An object describing the context to show the widget in.

## See Also

- [func entry(configuration: Self.Configuration, context: Self.Context) async throws -> Self.Entry](relevanceentriesprovider/entry(configuration:context:).md)
  Provides the entry used to render a widget for a specific relevance configuration.
- [func relevance() async -> WidgetRelevance<Self.Configuration>](relevanceentriesprovider/relevance.md)
  Provides a collection of conditions under which a specific widget could be relevant.
- [struct RelevanceEntriesProviderContext](relevanceentriesprovidercontext.md)
  An object that contains details about how a widget is rendered, including its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/relevanceentriesprovider/placeholder(context:))*