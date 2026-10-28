# relevance()

**Framework**: WidgetKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides a collection of conditions under which a specific widget could be relevant.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
func relevance() async -> WidgetRelevance<Self.Configuration>
```

## Mentions

- [Increasing the visibility of widgets in Smart Stacks](../widget-suggestions-in-smart-stacks.md)

## Discussion

The system can use the relevance to show this widget when the conditions for the relevance match the current state.

## See Also

### Generating relevance entries
- [func entry(configuration: Self.Configuration, context: Self.Context) async throws -> Self.Entry](./entry%28configuration,context%29.md)
  Provides the entry used to render a widget for a specific relevance configuration.
- [func placeholder(context: Self.Context) -> Self.Entry](./placeholder%28context%29.md)
  Provides the entry representing a placeholder version of the widget.
- [struct RelevanceEntriesProviderContext](../relevanceentriesprovidercontext.md)
  An object that contains details about how a widget is rendered, including its size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/relevanceentriesprovider/relevance())*